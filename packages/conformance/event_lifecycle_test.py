"""Tests for delivery event state transitions."""

from absl.testing import absltest

from integration_test_utils import IntegrationTestBase


class EventLifecycleTest(IntegrationTestBase):
  """Tests for delivery event state transitions using courier vocabulary."""

  def _create_delivery_sdk(self):
    """Create a delivery using the SDK, returning a Delivery object."""
    req = self.create_request()
    quote = self.create_quote(req.id)
    return self.create_delivery(req.id, quote.id)

  def test_initial_event_is_created(self) -> None:
    """New delivery MUST start in 'created' state."""
    delivery = self._create_delivery_sdk()
    self.assertEqual(delivery.event, "created")
    self.assertEqual(delivery.event_description, "Delivery created")

  def test_event_can_transition_to_assigned(self) -> None:
    """Delivery CAN transition from created to assigned."""
    delivery = self._create_delivery_sdk()
    updated = self.update_event(
      delivery.id, "assigned", "Courier assigned"
    )
    self.assertEqual(updated.event, "assigned")

  def test_event_can_transition_to_enroute_pickup(self) -> None:
    """Delivery CAN transition to enroute_pickup."""
    delivery = self._create_delivery_sdk()
    updated = self.update_event(
      delivery.id, "enroute_pickup", "Courier heading to pickup"
    )
    self.assertEqual(updated.event, "enroute_pickup")

  def test_event_can_transition_to_arrived_pickup(self) -> None:
    """Delivery CAN transition to arrived_pickup."""
    delivery = self._create_delivery_sdk()
    updated = self.update_event(
      delivery.id, "arrived_pickup", "Courier at pickup location"
    )
    self.assertEqual(updated.event, "arrived_pickup")

  def test_event_can_transition_to_collected(self) -> None:
    """Delivery CAN transition to collected."""
    delivery = self._create_delivery_sdk()
    updated = self.update_event(
      delivery.id, "collected", "Courier picked up"
    )
    self.assertEqual(updated.event, "collected")

  def test_event_can_transition_to_arrived_dropoff(self) -> None:
    """Delivery CAN transition to arrived_dropoff."""
    delivery = self._create_delivery_sdk()
    updated = self.update_event(
      delivery.id, "arrived_dropoff", "Courier at dropoff location"
    )
    self.assertEqual(updated.event, "arrived_dropoff")

  def test_event_can_transition_to_delivered(self) -> None:
    """Delivery CAN transition to delivered."""
    delivery = self._create_delivery_sdk()
    updated = self.update_event(
      delivery.id, "delivered", "Courier completed dropoff"
    )
    self.assertEqual(updated.event, "delivered")

  def test_event_can_transition_to_canceled(self) -> None:
    """Delivery CAN transition to canceled."""
    delivery = self._create_delivery_sdk()
    updated = self.update_event(
      delivery.id, "canceled", "Delivery canceled"
    )
    self.assertEqual(updated.event, "canceled")

  def test_updated_at_changes_on_transition(self) -> None:
    """updated_at MUST change when event transitions."""
    delivery = self._create_delivery_sdk()
    original_updated_at = delivery.updated_at

    import time
    time.sleep(0.1)

    updated = self.update_event(
      delivery.id, "assigned", "Courier assigned"
    )
    self.assertNotEqual(
      updated.updated_at,
      original_updated_at,
      "updated_at should change on event transition",
    )

  def test_full_courier_lifecycle(self) -> None:
    """Courier delivery CAN follow full lifecycle sequence."""
    delivery = self._create_delivery_sdk()

    lifecycle = [
      ("assigned", "Courier assigned"),
      ("enroute_pickup", "Courier heading to pickup"),
      ("arrived_pickup", "Courier at pickup location"),
      ("collected", "Courier picked up"),
      ("arrived_dropoff", "Courier at dropoff location"),
      ("delivered", "Courier completed dropoff"),
    ]

    for event, description in lifecycle:
      updated = self.update_event(delivery.id, event, description)
      self.assertEqual(
        updated.event,
        event,
        f"Failed to transition to {event}",
      )

    # Verify final state
    final = self.sdk.deliveries.retrieve(delivery.id)
    self.assertEqual(final.event, "delivered")


if __name__ == "__main__":
  absltest.main()
