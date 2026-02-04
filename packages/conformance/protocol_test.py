"""Basic protocol conformance tests for Local Protocol servers."""

from absl.testing import absltest

from integration_test_utils import IntegrationTestBase


class DiscoveryTest(IntegrationTestBase):
  """Tests for service discovery endpoints."""

  def test_well_known_endpoint_exists(self) -> None:
    """Server MUST expose /.well-known/local-protocol."""
    response = self.client.get(
      "/.well-known/local-protocol",
      headers=self.get_headers(),
    )
    self.assert_response_status(response, 200)
    data = response.json()
    self.assertIn("version", data)

  def test_health_check(self) -> None:
    """Server SHOULD expose /healthz endpoint."""
    response = self.client.get("/healthz")
    self.assert_response_status(response, 200)


class RequestLifecycleTest(IntegrationTestBase):
  """Tests for delivery request lifecycle."""

  def test_create_request_returns_201(self) -> None:
    """Creating a valid request MUST return 201."""
    request_payload = self.create_request_payload()
    response = self.post_request(request_payload)
    self.assert_response_status(response, [200, 201])
    data = response.json()
    self.assertEqual(data["id"], request_payload["id"])

  def test_create_request_missing_required_field_returns_4xx(self) -> None:
    """Creating a request without required fields MUST return 4xx."""
    invalid_payload = {"id": "test-invalid"}  # Missing locations and times
    response = self.client.post(
      "/requests",
      json=invalid_payload,
      headers=self.get_headers(),
    )
    self.assertIn(response.status_code, [400, 422])

  def test_get_request_by_id(self) -> None:
    """Server MUST allow fetching a request by ID."""
    request_payload = self.create_request_payload()
    create_response = self.post_request(request_payload)
    self.assert_response_status(create_response, [200, 201])

    get_response = self.client.get(
      f"/requests/{request_payload['id']}",
      headers=self.get_headers(),
    )
    self.assert_response_status(get_response, 200)
    data = get_response.json()
    self.assertEqual(data["id"], request_payload["id"])

  def test_get_nonexistent_request_returns_404(self) -> None:
    """Fetching a nonexistent request MUST return 404."""
    response = self.client.get(
      "/requests/nonexistent-request-id",
      headers=self.get_headers(),
    )
    self.assert_response_status(response, 404)


class QuoteLifecycleTest(IntegrationTestBase):
  """Tests for delivery quote lifecycle."""

  def test_create_quote_for_request(self) -> None:
    """Creating a quote for a valid request MUST succeed."""
    # First create a request
    request_payload = self.create_request_payload()
    request_response = self.post_request(request_payload)
    self.assert_response_status(request_response, [200, 201])

    # Then create a quote
    quote_payload = self.create_quote_payload()
    quote_response = self.post_quote(request_payload["id"], quote_payload)
    self.assert_response_status(quote_response, [200, 201])
    data = quote_response.json()
    self.assertEqual(data["id"], quote_payload["id"])

  def test_create_quote_for_nonexistent_request_returns_404(self) -> None:
    """Creating a quote for nonexistent request MUST return 404."""
    quote_payload = self.create_quote_payload()
    response = self.client.post(
      "/requests/nonexistent-request-id/quotes",
      json=quote_payload,
      headers=self.get_headers(),
    )
    self.assert_response_status(response, 404)

  def test_list_quotes_for_request(self) -> None:
    """Server MUST allow listing quotes for a request."""
    # Create request
    request_payload = self.create_request_payload()
    request_response = self.post_request(request_payload)
    self.assert_response_status(request_response, [200, 201])
    request_id = request_response.json()["id"]

    # Create multiple quotes
    for i in range(3):
      quote_payload = self.create_quote_payload(price=1000 + i * 100)
      self.post_quote(request_id, quote_payload)

    # List quotes
    response = self.client.get(
      f"/requests/{request_id}/quotes",
      headers=self.get_headers(),
    )
    self.assert_response_status(response, 200)
    data = response.json()
    self.assertIsInstance(data, list)
    self.assertGreaterEqual(len(data), 3)


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
