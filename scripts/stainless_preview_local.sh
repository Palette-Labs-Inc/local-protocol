#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SOURCE_CONFIG="$ROOT_DIR/.stainless/stainless.yml"
TMP_CONFIG="$(mktemp "${TMPDIR:-/tmp}/stainless.local.XXXXXX.yml")"

cleanup() {
  rm -f "$TMP_CONFIG"
}
trap cleanup EXIT

# Local development runs should not require GitHub App access to production repos.
perl -pe 's/^(\s*production_repo:).*/\1 null/' "$SOURCE_CONFIG" >"$TMP_CONFIG"

cd "$ROOT_DIR"
stl preview --config "$TMP_CONFIG" "$@"
