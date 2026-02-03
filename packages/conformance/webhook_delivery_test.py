"""Tests for webhook-based event delivery."""

import time

from absl import flags
from absl.testing import absltest

from integration_test_utils import IntegrationTestBase, MockWebhookServer

FLAGS = flags.FLAGS


class WebhookDeliveryTest(IntegrationTestBase):
  """Tests for webhook-based event delivery."""

  webhook_server: MockWebhookServer

  @classmethod
  def setUpClass(cls) -> None:
    """Set up the webhook server for all tests."""
    super().setUpClass()
    cls.webhook_server = MockWebhookServer(FLAGS.mock_webhook_port)
    cls.webhook_server.start()

  @classmethod
  def tearDownClass(cls) -> None:
    """Tear down the webhook server after all tests."""
    cls.webhook_server.stop()
    super().tearDownClass()

  def setUp(self) -> None:
    """Clear events before each test."""
    super().setUp()
    self.webhook_server.clear_events()

  def test_webhook_receives_event_on_transition(self) -> None:
    """Webhook MUST receive POST when delivery event changes."""
    delivery = self.create_delivery(webhook_url=self.webhook_server.url)

    # Update event
    response = self.update_delivery_event(
      delivery["id"],
      "assigned",
      "Courier assigned",
    )
    self.assert_response_status(response, 200)

    # Wait for background task
    time.sleep(0.5)

    events = self.webhook_server.get_events()
    self.assertEqual(len(events), 1, f"Expected 1 event, got {len(events)}")
    self.assertEqual(events[0]["event"], "assigned")

  def test_webhook_payload_has_required_fields(self) -> None:
    """Webhook payload MUST include required fields."""
    delivery = self.create_delivery(webhook_url=self.webhook_server.url)

    response = self.update_delivery_event(
      delivery["id"],
      "assigned",
      "Courier assigned",
    )
    self.assert_response_status(response, 200)

    # Wait for background task
    time.sleep(0.5)

    events = self.webhook_server.get_events()
    self.assertEqual(len(events), 1)

    required_fields = [
      "event_type",
      "delivery_id",
      "event",
      "event_description",
      "event_vocabulary",
      "updated_at",
    ]
    for field in required_fields:
      self.assertIn(field, events[0], f"Missing field: {field}")

  def test_webhook_payload_matches_delivery(self) -> None:
    """Webhook payload MUST match delivery object state."""
    delivery = self.create_delivery(webhook_url=self.webhook_server.url)

    response = self.update_delivery_event(
      delivery["id"],
      "enroute_pickup",
      "Courier heading to pickup",
    )
    self.assert_response_status(response, 200)
    updated_delivery = response.json()

    # Wait for background task
    time.sleep(0.5)

    events = self.webhook_server.get_events()
    self.assertEqual(len(events), 1)

    event = events[0]
    self.assertEqual(event["delivery_id"], updated_delivery["id"])
    self.assertEqual(event["event"], updated_delivery["event"])
    self.assertEqual(
      event["event_description"],
      updated_delivery["event_description"],
    )
    self.assertEqual(
      event["event_vocabulary"],
      updated_delivery["event_vocabulary"],
    )

  def test_webhook_event_type_is_delivery_event(self) -> None:
    """Webhook event_type MUST be 'delivery_event'."""
    delivery = self.create_delivery(webhook_url=self.webhook_server.url)

    response = self.update_delivery_event(
      delivery["id"],
      "assigned",
      "Courier assigned",
    )
    self.assert_response_status(response, 200)

    # Wait for background task
    time.sleep(0.5)

    events = self.webhook_server.get_events()
    self.assertEqual(len(events), 1)
    self.assertEqual(events[0]["event_type"], "delivery_event")

  def test_no_webhook_when_url_not_provided(self) -> None:
    """No webhook should be sent when webhook_url is not provided."""
    # Create delivery without webhook URL
    delivery = self.create_delivery(webhook_url=None)

    response = self.update_delivery_event(
      delivery["id"],
      "assigned",
      "Courier assigned",
    )
    self.assert_response_status(response, 200)

    # Wait for potential background task
    time.sleep(0.5)

    events = self.webhook_server.get_events()
    self.assertEqual(len(events), 0, "No webhook should be sent")

  def test_multiple_transitions_send_multiple_webhooks(self) -> None:
    """Multiple event transitions MUST send multiple webhooks."""
    delivery = self.create_delivery(webhook_url=self.webhook_server.url)

    # First transition
    response1 = self.update_delivery_event(
      delivery["id"],
      "assigned",
      "Courier assigned",
    )
    self.assert_response_status(response1, 200)

    # Second transition
    response2 = self.update_delivery_event(
      delivery["id"],
      "delivered",
      "Courier completed dropoff",
    )
    self.assert_response_status(response2, 200)

    # Wait for background tasks
    time.sleep(0.5)

    events = self.webhook_server.get_events()
    self.assertEqual(len(events), 2, f"Expected 2 events, got {len(events)}")
    self.assertEqual(events[0]["event"], "assigned")
    self.assertEqual(events[1]["event"], "delivered")


if __name__ == "__main__":
  absltest.main()
