"""Tests for canonical UCP discovery profile conformance."""

import re
from typing import Any

from absl.testing import absltest

from integration_test_utils import IntegrationTestBase


_REVERSE_DOMAIN_RE = re.compile(r"^[a-z][a-z0-9]*(?:\.[a-z][a-z0-9_]*)+$")
_DATE_VERSION_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


class DiscoveryConformanceTest(IntegrationTestBase):
  """Tests for `/.well-known/ucp` profile conformance."""

  def _get_ucp_payload(self) -> dict[str, Any]:
    response = self.http_client.get("/.well-known/ucp")
    self.assert_response_status(response, 200)
    body = response.json()
    self.assertIsInstance(body, dict)
    self.assertIn("ucp", body)
    self.assertIsInstance(body["ucp"], dict)
    return body["ucp"]

  def test_discovery_headers_include_cache_and_etag(self) -> None:
    """Canonical discovery SHOULD expose cache and etag headers."""
    response = self.http_client.get("/.well-known/ucp")
    self.assert_response_status(response, 200)
    self.assertIn("cache-control", response.headers)
    self.assertIn("etag", response.headers)

  def test_discovery_has_required_ucp_fields(self) -> None:
    """UCP discovery MUST include required top-level registries."""
    ucp = self._get_ucp_payload()
    for required in ("version", "services", "capabilities", "payment_handlers"):
      self.assertIn(required, ucp, f"Missing ucp.{required}")

  def test_ucp_version_uses_date_format(self) -> None:
    """UCP version MUST be YYYY-MM-DD."""
    ucp = self._get_ucp_payload()
    version = ucp["version"]
    self.assertIsInstance(version, str)
    self.assertRegex(version, _DATE_VERSION_RE)

  def test_ucp_registries_are_objects(self) -> None:
    """UCP registries MUST be keyed objects, not arrays."""
    ucp = self._get_ucp_payload()
    for key in ("services", "capabilities", "payment_handlers"):
      self.assertIsInstance(ucp[key], dict, f"ucp.{key} must be an object")

  def test_services_are_reverse_domain_keyed_arrays(self) -> None:
    """Service registry keys MUST be reverse-domain names mapping to arrays."""
    ucp = self._get_ucp_payload()
    services = ucp["services"]
    for key, value in services.items():
      self.assertRegex(key, _REVERSE_DOMAIN_RE)
      self.assertIsInstance(value, list)

  def test_capabilities_are_reverse_domain_keyed_arrays(self) -> None:
    """Capability registry keys MUST be reverse-domain names mapping to arrays."""
    ucp = self._get_ucp_payload()
    capabilities = ucp["capabilities"]
    for key, value in capabilities.items():
      self.assertRegex(key, _REVERSE_DOMAIN_RE)
      self.assertIsInstance(value, list)

  def test_service_entries_have_ucp_required_fields(self) -> None:
    """Service entries MUST include UCP required fields by transport."""
    ucp = self._get_ucp_payload()
    for service_name, entries in ucp["services"].items():
      for entry in entries:
        self.assertIsInstance(entry, dict)
        for required in ("version", "spec", "transport"):
          self.assertIn(required, entry, f"{service_name} missing {required}")
        self.assertRegex(entry["version"], _DATE_VERSION_RE)
        transport = entry["transport"]
        if transport in ("rest", "mcp"):
          self.assertIn("endpoint", entry)
          self.assertIn("schema", entry)
        elif transport == "a2a":
          self.assertIn("endpoint", entry)
        elif transport == "embedded":
          self.assertIn("schema", entry)
        else:
          self.fail(f"Invalid service transport: {transport}")

  def test_capability_entries_have_ucp_required_fields(self) -> None:
    """Capability entries MUST include version, spec, and schema."""
    ucp = self._get_ucp_payload()
    for capability_name, entries in ucp["capabilities"].items():
      for entry in entries:
        self.assertIsInstance(entry, dict)
        for required in ("version", "spec", "schema"):
          self.assertIn(
            required,
            entry,
            f"{capability_name} missing {required}",
          )
        self.assertRegex(entry["version"], _DATE_VERSION_RE)

  def test_payment_handlers_registry_keys_are_reverse_domain(self) -> None:
    """Payment handler registry keys, if present, MUST be reverse-domain names."""
    ucp = self._get_ucp_payload()
    for key, value in ucp["payment_handlers"].items():
      self.assertRegex(key, _REVERSE_DOMAIN_RE)
      self.assertIsInstance(value, list)

  # ---------------------------------------------------------------------------
  # Local-Protocol-specific discovery assertions
  # ---------------------------------------------------------------------------

  def test_discovery_has_delivery_service(self) -> None:
    """Discovery MUST declare the delivery service."""
    ucp = self._get_ucp_payload()
    self.assertIn(
      "xyz.localprotocol.delivery",
      ucp["services"],
      "Delivery service must be declared in ucp.services",
    )
    entries = ucp["services"]["xyz.localprotocol.delivery"]
    self.assertGreater(
      len(entries),
      0,
      "Delivery service must have at least one entry",
    )

  def test_discovery_has_delivery_capability(self) -> None:
    """Discovery MUST declare the delivery capability."""
    ucp = self._get_ucp_payload()
    self.assertIn(
      "xyz.localprotocol.delivery",
      ucp["capabilities"],
      "Delivery capability must be declared in ucp.capabilities",
    )
    entries = ucp["capabilities"]["xyz.localprotocol.delivery"]
    self.assertGreater(
      len(entries),
      0,
      "Delivery capability must have at least one entry",
    )

  def test_delivery_service_declares_rest_transport(self) -> None:
    """At least one delivery service entry MUST use REST transport."""
    ucp = self._get_ucp_payload()
    entries = ucp["services"].get("xyz.localprotocol.delivery", [])
    has_rest = any(
      entry.get("transport") == "rest" for entry in entries
    )
    self.assertTrue(
      has_rest,
      "Delivery service must declare at least one REST transport entry",
    )

  def test_delivery_capability_has_schema_url(self) -> None:
    """Delivery capability entries MUST include a schema URL."""
    ucp = self._get_ucp_payload()
    entries = ucp["capabilities"].get("xyz.localprotocol.delivery", [])
    for entry in entries:
      self.assertIn(
        "schema",
        entry,
        "Delivery capability entry must include a schema URL",
      )
      self.assertIsInstance(entry["schema"], str)
      self.assertTrue(
        entry["schema"].startswith("http"),
        f"Delivery capability schema must be a URL, got: {entry['schema']}",
      )


if __name__ == "__main__":
  absltest.main()
