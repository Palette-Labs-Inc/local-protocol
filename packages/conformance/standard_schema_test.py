"""Tests for delivery standard schema validation."""

from absl.testing import absltest

from integration_test_utils import IntegrationTestBase


class StandardSchemaTest(IntegrationTestBase):
  """Tests for delivery event vocabulary schema validation."""

  def test_courier_standard_has_required_fields(self) -> None:
    """Courier standard MUST have name, version, title, and events fields."""
    courier = self.load_standard("courier")
    self.assertIn("name", courier)
    self.assertIn("version", courier)
    self.assertIn("title", courier)
    self.assertIn("events", courier)

  def test_courier_standard_has_required_events(self) -> None:
    """Courier standard MUST define all courier events."""
    courier = self.load_standard("courier")
    required_events = {
      "created",
      "assigned",
      "enroute_pickup",
      "arrived_pickup",
      "collected",
      "arrived_dropoff",
      "delivered",
      "canceled",
    }
    self.assertEqual(set(courier["events"].keys()), required_events)

  def test_courier_standard_name_format(self) -> None:
    """Courier standard name MUST follow reverse-DNS format."""
    courier = self.load_standard("courier")
    self.assertEqual(courier["name"], "xyz.localprotocol.delivery.courier")

  def test_courier_standard_version_is_date_format(self) -> None:
    """Courier standard version MUST be valid YYYY-MM-DD format."""
    courier = self.load_standard("courier")
    self.assertRegex(courier["version"], r"^\d{4}-\d{2}-\d{2}$")

  def test_courier_events_have_descriptions(self) -> None:
    """Each courier event MUST have a description."""
    courier = self.load_standard("courier")
    for event_id, event in courier["events"].items():
      self.assertIn(
        "description",
        event,
        f"Event '{event_id}' missing description",
      )
      self.assertIsInstance(event["description"], str)
      self.assertGreater(
        len(event["description"]),
        0,
        f"Event '{event_id}' has empty description",
      )

  def test_courier_standard_has_title(self) -> None:
    """Courier standard MUST have a human-readable title."""
    courier = self.load_standard("courier")
    self.assertIn("title", courier)
    self.assertIsInstance(courier["title"], str)
    self.assertGreater(len(courier["title"]), 0)

  def test_courier_standard_has_description(self) -> None:
    """Courier standard SHOULD have a description."""
    courier = self.load_standard("courier")
    if "description" in courier:
      self.assertIsInstance(courier["description"], str)
      self.assertGreater(len(courier["description"]), 0)


if __name__ == "__main__":
  absltest.main()
