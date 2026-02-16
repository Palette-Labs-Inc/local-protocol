"""Basic protocol conformance tests for Local Protocol servers."""

from absl.testing import absltest

from integration_test_utils import IntegrationTestBase


class DiscoveryTest(IntegrationTestBase):
  """Tests for service discovery endpoints."""

  def test_ucp_well_known_endpoint_exists(self) -> None:
    """Server MUST expose /.well-known/ucp."""
    response = self.http_client.get("/.well-known/ucp")
    self.assert_response_status(response, 200)
    data = response.json()
    self.assertIn("ucp", data)
    self.assertIsNotNone(data["ucp"].get("version"))

  def test_health_check(self) -> None:
    """Server SHOULD expose /healthz endpoint."""
    data = self.sdk.healthz.check()
    self.assertEqual(data.status, "ok")


class RequestLifecycleTest(IntegrationTestBase):
  """Tests for delivery request lifecycle."""

  def test_create_request_returns_201(self) -> None:
    """Creating a valid request MUST return 201."""
    req = self.create_request()
    self.assertIsNotNone(req.id)

  def test_create_request_missing_required_field_returns_4xx(self) -> None:
    """Creating a request without required fields MUST return 4xx."""
    invalid_payload = {"id": "test-invalid"}  # Missing locations and times
    response = self.http_client.post(
      "/requests",
      json=invalid_payload,
      headers=self.get_headers(),
    )
    self.assertIn(response.status_code, [400, 422])

  def test_get_request_by_id(self) -> None:
    """Server MUST allow fetching a request by ID."""
    created = self.create_request()
    fetched = self.sdk.requests.retrieve(created.id)
    self.assertEqual(fetched.id, created.id)

  def test_get_nonexistent_request_returns_404(self) -> None:
    """Fetching a nonexistent request MUST return 404."""
    response = self.http_client.get(
      "/requests/nonexistent-request-id",
      headers=self.get_headers(),
    )
    self.assert_response_status(response, 404)


class QuoteLifecycleTest(IntegrationTestBase):
  """Tests for delivery quote lifecycle."""

  def test_create_quote_for_request(self) -> None:
    """Creating a quote for a valid request MUST succeed."""
    req = self.create_request()
    quote = self.create_quote(req.id)
    self.assertIsNotNone(quote.id)

  def test_create_quote_for_nonexistent_request_returns_404(self) -> None:
    """Creating a quote for nonexistent request MUST return 404."""
    quote_payload = self.create_quote_payload()
    response = self.http_client.post(
      "/requests/nonexistent-request-id/quotes",
      json=quote_payload,
      headers=self.get_headers(),
    )
    self.assert_response_status(response, 404)

  def test_list_quotes_for_request(self) -> None:
    """Server MUST allow listing quotes for a request."""
    req = self.create_request()

    # Create multiple quotes
    for i in range(3):
      self.create_quote(req.id, price=1000 + i * 100)

    # List quotes
    quotes = self.sdk.requests.quotes.list(req.id)
    self.assertGreaterEqual(len(quotes), 3)


class IdempotencyTest(IntegrationTestBase):
  """Tests for idempotency behavior."""

  def test_duplicate_request_with_same_nonce(self) -> None:
    """Duplicate requests with same nonce MUST return same result."""
    request_payload = self.create_request_payload()
    # Use a fixed nonce for both requests
    request_payload["nonce"] = "test-nonce-123"

    # First request
    response1 = self.post_request(request_payload)
    self.assert_response_status(response1, [200, 201])

    # Second request with same nonce
    response2 = self.post_request(request_payload)
    self.assert_response_status(response2, [200, 201])

    # Should return the same request
    self.assertEqual(response1.json()["id"], response2.json()["id"])


if __name__ == "__main__":
  absltest.main()
