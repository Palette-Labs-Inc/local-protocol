"""Discovery and health endpoints."""

import hashlib
import json
from pathlib import Path
import re
from typing import Any

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

router = APIRouter()

_REVERSE_DOMAIN_RE = re.compile(r"^[a-z][a-z0-9]*(?:\.[a-z][a-z0-9_]*)+$")
_DATE_VERSION_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
_REPO_ROOT = Path(__file__).resolve().parents[4]
_SCHEMAS_DIR = _REPO_ROOT / "schemas"
_UCP_VERSION_FILE = _SCHEMAS_DIR / "ucp" / "VERSION"

_REVERSE_DOMAIN_PREFIX = "xyz.localprotocol"
_SCHEMA_BASE_URL = "https://localprotocol.xyz/schemas"
_DOCS_BASE_URL = "https://localprotocol.xyz/docs"
_OPENAPI_SCHEMA_URL = (
  "https://localprotocol.xyz/openapi/specs/local-protocol.v1.openapi.json"
)

_SKIP_SCHEMA_DIRS = frozenset({"ucp", "shared"})


def _load_ucp_version() -> str:
  """Load canonical UCP version from vendored schema metadata."""
  version = _UCP_VERSION_FILE.read_text(encoding="utf-8").strip()
  if not _DATE_VERSION_RE.fullmatch(version):
    raise ValueError(
      f"Invalid UCP version in {_UCP_VERSION_FILE}; expected YYYY-MM-DD."
    )
  return version


def _discover_capabilities() -> list[tuple[str, str]]:
  """Discover capabilities by traversing schemas/*/{name}.json.

  Returns a list of (reverse_domain_name, schema_dir_name) tuples for every
  schema subdirectory that contains a root schema file matching its directory
  name (e.g. ``schemas/delivery/delivery.json``).
  """
  capabilities: list[tuple[str, str]] = []
  for child in sorted(_SCHEMAS_DIR.iterdir()):
    if child.name in _SKIP_SCHEMA_DIRS or not child.is_dir():
      continue
    if (child / f"{child.name}.json").is_file():
      name = f"{_REVERSE_DOMAIN_PREFIX}.{child.name}"
      if not _REVERSE_DOMAIN_RE.fullmatch(name):
        raise ValueError(
          f"Derived capability name '{name}' from {child} "
          "is not a valid reverse-domain identifier."
        )
      capabilities.append((name, child.name))
  if not capabilities:
    raise ValueError(f"No capability schema files found under {_SCHEMAS_DIR}")
  return capabilities


_UCP_VERSION = _load_ucp_version()
_UCP_CAPABILITIES = _discover_capabilities()


def _build_ucp_payload(base_url: str) -> dict[str, Any]:
  """Build a canonical UCP discovery payload.

  Service and capability names are auto-populated by traversing
  ``schemas/*/{name}.json`` root schema files at startup.
  """
  services: dict[str, Any] = {}
  capabilities: dict[str, Any] = {}

  for rdname, dirname in _UCP_CAPABILITIES:
    services[rdname] = [
      {
        "version": _UCP_VERSION,
        "spec": f"{_DOCS_BASE_URL}/getting-started/understanding-capabilities/",
        "transport": "rest",
        "endpoint": base_url,
        "schema": _OPENAPI_SCHEMA_URL,
      }
    ]
    capabilities[rdname] = [
      {
        "version": _UCP_VERSION,
        "spec": f"{_DOCS_BASE_URL}/capabilities/{dirname}/overview/",
        "schema": f"{_SCHEMA_BASE_URL}/{dirname}/{dirname}.json",
      }
    ]

  return {
    "ucp": {
      "version": _UCP_VERSION,
      "services": services,
      "capabilities": capabilities,
      "payment_handlers": {},
    }
  }


