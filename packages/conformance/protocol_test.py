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


class AskLifecycleTest(IntegrationTestBase):
  """Tests for delivery ask lifecycle."""

  def test_create_ask_returns_201(self) -> None:
    """Creating a valid ask MUST return 201."""
    ask_payload = self.create_ask_payload()
    response = self.post_ask(ask_payload)
    self.assert_response_status(response, [200, 201])
    data = response.json()
    self.assertEqual(data["id"], ask_payload["id"])

  def test_create_ask_missing_required_field_returns_4xx(self) -> None:
    """Creating an ask without required fields MUST return 4xx."""
    invalid_payload = {"id": "test-invalid"}  # Missing locations and times
    response = self.client.post(
      "/asks",
      json=invalid_payload,
      headers=self.get_headers(),
    )
    self.assertIn(response.status_code, [400, 422])

  def test_get_ask_by_id(self) -> None:
    """Server MUST allow fetching an ask by ID."""
    ask_payload = self.create_ask_payload()
    create_response = self.post_ask(ask_payload)
    self.assert_response_status(create_response, [200, 201])

    get_response = self.client.get(
      f"/asks/{ask_payload['id']}",
      headers=self.get_headers(),
    )
    self.assert_response_status(get_response, 200)
    data = get_response.json()
    self.assertEqual(data["id"], ask_payload["id"])

  def test_get_nonexistent_ask_returns_404(self) -> None:
    """Fetching a nonexistent ask MUST return 404."""
    response = self.client.get(
      "/asks/nonexistent-ask-id",
      headers=self.get_headers(),
    )
    self.assert_response_status(response, 404)


class BidLifecycleTest(IntegrationTestBase):
  """Tests for delivery bid lifecycle."""

  def test_create_bid_for_ask(self) -> None:
    """Creating a bid for a valid ask MUST succeed."""
    # First create an ask
    ask_payload = self.create_ask_payload()
    ask_response = self.post_ask(ask_payload)
    self.assert_response_status(ask_response, [200, 201])

    # Then create a bid
    bid_payload = self.create_bid_payload()
    bid_response = self.post_bid(ask_payload["id"], bid_payload)
    self.assert_response_status(bid_response, [200, 201])
    data = bid_response.json()
    self.assertEqual(data["id"], bid_payload["id"])

  def test_create_bid_for_nonexistent_ask_returns_404(self) -> None:
    """Creating a bid for nonexistent ask MUST return 404."""
    bid_payload = self.create_bid_payload()
    response = self.client.post(
      "/asks/nonexistent-ask-id/bids",
      json=bid_payload,
      headers=self.get_headers(),
    )
    self.assert_response_status(response, 404)

  def test_list_bids_for_ask(self) -> None:
    """Server MUST allow listing bids for an ask."""
    # Create ask
    ask_payload = self.create_ask_payload()
    ask_response = self.post_ask(ask_payload)
    self.assert_response_status(ask_response, [200, 201])
    ask_id = ask_response.json()["id"]

    # Create multiple bids
    for i in range(3):
      bid_payload = self.create_bid_payload(price=1000 + i * 100)
      self.post_bid(ask_id, bid_payload)

    # List bids
    response = self.client.get(
      f"/asks/{ask_id}/bids",
      headers=self.get_headers(),
    )
    self.assert_response_status(response, 200)
    data = response.json()
    self.assertIsInstance(data, list)
    self.assertGreaterEqual(len(data), 3)


class IdempotencyTest(IntegrationTestBase):
  """Tests for idempotency behavior."""

  def test_duplicate_ask_with_same_nonce(self) -> None:
    """Duplicate requests with same nonce MUST return same result."""
    ask_payload = self.create_ask_payload()
    # Use a fixed nonce for both requests
    ask_payload["nonce"] = "test-nonce-123"

    # First request
    response1 = self.post_ask(ask_payload)
    self.assert_response_status(response1, [200, 201])

    # Second request with same nonce
    response2 = self.post_ask(ask_payload)
    self.assert_response_status(response2, [200, 201])

    # Should return the same ask
    self.assertEqual(response1.json()["id"], response2.json()["id"])


if __name__ == "__main__":
  absltest.main()
