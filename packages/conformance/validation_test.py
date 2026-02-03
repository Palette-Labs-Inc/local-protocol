"""Schema validation conformance tests for Local Protocol servers."""

from absl.testing import absltest

from integration_test_utils import IntegrationTestBase


class AskValidationTest(IntegrationTestBase):
  """Tests for ask payload validation."""

  def test_ask_requires_pickup_location(self) -> None:
    """Ask without pickup_location MUST be rejected."""
    payload = self.create_ask_payload()
    del payload["pickup_location"]

    response = self.client.post(
      "/asks",
      json=payload,
      headers=self.get_headers(),
    )
    self.assertIn(response.status_code, [400, 422])

  def test_ask_requires_dropoff_location(self) -> None:
    """Ask without dropoff_location MUST be rejected."""
    payload = self.create_ask_payload()
    del payload["dropoff_location"]

    response = self.client.post(
      "/asks",
      json=payload,
      headers=self.get_headers(),
    )
    self.assertIn(response.status_code, [400, 422])

  def test_ask_requires_pickup_time(self) -> None:
    """Ask without pickup_time MUST be rejected."""
    payload = self.create_ask_payload()
    del payload["pickup_time"]

    response = self.client.post(
      "/asks",
      json=payload,
      headers=self.get_headers(),
    )
    self.assertIn(response.status_code, [400, 422])

  def test_ask_requires_dropoff_time(self) -> None:
    """Ask without dropoff_time MUST be rejected."""
    payload = self.create_ask_payload()
    del payload["dropoff_time"]

    response = self.client.post(
      "/asks",
      json=payload,
      headers=self.get_headers(),
    )
    self.assertIn(response.status_code, [400, 422])

  def test_ask_invalid_time_format_rejected(self) -> None:
    """Ask with invalid time format MUST be rejected."""
    payload = self.create_ask_payload()
    payload["pickup_time"] = "not-a-valid-datetime"

    response = self.client.post(
      "/asks",
      json=payload,
      headers=self.get_headers(),
    )
    self.assertIn(response.status_code, [400, 422])


class BidValidationTest(IntegrationTestBase):
  """Tests for bid payload validation."""

  def test_bid_requires_price(self) -> None:
    """Bid without price MUST be rejected."""
    # Create ask first
    ask_payload = self.create_ask_payload()
    self.post_ask(ask_payload)

    bid_payload = self.create_bid_payload()
    del bid_payload["price"]

    response = self.client.post(
      f"/asks/{ask_payload['id']}/bids",
      json=bid_payload,
      headers=self.get_headers(),
    )
    self.assertIn(response.status_code, [400, 422])

  def test_bid_requires_currency(self) -> None:
    """Bid without currency MUST be rejected."""
    ask_payload = self.create_ask_payload()
    self.post_ask(ask_payload)

    bid_payload = self.create_bid_payload()
    del bid_payload["currency"]

    response = self.client.post(
      f"/asks/{ask_payload['id']}/bids",
      json=bid_payload,
      headers=self.get_headers(),
    )
    self.assertIn(response.status_code, [400, 422])

  def test_bid_invalid_currency_format_rejected(self) -> None:
    """Bid with invalid currency code MUST be rejected."""
    ask_payload = self.create_ask_payload()
    self.post_ask(ask_payload)

    bid_payload = self.create_bid_payload()
    bid_payload["currency"] = "invalid"  # Not ISO 4217

    response = self.client.post(
      f"/asks/{ask_payload['id']}/bids",
      json=bid_payload,
      headers=self.get_headers(),
    )
    self.assertIn(response.status_code, [400, 422])

  def test_bid_negative_price_rejected(self) -> None:
    """Bid with negative price MUST be rejected."""
    ask_payload = self.create_ask_payload()
    self.post_ask(ask_payload)

    bid_payload = self.create_bid_payload()
    bid_payload["price"] = -100

    response = self.client.post(
      f"/asks/{ask_payload['id']}/bids",
      json=bid_payload,
      headers=self.get_headers(),
    )
    self.assertIn(response.status_code, [400, 422])


if __name__ == "__main__":
  absltest.main()
