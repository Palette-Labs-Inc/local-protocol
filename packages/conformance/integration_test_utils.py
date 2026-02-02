"""Shared utilities for Local Protocol integration tests."""

import json
import logging
from pathlib import Path
import threading
import time
from typing import Any
import uuid

from absl import flags
from absl.testing import absltest
from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse
import httpx
import uvicorn


FLAGS = flags.FLAGS
try:
  flags.DEFINE_string("server_url", None, "Base URL of the server under test")
  flags.DEFINE_string(
    "simulation_secret",
    str(uuid.uuid4()),
    "Secret for simulation endpoints",
  )
  flags.DEFINE_integer(
    "mock_webhook_port", 8284, "Port for the mock webhook server"
  )
  flags.DEFINE_bool("verbose_http", False, "Whether to log HTTP requests.")
  flags.DEFINE_string(
    "conformance_input",
    "test_data/delivery/conformance_input.json",
    "Path to conformance input configuration JSON.",
  )
  flags.DEFINE_string(
    "test_data_dir",
    "test_data/delivery",
    "Directory containing test data.",
  )
except flags.DuplicateFlagError:
  pass


def get_headers(
  idempotency_key: str | None = None, request_id: str | None = None
) -> dict[str, str]:
  """Generate headers for Local Protocol requests.

  Args:
      idempotency_key: Optional specific idempotency key.
      request_id: Optional specific request ID.

  Returns:
      A dictionary of HTTP headers.

  """
  return {
    "Content-Type": "application/json",
    "idempotency-key": idempotency_key or str(uuid.uuid4()),
    "request-id": request_id or str(uuid.uuid4()),
  }


class MockWebhookServer:
  """A background mock webhook server that records incoming events."""

  def __init__(self, port: int):
    """Initialize the MockWebhookServer.

    Args:
      port: The port to listen on.

    """
    self.port = port
    self.app = FastAPI()
    self.events: list[dict[str, Any]] = []
    self._setup_routes()
    self._server: uvicorn.Server | None = None
    self._thread: threading.Thread | None = None

  def _setup_routes(self) -> None:
    """Set up the routes for the mock server."""

    @self.app.post("/webhooks/delivery/{delivery_id}/status")
    async def delivery_status(
      delivery_id: str, request: Request
    ) -> dict[str, str]:
      """Record an incoming delivery status event."""
      payload = await request.json()
      self.events.append({"delivery_id": delivery_id, "payload": payload})
      return {"status": "ok"}

    @self.app.get("/healthz")
    async def health_check() -> dict[str, str]:
      """Return a simple health check response."""
      return {"status": "ok"}

  def start(self) -> None:
    """Start the mock server in a background thread."""
    config = uvicorn.Config(
      self.app, host="0.0.0.0", port=self.port, log_level="error"
    )
    self._server = uvicorn.Server(config)
    self._thread = threading.Thread(target=self._server.run, daemon=True)
    self._thread.start()
    for _ in range(50):
      try:
        with httpx.Client() as client:
          if (
            client.get(f"http://localhost:{self.port}/healthz").status_code
            == 200
          ):
            break
      except httpx.ConnectError:
        time.sleep(0.1)
    else:
      raise RuntimeError(f"Server failed to start on port {self.port}")

  def stop(self) -> None:
    """Stop the mock server."""
    if self._server is not None:
      self._server.should_exit = True
      if self._thread is not None:
        self._thread.join(timeout=5)

  def clear_events(self) -> None:
    """Clear all recorded events."""
    self.events = []


