"""Schema validation conformance tests for Local Protocol servers."""

from absl.testing import absltest

from integration_test_utils import IntegrationTestBase


class RequestValidationTest(IntegrationTestBase):
  """Tests for request payload validation."""

  def test_request_requires_pickup_location(self) -> None:
    """Request without pickup_location MUST be rejected."""
    payload = self.create_request_payload()
    del payload["pickup_location"]

    response = self.client.post(
      "/requests",
      json=payload,
      headers=self.get_headers(),
    )
    self.assertIn(response.status_code, [400, 422])

  def test_request_requires_dropoff_location(self) -> None:
    """Request without dropoff_location MUST be rejected."""
    payload = self.create_request_payload()
    del payload["dropoff_location"]

    response = self.client.post(
      "/requests",
      json=payload,
      headers=self.get_headers(),
    )
    self.assertIn(response.status_code, [400, 422])

  def test_request_requires_pickup_time(self) -> None:
    """Request without pickup_time MUST be rejected."""
    payload = self.create_request_payload()
    del payload["pickup_time"]

    response = self.client.post(
      "/requests",
      json=payload,
      headers=self.get_headers(),
    )
    self.assertIn(response.status_code, [400, 422])

  def test_request_requires_dropoff_time(self) -> None:
    """Request without dropoff_time MUST be rejected."""
    payload = self.create_request_payload()
    del payload["dropoff_time"]

    response = self.client.post(
      "/requests",
      json=payload,
      headers=self.get_headers(),
    )
    self.assertIn(response.status_code, [400, 422])

  def test_request_invalid_time_format_rejected(self) -> None:
    """Request with invalid time format MUST be rejected."""
    payload = self.create_request_payload()
    payload["pickup_time"] = "not-a-valid-datetime"

    response = self.client.post(
      "/requests",
      json=payload,
      headers=self.get_headers(),
    )
    self.assertIn(response.status_code, [400, 422])


class QuoteValidationTest(IntegrationTestBase):
  """Tests for quote payload validation."""

  def test_quote_requires_price(self) -> None:
    """Quote without price MUST be rejected."""
    # Create request first
    request_payload = self.create_request_payload()
    self.post_request(request_payload)

    quote_payload = self.create_quote_payload()
    del quote_payload["price"]

    response = self.client.post(
      f"/requests/{request_payload['id']}/quotes",
      json=quote_payload,
      headers=self.get_headers(),
    )
    self.assertIn(response.status_code, [400, 422])

  def test_quote_requires_currency(self) -> None:
    """Quote without currency MUST be rejected."""
    request_payload = self.create_request_payload()
    self.post_request(request_payload)

    quote_payload = self.create_quote_payload()
    del quote_payload["currency"]

    response = self.client.post(
      f"/requests/{request_payload['id']}/quotes",
      json=quote_payload,
      headers=self.get_headers(),
    )
    self.assertIn(response.status_code, [400, 422])

  def test_quote_invalid_currency_format_rejected(self) -> None:
    """Quote with invalid currency code MUST be rejected."""
    request_payload = self.create_request_payload()
    self.post_request(request_payload)

    quote_payload = self.create_quote_payload()
    quote_payload["currency"] = "invalid"  # Not ISO 4217

    response = self.client.post(
      f"/requests/{request_payload['id']}/quotes",
      json=quote_payload,
      headers=self.get_headers(),
    )
    self.assertIn(response.status_code, [400, 422])

  def test_quote_negative_price_rejected(self) -> None:
    """Quote with negative price MUST be rejected."""
    request_payload = self.create_request_payload()
    self.post_request(request_payload)

    quote_payload = self.create_quote_payload()
    quote_payload["price"] = -100

    response = self.client.post(
      f"/requests/{request_payload['id']}/quotes",
      json=quote_payload,
      headers=self.get_headers(),
    )
    self.assertIn(response.status_code, [400, 422])


if __name__ == "__main__":
  absltest.main()
