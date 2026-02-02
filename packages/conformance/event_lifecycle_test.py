"""Tests for delivery event state transitions."""

from datetime import datetime

from absl.testing import absltest

from integration_test_utils import IntegrationTestBase


class EventLifecycleTest(IntegrationTestBase):
  """Tests for delivery event state transitions."""

  def test_initial_event_is_pending(self) -> None:
    """New delivery MUST start in 'pending' state."""
    delivery = self.create_delivery()
    self.assertEqual(delivery["event"], "pending")
    self.assertEqual(
      delivery["event_description"],
      "Job accepted, work not started",
    )

  def test_event_can_transition_to_active(self) -> None:
    """Delivery CAN transition from pending to active."""
    delivery = self.create_delivery()
    response = self.update_delivery_event(
      delivery["id"],
      "active",
      "Work in progress",
    )
    self.assert_response_status(response, 200)
    updated = response.json()
    self.assertEqual(updated["event"], "active")

  def test_event_can_transition_to_completed(self) -> None:
    """Delivery CAN transition to completed."""
    delivery = self.create_delivery()
    response = self.update_delivery_event(
      delivery["id"],
      "completed",
      "Successfully finished",
    )
    self.assert_response_status(response, 200)
    updated = response.json()
    self.assertEqual(updated["event"], "completed")

  def test_event_can_transition_to_failed(self) -> None:
    """Delivery CAN transition to failed."""
    delivery = self.create_delivery()
    response = self.update_delivery_event(
      delivery["id"],
      "failed",
      "Unsuccessfully finished",
    )
    self.assert_response_status(response, 200)
    updated = response.json()
    self.assertEqual(updated["event"], "failed")

  def test_updated_at_changes_on_transition(self) -> None:
    """updated_at MUST change when event transitions."""
    delivery = self.create_delivery()
    original_updated_at = delivery["updated_at"]

    # Small delay to ensure timestamp changes
    import time
    time.sleep(0.1)

    response = self.update_delivery_event(
      delivery["id"],
      "active",
      "Work in progress",
    )
    self.assert_response_status(response, 200)
    updated = response.json()

    self.assertNotEqual(
      updated["updated_at"],
      original_updated_at,
      "updated_at should change on event transition",
    )

  def test_food_delivery_order_placed(self) -> None:
    """Food delivery CAN transition to order_placed."""
    delivery = self.create_delivery()
    response = self.update_delivery_event(
      delivery["id"],
      "order_placed",
      "Order has been placed with the merchant",
    )
    self.assert_response_status(response, 200)
    updated = response.json()
    self.assertEqual(updated["event"], "order_placed")

  def test_food_delivery_preparing(self) -> None:
    """Food delivery CAN transition to preparing."""
    delivery = self.create_delivery()
    response = self.update_delivery_event(
      delivery["id"],
      "preparing",
      "Merchant is preparing the order",
    )
    self.assert_response_status(response, 200)
    updated = response.json()
    self.assertEqual(updated["event"], "preparing")

  def test_food_delivery_courier_assigned(self) -> None:
    """Food delivery CAN transition to courier_assigned."""
    delivery = self.create_delivery()
    response = self.update_delivery_event(
      delivery["id"],
      "courier_assigned",
      "Courier has been assigned to the delivery",
    )
    self.assert_response_status(response, 200)
    updated = response.json()
    self.assertEqual(updated["event"], "courier_assigned")

  def test_food_delivery_in_transit(self) -> None:
    """Food delivery CAN transition to in_transit."""
    delivery = self.create_delivery()
    response = self.update_delivery_event(
      delivery["id"],
      "in_transit",
      "Order is in transit to delivery location",
    )
    self.assert_response_status(response, 200)
    updated = response.json()
    self.assertEqual(updated["event"], "in_transit")

  def test_food_delivery_delivered(self) -> None:
    """Food delivery CAN transition to delivered."""
    delivery = self.create_delivery()
    response = self.update_delivery_event(
      delivery["id"],
      "delivered",
      "Order has been delivered to recipient",
    )
    self.assert_response_status(response, 200)
    updated = response.json()
    self.assertEqual(updated["event"], "delivered")

  def test_food_delivery_canceled(self) -> None:
    """Food delivery CAN transition to canceled."""
    delivery = self.create_delivery()
    response = self.update_delivery_event(
      delivery["id"],
      "canceled",
      "Order has been canceled",
    )
    self.assert_response_status(response, 200)
    updated = response.json()
    self.assertEqual(updated["event"], "canceled")

  def test_full_food_lifecycle(self) -> None:
    """Food delivery CAN follow full lifecycle sequence."""
    delivery = self.create_delivery()

    # Full food delivery lifecycle
    lifecycle = [
      ("order_placed", "Order has been placed with the merchant"),
      ("preparing", "Merchant is preparing the order"),
      ("ready_for_pickup", "Order is ready for courier pickup"),
      ("courier_assigned", "Courier has been assigned to the delivery"),
      ("courier_at_pickup", "Courier has arrived at the pickup location"),
      ("picked_up", "Order has been picked up by courier"),
      ("in_transit", "Order is in transit to delivery location"),
      ("courier_at_dropoff", "Courier has arrived at the delivery location"),
      ("delivered", "Order has been delivered to recipient"),
      ("completed", "Successfully finished"),
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
    self.assertEqual(final["event"], "completed")


if __name__ == "__main__":
  absltest.main()
