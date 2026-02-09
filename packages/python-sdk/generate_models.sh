#!/bin/bash
set -euo pipefail
# Generate Pydantic models from Local Protocol JSON Schemas.
#
# This script runs datamodel-code-generator against our JSON Schema directory
# to produce Pydantic v2 models. Before invoking the generator, it copies the
# schemas to a temp directory and applies two workarounds for known bugs in
# datamodel-code-generator (v0.53.0):
#
#   1. Strip $id fields.  The generator uses $id as the base URL when resolving
#      relative $ref values within that file. Our schemas declare $id pointing
#      to localprotocol.xyz, which is not a live JSON Schema host. This causes
#      the generator to attempt HTTP fetches that fail or return HTML.
#
#   2. Resolve relative $ref paths to absolute filesystem paths.  When file A
#      references file B in a different directory, and file B contains its own
#      relative $ref values, the generator incorrectly resolves B's refs
#      relative to A's directory instead of B's directory. Pre-resolving to
#      absolute paths eliminates this ambiguity.
#
# Both workarounds operate on the temp copy only; source schemas are not
# modified.
#
# These workarounds would become unnecessary for local-protocol schemas if
# localprotocol.xyz were live and serving the schemas (the generator would
# resolve $ref values against the live host). Even then, the preprocessing
# is worth keeping: it makes generation fast, offline-capable, and immune to
# drift between hosted and local schemas. The UCP vendoring (schemas/ucp/)
# is a separate concern — it depends on ucp.dev hosting being fixed.
#
# See also:
#   schemas/ucp/README.md         — vendored UCP schema dependencies
#   docs/ucp-stale-latest-issue.md — upstream UCP hosting issues

cd "$(dirname "$0")"

OUTPUT_DIR="src/local_protocol_sdk/models"
SCHEMA_DIR="../../schemas/"

echo "Generating Pydantic models from $SCHEMA_DIR..."

if ! command -v uv &> /dev/null; then
    echo "Error: uv not found."
    echo "Please install uv: curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi

# --------------------------------------------------------------------------
# Pre-processing: copy schemas to temp dir and fix known generator bugs.
# --------------------------------------------------------------------------
TMPDIR="$(mktemp -d)"
trap 'rm -rf "$TMPDIR"' EXIT
cp -R "$SCHEMA_DIR" "$TMPDIR/schemas"
# Remove non-JSON files (e.g. README.md) that would confuse the generator.
find "$TMPDIR/schemas" -not -name '*.json' -type f -delete
python3 -c "
import json, os, sys

def process_refs(obj, base_dir):
    \"\"\"Recursively resolve relative ref paths to absolute filesystem paths.\"\"\"
    if isinstance(obj, dict):
        if '\$ref' in obj:
            ref = obj['\$ref']
            # Split JSON Pointer fragment (e.g. #/\$defs/foo) from file path
            if '#' in ref:
                file_part, fragment = ref.split('#', 1)
            else:
                file_part, fragment = ref, None
            # Only touch relative filesystem refs; leave http(s) and absolute
            # paths alone, and skip pure-fragment refs like '#' or '#/\$defs/x'.
            if file_part and not file_part.startswith(('http://', 'https://', '/')):
                abs_path = os.path.normpath(os.path.join(base_dir, file_part))
                obj['\$ref'] = abs_path + ('#' + fragment if fragment else '')
        for v in obj.values():
            process_refs(v, base_dir)
    elif isinstance(obj, list):
        for item in obj:
            process_refs(item, base_dir)

schema_root = sys.argv[1]
for dirpath, _, filenames in os.walk(schema_root):
    for fn in filenames:
        if not fn.endswith('.json'):
            continue
        path = os.path.join(dirpath, fn)
        with open(path) as f:
            data = json.load(f)
        # Workaround 1: strip \$id to prevent base-URL hijacking.
        data.pop('\$id', None)
        # Workaround 2: absolutify relative \$ref paths.
        process_refs(data, dirpath)
        with open(path, 'w') as f:
            json.dump(data, f, indent=2)
            f.write('\n')
" "$TMPDIR/schemas"

# --------------------------------------------------------------------------
# Generation
# --------------------------------------------------------------------------
rm -rf "$OUTPUT_DIR"
mkdir -p "$OUTPUT_DIR"

uv run \
    --link-mode=copy \
    --extra-index-url https://pypi.org/simple python \
    -m datamodel_code_generator \
    --input "$TMPDIR/schemas" \
    --input-file-type jsonschema \
    --output "$OUTPUT_DIR" \
    --output-model-type pydantic_v2.BaseModel \
    --use-schema-description \
    --field-constraints \
    --use-field-description \
    --enum-field-as-literal all \
    --disable-timestamp \
    --use-double-quotes \
    --no-use-annotated \
    --allow-extra-fields \
    --formatters ruff-format ruff-check

echo "Done. Models generated in $OUTPUT_DIR"