class IntegrationTestBase(absltest.TestCase):
  """Base class for Local Protocol integration tests."""

  def setUp(self) -> None:
    """Set up the test case, including clients and mock servers."""
    super().setUp()
    if not FLAGS.server_url:
      self.fail(
        "Missing required flag: --server_url. "
        "Provide the base URL of the server under test, "
        "e.g., --server_url=http://localhost:8000"
      )
    self.base_url = FLAGS.server_url
    self.client = httpx.Client(base_url=self.base_url)

    httpx_logger = logging.getLogger("httpx")
    if FLAGS.verbose_http:
      httpx_logger.setLevel(logging.INFO)
    else:
      httpx_logger.setLevel(logging.WARNING)

    # Load conformance input configuration
    try:
      with Path(FLAGS.conformance_input).open() as f:
        self.conformance_config = json.load(f)
    except FileNotFoundError:
      logging.warning(
        "Conformance input file not found at %s. Using defaults.",
        FLAGS.conformance_input,
      )
      self.conformance_config = {}

  def tearDown(self) -> None:
    """Tear down the test case."""
    self.client.close()
    super().tearDown()

  def get_headers(
    self, idempotency_key: str | None = None, request_id: str | None = None
  ) -> dict[str, str]:
    """Generate headers for requests (instance method)."""
    return get_headers(idempotency_key, request_id)

  def assert_response_status(
    self, response: httpx.Response, expected_code: int | list[int]
  ) -> None:
    """Assert that the response status code matches expected.

    Args:
        response: The httpx response object.
        expected_code: An integer or list of valid status codes.

    Raises:
        AssertionError: If status code not in expected_code.

    """
    if isinstance(expected_code, int):
      expected_codes = [expected_code]
    else:
      expected_codes = expected_code

    self.assertIn(
      response.status_code,
      expected_codes,
      msg=(
        f"Expected status {expected_code}, got {response.status_code}."
        f" Response: {response.text}"
      ),
    )

  # -------------------------------------------------------------------------
  # Delivery-specific helpers
  # -------------------------------------------------------------------------

  def create_ask_payload(
    self,
    ask_id: str | None = None,
    pickup_lat: float = 37.7749,
    pickup_lng: float = -122.4194,
    dropoff_lat: float = 37.7849,
    dropoff_lng: float = -122.4094,
    pickup_time: str | None = None,
    dropoff_time: str | None = None,
  ) -> dict[str, Any]:
    """Create a valid delivery ask payload.

    Args:
        ask_id: Unique ask ID. Auto-generated if None.
        pickup_lat: Pickup latitude.
        pickup_lng: Pickup longitude.
        dropoff_lat: Dropoff latitude.
        dropoff_lng: Dropoff longitude.
        pickup_time: RFC3339 pickup time. Auto-generated if None.
        dropoff_time: RFC3339 dropoff time. Auto-generated if None.

    Returns:
        A dictionary representing a DeliveryAsk.

    """
    from datetime import datetime, timedelta, timezone

    now = datetime.now(timezone.utc)

    return {
      "id": ask_id or str(uuid.uuid4()),
      "pickup_location": {
        "coordinates": {"latitude": pickup_lat, "longitude": pickup_lng},
      },
      "dropoff_location": {
        "coordinates": {"latitude": dropoff_lat, "longitude": dropoff_lng},
      },
      "pickup_time": pickup_time
      or (now + timedelta(minutes=30)).isoformat(),
      "dropoff_time": dropoff_time
      or (now + timedelta(minutes=60)).isoformat(),
    }

  def create_bid_payload(
    self,
    bid_id: str | None = None,
    price: int = 1500,
    currency: str = "USD",
    pickup_lat: float = 37.7749,
    pickup_lng: float = -122.4194,
    dropoff_lat: float = 37.7849,
    dropoff_lng: float = -122.4094,
    pickup_estimate: str | None = None,
    dropoff_estimate: str | None = None,
  ) -> dict[str, Any]:
    """Create a valid delivery bid payload.

    Args:
        bid_id: Unique bid ID. Auto-generated if None.
        price: Price in minor currency units (e.g., cents).
        currency: ISO 4217 currency code.
        pickup_lat: Pickup latitude.
        pickup_lng: Pickup longitude.
        dropoff_lat: Dropoff latitude.
        dropoff_lng: Dropoff longitude.
        pickup_estimate: RFC3339 estimated pickup time.
        dropoff_estimate: RFC3339 estimated dropoff time.

    Returns:
        A dictionary representing a DeliveryBid.

    """
    from datetime import datetime, timedelta, timezone

    now = datetime.now(timezone.utc)

    return {
      "id": bid_id or str(uuid.uuid4()),
      "price": price,
      "currency": currency,
      "pickup_location": {
        "coordinates": {"latitude": pickup_lat, "longitude": pickup_lng},
      },
      "dropoff_location": {
        "coordinates": {"latitude": dropoff_lat, "longitude": dropoff_lng},
      },
      "pickup_estimate": pickup_estimate
      or (now + timedelta(minutes=25)).isoformat(),
      "dropoff_estimate": dropoff_estimate
      or (now + timedelta(minutes=55)).isoformat(),
    }

  def post_ask(
    self,
    ask_payload: dict[str, Any] | None = None,
    headers: dict[str, str] | None = None,
  ) -> httpx.Response:
    """Post a delivery ask to the server.

    Args:
        ask_payload: The ask payload. Uses default if None.
        headers: Optional headers to include.

    Returns:
        The httpx response.

    """
    if ask_payload is None:
      ask_payload = self.create_ask_payload()

    request_headers = self.get_headers()
    if headers:
      request_headers.update(headers)

    return self.client.post(
      "/asks",
      json=ask_payload,
      headers=request_headers,
    )

  def post_bid(
    self,
    ask_id: str,
    bid_payload: dict[str, Any] | None = None,
    headers: dict[str, str] | None = None,
  ) -> httpx.Response:
    """Post a delivery bid for an ask.

    Args:
        ask_id: The ask ID to bid on.
        bid_payload: The bid payload. Uses default if None.
        headers: Optional headers to include.

    Returns:
        The httpx response.

    """
    if bid_payload is None:
      bid_payload = self.create_bid_payload()

    request_headers = self.get_headers()
    if headers:
      request_headers.update(headers)

    return self.client.post(
      f"/asks/{ask_id}/bids",
      json=bid_payload,
      headers=request_headers,
    )
