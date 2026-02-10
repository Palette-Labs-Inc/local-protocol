#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

patch_if_exists() {
  local file="$1"
  shift
  if [[ ! -f "$file" ]]; then
    return 0
  fi
  "$@" "$file"
}

patch_typescript_package_json() {
  local file="$1"
  perl -0pi -e 's/"files":\s*\[\s*"\*\*\/\*"\s*\]/"files": [\n    "dist",\n    "README.md",\n    "LICENSE"\n  ]/g' "$file"
}

patch_typescript_client() {
  local file="$1"
  perl -0pi -e "s/import \\{ getPlatformHeaders \\} from '\\.\\/internal\\/detect-platform';\\n//g" "$file"
  perl -0pi -e 's/stainless-node-retry-/local-protocol-retry-/g' "$file"
  perl -0pi -e 's/\n\s*'\''X-Stainless-Retry-Count'\'': String\(retryCount\),\n\s*\.\.\.\(options\.timeout \? \{ '\''X-Stainless-Timeout'\'': String\(Math\.trunc\(options\.timeout \/ 1000\)\) \} : \{\}\),\n\s*\.\.\.getPlatformHeaders\(\),//g' "$file"
}

patch_python_client() {
  local file="$1"
  perl -0pi -e 's/raise TypeError\(\n\s*'"'"'"Could not resolve authentication method. Expected the api_key to be set. Or for the `Authorization` headers to be explicitly omitted"'"'"'\n\s*\)/raise _exceptions.LocalProtocolError(\n            "Could not resolve authentication method. Expected the api_key to be set. Or for the `Authorization` headers to be explicitly omitted"\n        )/g' "$file"
}

patch_python_pyproject() {
  local file="$1"
  perl -0pi -e 's/target-version = "py38"/target-version = "py39"/g' "$file"
}

patch_php_base_client() {
  local file="$1"
  perl -0pi -e 's/catch \(\\DateMalformedStringException\) \{/catch \(\\Exception\) \{/g' "$file"
  perl -0pi -e 's/time_nanosleep\(\(int\) \$floor, nanoseconds: \(int\) \(\$seconds - \$floor\) \* 10 \*\* 9\);/time_nanosleep((int) \$floor, nanoseconds: (int) ((\$seconds - \$floor) * 10 ** 9));/g' "$file"
}

patch_php_api_status_exception() {
  local file="$1"
  perl -0pi -e 's/\$summary \.= \$message\.PHP_EOL\.\$summary;/\$summary = \$message.PHP_EOL.\$summary;/g' "$file"
}

patch_php_client() {
  local file="$1"
  perl -0pi -e 's/public string \$apiKey;/protected string \$apiKey;/g' "$file"
}

patch_if_exists "$ROOT_DIR/sdks/local-protocol-typescript/package.json" patch_typescript_package_json
patch_if_exists "$ROOT_DIR/sdks/local-protocol-typescript/src/client.ts" patch_typescript_client
patch_if_exists "$ROOT_DIR/sdks/local-protocol-python/src/local_protocol/_client.py" patch_python_client
patch_if_exists "$ROOT_DIR/sdks/local-protocol-python/pyproject.toml" patch_python_pyproject
patch_if_exists "$ROOT_DIR/sdks/local-protocol-php/src/Core/BaseClient.php" patch_php_base_client
patch_if_exists "$ROOT_DIR/sdks/local-protocol-php/src/Core/Exceptions/APIStatusException.php" patch_php_api_status_exception
patch_if_exists "$ROOT_DIR/sdks/local-protocol-php/src/Client.php" patch_php_client

echo "Applied Stainless SDK post-generation patches."
