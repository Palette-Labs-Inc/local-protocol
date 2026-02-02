#!/bin/bash
set -euo pipefail
# Generate Pydantic models from Local Protocol JSON Schemas

cd "$(dirname "$0")"

OUTPUT_DIR="src/local_protocol_sdk/models"
SCHEMA_DIR="../../schemas/"

echo "Generating Pydantic models from $SCHEMA_DIR..."

if ! command -v uv &> /dev/null; then
    echo "Error: uv not found."
    echo "Please install uv: curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi

rm -rf "$OUTPUT_DIR"
mkdir -p "$OUTPUT_DIR"

uv run \
    --link-mode=copy \
    --extra-index-url https://pypi.org/simple python \
    -m datamodel_code_generator \
    --input "$SCHEMA_DIR" \
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
