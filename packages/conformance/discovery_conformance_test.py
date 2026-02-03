"""Tests for discovery profile conformance declarations."""

from absl.testing import absltest

from integration_test_utils import IntegrationTestBase


class DiscoveryConformanceTest(IntegrationTestBase):
  """Tests for discovery profile conformance declarations."""

  def test_discovery_has_capabilities(self) -> None:
    """Discovery response MUST include capabilities."""
    response = self.client.get("/.well-known/local-protocol")
    self.assert_response_status(response, 200)
    data = response.json()
    self.assertIn("capabilities", data)
    self.assertIsInstance(data["capabilities"], dict)

  def test_discovery_has_delivery_capability(self) -> None:
    """Discovery MUST declare delivery capability."""
    response = self.client.get("/.well-known/local-protocol")
    data = response.json()
    self.assertIn("delivery", data.get("capabilities", {}))

  def test_delivery_capability_has_conforms_to(self) -> None:
    """Delivery capability MUST declare conforms_to."""
    response = self.client.get("/.well-known/local-protocol")
    data = response.json()
    delivery = data.get("capabilities", {}).get("delivery", {})
    self.assertIn(
      "conforms_to",
      delivery,
      "Delivery capability must declare conforms_to",
    )
    self.assertIsInstance(delivery["conforms_to"], list)

  def test_conforms_to_is_not_empty(self) -> None:
    """conforms_to MUST have at least one standard reference."""
    response = self.client.get("/.well-known/local-protocol")
    data = response.json()
    conforms_to = data["capabilities"]["delivery"]["conforms_to"]
    self.assertGreater(
      len(conforms_to),
      0,
      "conforms_to must have at least one standard reference",
    )

  def test_conforms_to_includes_version(self) -> None:
    """Standard references MUST include @version."""
    response = self.client.get("/.well-known/local-protocol")
    data = response.json()
    conforms_to = data["capabilities"]["delivery"]["conforms_to"]
    for ref in conforms_to:
      self.assertIn(
        "@",
        ref,
        f"Standard reference missing version: {ref}",
      )

  def test_conforms_to_version_is_date_format(self) -> None:
    """Standard reference versions MUST be valid YYYY-MM-DD format."""
    response = self.client.get("/.well-known/local-protocol")
    data = response.json()
    conforms_to = data["capabilities"]["delivery"]["conforms_to"]
    for ref in conforms_to:
      parts = ref.split("@")
      self.assertEqual(
        len(parts),
        2,
        f"Invalid standard reference format: {ref}",
      )
      self.assertRegex(
        parts[1],
        r"^\d{4}-\d{2}-\d{2}$",
        f"Invalid date version in reference: {ref}",
      )

  def test_conforms_to_references_known_standards(self) -> None:
    """Standard references SHOULD reference known standards."""
    response = self.client.get("/.well-known/local-protocol")
    data = response.json()
    conforms_to = data["capabilities"]["delivery"]["conforms_to"]

    known_standard_prefixes = [
      "xyz.localprotocol.delivery.courier",
    ]

    for ref in conforms_to:
      name = ref.split("@")[0]
      is_known = any(name == prefix for prefix in known_standard_prefixes)
      self.assertTrue(
        is_known,
        f"Unknown standard reference: {ref}. "
        f"Known standards: {known_standard_prefixes}",
      )

  def test_conforms_to_courier_standard(self) -> None:
    """conforms_to SHOULD include courier standard."""
    response = self.client.get("/.well-known/local-protocol")
    data = response.json()
    conforms_to = data["capabilities"]["delivery"]["conforms_to"]

    has_courier = any(
      ref.startswith("xyz.localprotocol.delivery.courier@")
      for ref in conforms_to
    )
    self.assertTrue(
      has_courier,
      "Courier standard should be declared in conforms_to",
    )


if __name__ == "__main__":
  absltest.main()
