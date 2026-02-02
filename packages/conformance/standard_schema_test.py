"""Tests for delivery standard schema validation."""

import re

from absl.testing import absltest

from integration_test_utils import IntegrationTestBase


class StandardSchemaTest(IntegrationTestBase):
  """Tests for delivery standard schema validation."""

  def test_core_standard_has_required_fields(self) -> None:
    """Core standard MUST have name, version, and events fields."""
    core = self.load_standard("core")
    self.assertIn("name", core)
    self.assertIn("version", core)
    self.assertIn("events", core)

  def test_core_standard_has_required_events(self) -> None:
    """Core standard MUST define pending, active, completed, failed."""
    core = self.load_standard("core")
    required_events = {"pending", "active", "completed", "failed"}
    self.assertEqual(set(core["events"].keys()), required_events)

  def test_core_standard_name_format(self) -> None:
    """Core standard name MUST follow reverse-DNS format."""
    core = self.load_standard("core")
    self.assertEqual(core["name"], "xyz.localprotocol.delivery.core")

  def test_core_standard_version_is_semver(self) -> None:
    """Core standard version MUST be valid semver."""
    core = self.load_standard("core")
    self.assertRegex(core["version"], r"^\d+\.\d+\.\d+$")

  def test_core_events_have_descriptions(self) -> None:
    """Each core event MUST have a description."""
    core = self.load_standard("core")
    for event_id, event in core["events"].items():
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

  def test_food_standard_has_required_fields(self) -> None:
    """Food standard MUST have name, version, extends, title, and events."""
    food = self.load_standard("food")
    self.assertIn("name", food)
    self.assertIn("version", food)
    self.assertIn("extends", food)
    self.assertIn("title", food)
    self.assertIn("events", food)

  def test_food_standard_extends_core(self) -> None:
    """Food standard MUST extend core standard."""
    food = self.load_standard("food")
    self.assertIn("extends", food)
    self.assertIsInstance(food["extends"], list)
    self.assertGreater(len(food["extends"]), 0)
    # Check that it extends core with version
    extends_core = any(
      ref.startswith("xyz.localprotocol.delivery.core@")
      for ref in food["extends"]
    )
    self.assertTrue(
      extends_core,
      f"Food standard must extend core, got: {food['extends']}",
    )

  def test_food_standard_includes_core_events(self) -> None:
    """Food standard MUST include all core events."""
    food = self.load_standard("food")
    core_events = {"pending", "active", "completed", "failed"}
    food_events = set(food["events"].keys())
    self.assertTrue(
      core_events.issubset(food_events),
      f"Food standard missing core events: {core_events - food_events}",
    )

  def test_food_standard_has_food_specific_events(self) -> None:
    """Food standard MUST have food-specific events."""
    food = self.load_standard("food")
    food_specific_events = {
      "order_placed",
      "preparing",
      "ready_for_pickup",
      "courier_assigned",
      "courier_at_pickup",
      "picked_up",
      "in_transit",
      "courier_at_dropoff",
      "delivered",
      "canceled",
    }
    food_events = set(food["events"].keys())
    self.assertTrue(
      food_specific_events.issubset(food_events),
      f"Food standard missing events: {food_specific_events - food_events}",
    )

  def test_food_standard_version_is_semver(self) -> None:
    """Food standard version MUST be valid semver."""
    food = self.load_standard("food")
    self.assertRegex(food["version"], r"^\d+\.\d+\.\d+$")

  def test_food_events_have_descriptions(self) -> None:
    """Each food event MUST have a description."""
    food = self.load_standard("food")
    for event_id, event in food["events"].items():
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

  def test_extends_reference_includes_version(self) -> None:
    """Extends references MUST include @version."""
    food = self.load_standard("food")
    for ref in food["extends"]:
      self.assertIn(
        "@",
        ref,
        f"Extends reference missing version: {ref}",
      )
      # Validate version format after @
      parts = ref.split("@")
      self.assertEqual(len(parts), 2, f"Invalid extends reference format: {ref}")
      self.assertRegex(
        parts[1],
        r"^\d+\.\d+\.\d+$",
        f"Invalid version in extends reference: {ref}",
      )


if __name__ == "__main__":
  absltest.main()
