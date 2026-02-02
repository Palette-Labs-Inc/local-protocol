# Local Protocol Development Commands

# Default recipe - show help
default:
  @just --list

# --- paths ---
root_dir := justfile_directory()
py_sdk_dir := root_dir / "packages/python-sdk"
conformance_dir := root_dir / "packages/conformance"
schema_dir := root_dir / "schemas"

# --- SDK & Code Generation ---

# Generate Python SDK from JSON schemas
generate: build-python-sdk

# Build/regenerate Python SDK from schemas
build-python-sdk:
  @echo "Generating Python SDK from schemas..."
  @chmod +x "{{py_sdk_dir}}/generate_models.sh"
  @cd "{{py_sdk_dir}}" && ./generate_models.sh

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

# Lint Python code
lint:
  @echo "Linting Python code..."
  @cd "{{py_sdk_dir}}" && uv run ruff check .
  @cd "{{conformance_dir}}" && uv run ruff check .

# --- Cleanup ---

# Clean generated files
clean:
  @echo "Cleaning generated files..."
  @rm -rf "{{py_sdk_dir}}/src/local_protocol_sdk/models"
  @find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
  @find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
  @find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
