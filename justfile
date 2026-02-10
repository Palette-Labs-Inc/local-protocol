# Local Protocol Development Commands
#
# SDK generation uses Stainless (stl CLI). Config lives in .stainless/.
# The OpenAPI spec at openapi/specs/local-protocol.v1.openapi.json is the
# single source of truth -- it contains no generator-specific annotations.
# See DECISIONS.md (2026-02-09) for migration history from OpenAPI Generator
# and Speakeasy to Stainless.

# Default recipe - show help
default:
  @just --list

# --- paths ---
root_dir := justfile_directory()
conformance_dir := root_dir / "packages/conformance"
conformance_php_dir := root_dir / "packages/conformance-php"
schema_dir := root_dir / "schemas"
server_dir := root_dir / "apps/samples/server"
openapi_spec := root_dir / "openapi/specs/local-protocol.v1.openapi.json"

# --- SDK Generation (Stainless) ---

# Generate all SDKs (Python, PHP, TypeScript from OpenAPI via Stainless)
build-sdks: openapi-validate build-stainless-sdks

# Build all SDKs from OpenAPI spec (Stainless)
build-stainless-sdks:
  @echo "Generating Python, PHP, and TypeScript SDKs via Stainless..."
  @cd "{{root_dir}}" && stl preview

# Build a single Stainless target (e.g., just build-sdk python)
build-sdk target:
  @echo "Generating {{target}} SDK via Stainless..."
  @cd "{{root_dir}}" && stl preview --target {{target}}

# Validate the OpenAPI spec and Stainless config
openapi-validate:
  @cd "{{root_dir}}" && stl lint

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

# Run PHP conformance tests against a server
test-conformance-php server_url:
  @echo "Running PHP conformance tests against {{server_url}}..."
  @cd "{{conformance_php_dir}}" && TEST_API_BASE_URL={{server_url}} composer test

# Run all tests
test server_url: (test-conformance server_url)

# --- Development ---

# Format Python code
fmt:
  @echo "Formatting Python code..."
  @cd "{{conformance_dir}}" && uv run ruff format .
  @cd "{{server_dir}}" && uv run ruff format .

# Lint Python code
lint:
  @echo "Linting Python code..."
  @cd "{{conformance_dir}}" && uv run ruff check .
  @cd "{{server_dir}}" && uv run ruff check .

# --- Cleanup ---

# Clean generated SDK files
clean:
  @echo "Cleaning generated files..."
  @rm -rf "{{root_dir}}/sdks/local-protocol-python/src" "{{root_dir}}/sdks/local-protocol-python/tests"
  @rm -rf "{{root_dir}}/sdks/local-protocol-php/src" "{{root_dir}}/sdks/local-protocol-php/docs" "{{root_dir}}/sdks/local-protocol-php/vendor"
  @rm -rf "{{root_dir}}/sdks/local-protocol-typescript/src" "{{root_dir}}/sdks/local-protocol-typescript/docs" "{{root_dir}}/sdks/local-protocol-typescript/node_modules"
  @find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
  @find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
  @find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
