"""Tests for delivery event state transitions."""

from absl.testing import absltest

from integration_test_utils import IntegrationTestBase


class EventLifecycleTest(IntegrationTestBase):
  """Tests for delivery event state transitions using courier vocabulary."""

  def test_initial_event_is_created(self) -> None:
    """New delivery MUST start in 'created' state."""
    delivery = self.create_delivery()
    self.assertEqual(delivery["event"], "created")
    self.assertEqual(
      delivery["event_description"],
      "Delivery created",
    )

  def test_event_can_transition_to_assigned(self) -> None:
    """Delivery CAN transition from created to assigned."""
    delivery = self.create_delivery()
    response = self.update_delivery_event(
      delivery["id"],
      "assigned",
      "Courier assigned",
    )
    self.assert_response_status(response, 200)
    updated = response.json()
    self.assertEqual(updated["event"], "assigned")

  def test_event_can_transition_to_enroute_pickup(self) -> None:
    """Delivery CAN transition to enroute_pickup."""
    delivery = self.create_delivery()
    response = self.update_delivery_event(
      delivery["id"],
      "enroute_pickup",
      "Courier heading to pickup",
    )
    self.assert_response_status(response, 200)
    updated = response.json()
    self.assertEqual(updated["event"], "enroute_pickup")

  def test_event_can_transition_to_arrived_pickup(self) -> None:
    """Delivery CAN transition to arrived_pickup."""
    delivery = self.create_delivery()
    response = self.update_delivery_event(
      delivery["id"],
      "arrived_pickup",
      "Courier at pickup location",
    )
    self.assert_response_status(response, 200)
    updated = response.json()
    self.assertEqual(updated["event"], "arrived_pickup")

  def test_event_can_transition_to_collected(self) -> None:
    """Delivery CAN transition to collected."""
    delivery = self.create_delivery()
    response = self.update_delivery_event(
      delivery["id"],
      "collected",
      "Courier picked up",
    )
    self.assert_response_status(response, 200)
    updated = response.json()
    self.assertEqual(updated["event"], "collected")

  def test_event_can_transition_to_arrived_dropoff(self) -> None:
    """Delivery CAN transition to arrived_dropoff."""
    delivery = self.create_delivery()
    response = self.update_delivery_event(
      delivery["id"],
      "arrived_dropoff",
      "Courier at dropoff location",
    )
    self.assert_response_status(response, 200)
    updated = response.json()
    self.assertEqual(updated["event"], "arrived_dropoff")

  def test_event_can_transition_to_delivered(self) -> None:
    """Delivery CAN transition to delivered."""
    delivery = self.create_delivery()
    response = self.update_delivery_event(
      delivery["id"],
      "delivered",
      "Courier completed dropoff",
    )
    self.assert_response_status(response, 200)
    updated = response.json()
    self.assertEqual(updated["event"], "delivered")

  def test_event_can_transition_to_canceled(self) -> None:
    """Delivery CAN transition to canceled."""
    delivery = self.create_delivery()
    response = self.update_delivery_event(
      delivery["id"],
      "canceled",
      "Delivery canceled",
    )
    self.assert_response_status(response, 200)
    updated = response.json()
    self.assertEqual(updated["event"], "canceled")

  def test_updated_at_changes_on_transition(self) -> None:
    """updated_at MUST change when event transitions."""
    delivery = self.create_delivery()
    original_updated_at = delivery["updated_at"]

    # Small delay to ensure timestamp changes
    import time
    time.sleep(0.1)

    response = self.update_delivery_event(
      delivery["id"],
      "assigned",
      "Courier assigned",
    )
    self.assert_response_status(response, 200)
    updated = response.json()

    self.assertNotEqual(
      updated["updated_at"],
      original_updated_at,
      "updated_at should change on event transition",
    )

  def test_full_courier_lifecycle(self) -> None:
    """Courier delivery CAN follow full lifecycle sequence."""
    delivery = self.create_delivery()

    # Full courier delivery lifecycle
    lifecycle = [
      ("assigned", "Courier assigned"),
      ("enroute_pickup", "Courier heading to pickup"),
      ("arrived_pickup", "Courier at pickup location"),
      ("collected", "Courier picked up"),
      ("arrived_dropoff", "Courier at dropoff location"),
      ("delivered", "Courier completed dropoff"),
    ]

    for event, description in lifecycle:
      response = self.update_delivery_event(delivery["id"], event, description)
      self.assert_response_status(response, 200)
      updated = response.json()
      self.assertEqual(
        updated["event"],
        event,
        f"Failed to transition to {event}",
      )

    # Verify final state
    final_response = self.client.get(f"/deliveries/{delivery['id']}")
    self.assert_response_status(final_response, 200)
    final = final_response.json()
    self.assertEqual(final["event"], "delivered")


if __name__ == "__main__":
  absltest.main()