def _validate_ucp_payload(payload: dict[str, Any]) -> None:
  """Validate discovery shape against required UCP contracts."""
  ucp = payload.get("ucp")
  if not isinstance(ucp, dict):
    raise ValueError("Missing top-level 'ucp' object.")

  version = ucp.get("version")
  if not isinstance(version, str) or not _DATE_VERSION_RE.fullmatch(version):
    raise ValueError("Invalid ucp.version; expected YYYY-MM-DD.")

  for key in ("services", "capabilities", "payment_handlers"):
    if not isinstance(ucp.get(key), dict):
      raise ValueError(f"Invalid ucp.{key}; expected object registry.")

  services = ucp["services"]
  for service_name, entries in services.items():
    if not isinstance(service_name, str) or not _REVERSE_DOMAIN_RE.fullmatch(
      service_name
    ):
      raise ValueError(f"Invalid service key: {service_name}")
    if not isinstance(entries, list):
      raise ValueError(f"Invalid service entries for {service_name}")
    for entry in entries:
      if not isinstance(entry, dict):
        raise ValueError(f"Invalid service entry for {service_name}")
      for required in ("version", "spec", "transport"):
        if required not in entry:
          raise ValueError(f"Missing {required} in service {service_name}")
      _ALLOWED_TRANSPORTS = ("rest", "mcp", "a2a", "embedded")
      if not isinstance(entry["transport"], str):
        raise ValueError(
          f"Invalid transport type in service {service_name}; expected str."
        )
      if entry["transport"] not in _ALLOWED_TRANSPORTS:
        raise ValueError(
          f"Unknown transport '{entry['transport']}' in service "
          f"{service_name}; must be one of {_ALLOWED_TRANSPORTS}."
        )
      if (
        not isinstance(entry["version"], str)
        or not _DATE_VERSION_RE.fullmatch(entry["version"])
      ):
        raise ValueError(f"Invalid service version in {service_name}")
      if entry["transport"] in ("rest", "mcp"):
        for required in ("endpoint", "schema"):
          if required not in entry:
            raise ValueError(
              f"Missing {required} in {entry['transport']} service {service_name}"
            )
      if entry["transport"] == "a2a" and "endpoint" not in entry:
        raise ValueError(f"Missing endpoint in a2a service {service_name}")
      if entry["transport"] == "embedded" and "schema" not in entry:
        raise ValueError(f"Missing schema in embedded service {service_name}")

  capabilities = ucp["capabilities"]
  for capability_name, entries in capabilities.items():
    if not isinstance(capability_name, str) or not _REVERSE_DOMAIN_RE.fullmatch(
      capability_name
    ):
      raise ValueError(f"Invalid capability key: {capability_name}")
    if not isinstance(entries, list):
      raise ValueError(f"Invalid capability entries for {capability_name}")
    for entry in entries:
      if not isinstance(entry, dict):
        raise ValueError(f"Invalid capability entry for {capability_name}")
      for required in ("version", "spec", "schema"):
        if required not in entry:
          raise ValueError(f"Missing {required} in capability {capability_name}")
      if (
        not isinstance(entry["version"], str)
        or not _DATE_VERSION_RE.fullmatch(entry["version"])
      ):
        raise ValueError(f"Invalid capability version in {capability_name}")

  payment_handlers = ucp["payment_handlers"]
  for handler_name, entries in payment_handlers.items():
    if not isinstance(handler_name, str) or not _REVERSE_DOMAIN_RE.fullmatch(
      handler_name
    ):
      raise ValueError(f"Invalid payment handler key: {handler_name}")
    if not isinstance(entries, list):
      raise ValueError(f"Invalid payment handler entries for {handler_name}")
    for entry in entries:
      if not isinstance(entry, dict):
        raise ValueError(f"Invalid payment handler entry for {handler_name}")
      for required in ("id", "version"):
        if required not in entry:
          raise ValueError(
            f"Missing {required} in payment handler {handler_name}"
          )
      if (
        not isinstance(entry["version"], str)
        or not _DATE_VERSION_RE.fullmatch(entry["version"])
      ):
        raise ValueError(f"Invalid payment handler version in {handler_name}")


def _discovery_headers(payload: dict[str, Any]) -> dict[str, str]:
  """Compute cache and etag headers for discovery responses."""
  serialized = json.dumps(payload, sort_keys=True, separators=(",", ":"))
  etag = hashlib.sha256(serialized.encode("utf-8")).hexdigest()
  return {
    "Cache-Control": "public, max-age=300",
    "ETag": f"\"{etag}\"",
  }


@router.get("/.well-known/ucp")
async def well_known_ucp(request: Request) -> JSONResponse:
  """Canonical UCP discovery endpoint."""
  # Dynamically determine the base URL from the incoming request. This avoids hardcoding
  # and ensures correct URLs regardless of which host or port the server is running on,
  # which is important since server.py allows overriding host and port at launch time.
  base_url = f"{request.url.scheme}://{request.url.netloc}"
  payload = _build_ucp_payload(base_url)
  _validate_ucp_payload(payload)
  return JSONResponse(content=payload, headers=_discovery_headers(payload))


@router.get("/healthz")
async def health_check() -> dict:
  """Health check endpoint."""
  return {"status": "ok"}
