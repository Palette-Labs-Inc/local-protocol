"""Tests for delivery object event fields."""

import re
from datetime import datetime

from absl.testing import absltest

from integration_test_utils import IntegrationTestBase


class DeliveryEventTest(IntegrationTestBase):
  """Tests for delivery object event fields."""

  def test_delivery_has_event(self) -> None:
    """Delivery object MUST include event field."""
    delivery = self.create_delivery()
    self.assertIn("event", delivery)
    self.assertIsInstance(delivery["event"], str)

  def test_delivery_has_event_description(self) -> None:
    """Delivery object MUST include event_description field."""
    delivery = self.create_delivery()
    self.assertIn("event_description", delivery)
    self.assertIsInstance(delivery["event_description"], str)
    self.assertGreater(len(delivery["event_description"]), 0)

  def test_delivery_has_event_vocabulary(self) -> None:
    """Delivery object MUST include event_vocabulary field."""
    delivery = self.create_delivery()
    self.assertIn("event_vocabulary", delivery)
    self.assertIsInstance(delivery["event_vocabulary"], str)

  def test_delivery_has_updated_at(self) -> None:
    """Delivery object MUST include updated_at field."""
    delivery = self.create_delivery()
    self.assertIn("updated_at", delivery)
    self.assertIsInstance(delivery["updated_at"], str)

  def test_delivery_has_created_at(self) -> None:
    """Delivery object MUST include created_at field."""
    delivery = self.create_delivery()
    self.assertIn("created_at", delivery)
    self.assertIsInstance(delivery["created_at"], str)

  def test_delivery_has_ask_and_bid_ids(self) -> None:
    """Delivery object MUST include ask_id and bid_id."""
    delivery = self.create_delivery()
    self.assertIn("ask_id", delivery)
    self.assertIn("bid_id", delivery)

  def test_event_vocabulary_includes_version(self) -> None:
    """event_vocabulary MUST include @version."""
    delivery = self.create_delivery()
    vocabulary = delivery["event_vocabulary"]
    self.assertIn(
      "@",
      vocabulary,
      f"event_vocabulary missing version: {vocabulary}",
    )

  def test_event_vocabulary_version_is_date_format(self) -> None:
    """event_vocabulary version MUST be valid YYYY-MM-DD format."""
    delivery = self.create_delivery()
    vocabulary = delivery["event_vocabulary"]
    parts = vocabulary.split("@")
    self.assertEqual(
      len(parts),
      2,
      f"Invalid event_vocabulary format: {vocabulary}",
    )
    self.assertRegex(
      parts[1],
      r"^\d{4}-\d{2}-\d{2}$",
      f"Invalid date version in event_vocabulary: {vocabulary}",
    )

  def test_event_exists_in_vocabulary(self) -> None:
    """Event ID MUST exist in declared vocabulary."""
    delivery = self.create_delivery()
    vocabulary_ref = delivery["event_vocabulary"]

    # Extract standard name from reference (e.g., "xyz.localprotocol.delivery.courier@2026-01-30" -> "courier")
    standard_name = vocabulary_ref.split("@")[0].split(".")[-1]

    # Load the standard and check that the event exists
    standard = self.load_standard(standard_name)
    self.assertIn(
      delivery["event"],
      standard["events"],
      f"Event '{delivery['event']}' not in vocabulary {vocabulary_ref}",
    )

  def test_updated_at_is_iso8601(self) -> None:
    """updated_at MUST be a valid ISO 8601 datetime."""
    delivery = self.create_delivery()
    updated_at = delivery["updated_at"]

    # Try parsing as ISO 8601
    try:
      datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
    except ValueError:
      self.fail(f"updated_at is not valid ISO 8601: {updated_at}")

  def test_initial_event_is_created(self) -> None:
    """New delivery MUST start with 'created' event."""
    delivery = self.create_delivery()
    self.assertEqual(
      delivery["event"],
      "created",
      "New delivery should start in 'created' state",
    )

  def test_get_delivery_by_id(self) -> None:
    """GET /deliveries/{id} MUST return the delivery."""
    delivery = self.create_delivery()
    response = self.client.get(f"/deliveries/{delivery['id']}")
    self.assert_response_status(response, 200)
    fetched = response.json()
    self.assertEqual(fetched["id"], delivery["id"])
    self.assertEqual(fetched["event"], delivery["event"])

  def test_get_nonexistent_delivery_returns_404(self) -> None:
    """GET /deliveries/{id} MUST return 404 for nonexistent delivery."""
    response = self.client.get("/deliveries/nonexistent-id")
    self.assert_response_status(response, 404)

  def test_list_deliveries(self) -> None:
    """GET /deliveries MUST return list of deliveries."""
    delivery = self.create_delivery()
    response = self.client.get("/deliveries")
    self.assert_response_status(response, 200)
    deliveries = response.json()
    self.assertIsInstance(deliveries, list)
    delivery_ids = [d["id"] for d in deliveries]
    self.assertIn(delivery["id"], delivery_ids)


if __name__ == "__main__":
  absltest.main()
