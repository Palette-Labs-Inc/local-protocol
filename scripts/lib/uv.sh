#!/usr/bin/env bash
# Helper functions for uv package manager

resolve_uv() {
  if command -v uv &> /dev/null; then
    echo "uv"
  else
    echo "Error: uv not found. Install: curl -LsSf https://astral.sh/uv/install.sh | sh" >&2
    exit 1
  fi
}

uv_sync_or_install() {
  local project_dir="$1"
  local uv_bin="$2"

  if [[ -f "${project_dir}/pyproject.toml" ]]; then
    (cd "${project_dir}" && "${uv_bin}" sync)
  else
    echo "Warning: No pyproject.toml in ${project_dir}" >&2
  fi
}
