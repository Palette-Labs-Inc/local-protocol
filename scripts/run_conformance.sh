#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
source "${SCRIPT_DIR}/lib/uv.sh"

function wait_for_server() {
  local url="$1"
  local retries=30

  for _ in $(seq 1 "${retries}"); do
    if curl -fsS "${url}" >/dev/null 2>&1; then
      return 0
    fi
    sleep 1
  done

  echo "Error: server did not become ready at ${url}" >&2
  return 1
}

function find_free_port() {
  python3 - <<'PY'
import socket
s = socket.socket()
s.bind(("", 0))
port = s.getsockname()[1]
s.close()
print(port)
PY
}

# Parse arguments
SERVER_URL="${1:-}"
CONFORMANCE_DIR="${ROOT_DIR}/packages/conformance"
PY_SDK_DIR="${ROOT_DIR}/packages/python-sdk"
CONFORMANCE_INPUT="${CONFORMANCE_DIR}/test_data/delivery/conformance_input.json"
STANDARDS_DIR="${CONFORMANCE_DIR}/test_data/standards"
SCHEMA_DIR="${ROOT_DIR}/schemas"

UV_BIN="$(resolve_uv)"

# Sync dependencies
uv_sync_or_install "${CONFORMANCE_DIR}" "${UV_BIN}"
uv_sync_or_install "${PY_SDK_DIR}" "${UV_BIN}"

if [[ -z "${SERVER_URL}" ]]; then
  echo "Usage: $0 <server_url>"
  echo "Example: $0 http://localhost:8000"
  exit 1
fi

echo "Running conformance tests against ${SERVER_URL}..."

# Wait for server to be ready (either endpoint is acceptable)
if ! wait_for_server "${SERVER_URL}/healthz" && ! wait_for_server "${SERVER_URL}/.well-known/local-protocol"; then
  echo "Error: server not ready at ${SERVER_URL} (tried /healthz and /.well-known/local-protocol)" >&2
  exit 1
fi

# Run tests
shopt -s nullglob
for test_file in "${CONFORMANCE_DIR}"/*_test.py; do
  echo "Running $(basename "${test_file}")..."
  (cd "${CONFORMANCE_DIR}" && "${UV_BIN}" run python "${test_file}" \
    --server_url="${SERVER_URL}" \
    --conformance_input="${CONFORMANCE_INPUT}" \
    --standards_dir="${STANDARDS_DIR}" \
    --schema_dir="${SCHEMA_DIR}")
done

echo "Conformance tests completed."
