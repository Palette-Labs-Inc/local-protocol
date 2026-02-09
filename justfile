# Local Protocol Development Commands

# Default recipe - show help
default:
  @just --list

# --- paths ---
root_dir := justfile_directory()
py_sdk_dir := root_dir / "packages/python-sdk"
conformance_dir := root_dir / "packages/conformance"
schema_dir := root_dir / "schemas"
server_dir := root_dir / "apps/samples/server"
openapi_spec := root_dir / "openapi/specs/local-protocol.v1.openapi.json"
# oag is no longer used — both PHP and TS SDKs now use Speakeasy

# --- SDK Generation ---

# Generate all SDKs (Python from JSON Schema, PHP and TypeScript from OpenAPI via Speakeasy)
build-sdks: build-python-sdk openapi-validate build-php-sdk build-ts-sdk

# Build Python SDK from JSON schemas (datamodel-code-generator / Pydantic v2)
build-python-sdk:
  @echo "Generating Python SDK from JSON schemas..."
  @chmod +x "{{py_sdk_dir}}/generate_models.sh"
  @cd "{{py_sdk_dir}}" && ./generate_models.sh

# Build PHP SDK from OpenAPI spec (Speakeasy)
build-php-sdk:
  @echo "Generating PHP SDK from OpenAPI spec..."
  @cd "{{root_dir}}/packages/php-sdk" && speakeasy run

# Build TypeScript SDK from OpenAPI spec (Speakeasy)
build-ts-sdk:
  @echo "Generating TypeScript SDK from OpenAPI spec..."
  @cd "{{root_dir}}/packages/typescript-sdk" && speakeasy run

# Validate the OpenAPI spec
openapi-validate:
  @speakeasy validate openapi -s "{{openapi_spec}}"

# --- Server ---

# Run sample server
run-server port="8000":
  @cd "{{server_dir}}" && uv run server.py --port {{port}}

# Run sample server with auto-reload
run-server-dev port="8000":
  @cd "{{server_dir}}" && uv run server.py --port {{port}} --reload

# --- Testing ---

# Run conformance tests against a server
test-conformance server_url:
  @echo "Running conformance tests against {{server_url}}..."
  @chmod +x "{{root_dir}}/scripts/run_conformance.sh"
  @"{{root_dir}}/scripts/run_conformance.sh" "{{server_url}}"

# Run all tests
test server_url: (test-conformance server_url)

# --- Development ---

# Format Python code
fmt:
  @echo "Formatting Python code..."
  @cd "{{py_sdk_dir}}" && uv run ruff format .
  @cd "{{conformance_dir}}" && uv run ruff format .
  @cd "{{server_dir}}" && uv run ruff format .

# Lint Python code
lint:
  @echo "Linting Python code..."
  @cd "{{py_sdk_dir}}" && uv run ruff check .
  @cd "{{conformance_dir}}" && uv run ruff check .
  @cd "{{server_dir}}" && uv run ruff check .

# --- Cleanup ---

# Clean generated SDK files (preserves Speakeasy config in .speakeasy/)
clean:
  @echo "Cleaning generated files..."
  @rm -rf "{{py_sdk_dir}}/src/local_protocol_sdk/models"
  @rm -rf "{{root_dir}}/packages/php-sdk/src" "{{root_dir}}/packages/php-sdk/docs" "{{root_dir}}/packages/php-sdk/vendor"
  @rm -rf "{{root_dir}}/packages/typescript-sdk/src" "{{root_dir}}/packages/typescript-sdk/docs" "{{root_dir}}/packages/typescript-sdk/node_modules"
  @find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
  @find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
  @find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
