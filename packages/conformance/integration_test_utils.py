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
import httpx
from local_protocol import LocalProtocol
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
  flags.DEFINE_string(
    "standards_dir",
    "test_data/standards",
    "Directory containing standard definition fixtures.",
  )
  flags.DEFINE_string(
    "schema_dir",
    None,
    "Directory containing JSON schemas for validation.",
  )
except flags.DuplicateFlagError:
  pass


def load_standard(name: str) -> dict[str, Any]:
  """Load a standard definition from the test fixtures."""
  standards_path = Path(FLAGS.standards_dir)
  standard_file = standards_path / f"{name}.json"
  with standard_file.open() as f:
    return json.load(f)


def load_schema(schema_path: str) -> dict[str, Any]:
  """Load a JSON schema from the schemas directory."""
  if FLAGS.schema_dir is None:
    raise ValueError(
      "--schema_dir flag must be set for schema validation tests"
    )
  schema_file = Path(FLAGS.schema_dir) / schema_path
  with schema_file.open() as f:
    return json.load(f)


def get_headers(request_id: str | None = None) -> dict[str, str]:
  """Generate headers for Local Protocol requests."""
  return {
    "Content-Type": "application/json",
    "request-id": request_id or str(uuid.uuid4()),
  }


class MockWebhookServer:
  """A background mock webhook server that records incoming events."""

  def __init__(self, port: int):
    self.port = port
    self.app = FastAPI()
    self.events: list[dict[str, Any]] = []
    self._setup_routes()
    self._server: uvicorn.Server | None = None
    self._thread: threading.Thread | None = None

  @property
  def url(self) -> str:
    """Return the base URL of the webhook server."""
    return f"http://localhost:{self.port}/webhook"

  def _setup_routes(self) -> None:
    @self.app.post("/webhook")
    async def webhook_receiver(request: Request) -> dict[str, str]:
      payload = await request.json()
      self.events.append(payload)
      return {"status": "ok"}

    @self.app.post("/webhooks/delivery/{delivery_id}/status")
    async def delivery_status(
      delivery_id: str, request: Request
    ) -> dict[str, str]:
      payload = await request.json()
      self.events.append({"delivery_id": delivery_id, "payload": payload})
      return {"status": "ok"}

    @self.app.get("/healthz")
    async def health_check() -> dict[str, str]:
      return {"status": "ok"}

  def get_events(self) -> list[dict[str, Any]]:
    return self.events.copy()

  def start(self) -> None:
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
    if self._server is not None:
      self._server.should_exit = True
      if self._thread is not None:
        self._thread.join(timeout=5)

  def clear_events(self) -> None:
    self.events = []


class IntegrationTestBase(absltest.TestCase):
  """Base class for Local Protocol integration tests."""

  def setUp(self) -> None:
    super().setUp()
    if not FLAGS.server_url:
      self.fail(
        "Missing required flag: --server_url. "
        "Provide the base URL of the server under test, "
        "e.g., --server_url=http://localhost:8000"
      )
    self.base_url = FLAGS.server_url

    # SDK client for happy-path tests
    self.sdk = LocalProtocol(base_url=self.base_url, api_key="test")

    # Raw httpx client for error-path tests (invalid payloads, 404s)
    self.http_client = httpx.Client(base_url=self.base_url)

    # Backward-compat alias used by discovery/validation tests
    self.client = self.http_client

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
    self.sdk.close()
    self.http_client.close()
    super().tearDown()

  def get_headers(self, request_id: str | None = None) -> dict[str, str]:
    return get_headers(request_id)

  def load_standard(self, name: str) -> dict[str, Any]:
    return load_standard(name)

  def load_schema(self, schema_path: str) -> dict[str, Any]:
    return load_schema(schema_path)

  def assert_response_status(
    self, response: httpx.Response, expected_code: int | list[int]
  ) -> None:
    """Assert that the response status code matches expected."""
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
  # SDK-based helpers (return typed SDK objects)
  # -------------------------------------------------------------------------

  def create_request(
    self,
    request_id: str | None = None,
    pickup_lat: float = 37.7749,
    pickup_lng: float = -122.4194,
    dropoff_lat: float = 37.7849,
    dropoff_lng: float = -122.4094,
    pickup_time: str | None = None,
    dropoff_time: str | None = None,
  ):
    """Create a delivery request via SDK."""
    from datetime import datetime, timedelta, timezone

    now = datetime.now(timezone.utc)

    return self.sdk.requests.create(
      id=request_id or str(uuid.uuid4()),
      nonce=str(uuid.uuid4()),
      pickup_location={
        "coordinates": {"latitude": pickup_lat, "longitude": pickup_lng},
      },
      dropoff_location={
        "coordinates": {"latitude": dropoff_lat, "longitude": dropoff_lng},
      },
      pickup_time=pickup_time or (now + timedelta(minutes=30)).isoformat(),
      dropoff_time=dropoff_time or (now + timedelta(minutes=60)).isoformat(),
    )

  def create_quote(
    self,
    request_id: str,
    quote_id: str | None = None,
    price: int = 1500,
    currency: str = "USD",
    pickup_lat: float = 37.7749,
    pickup_lng: float = -122.4194,
    dropoff_lat: float = 37.7849,
    dropoff_lng: float = -122.4094,
    pickup_estimate: str | None = None,
    dropoff_estimate: str | None = None,
  ):
    """Create a quote for a request via SDK."""
    from datetime import datetime, timedelta, timezone

    now = datetime.now(timezone.utc)

    return self.sdk.requests.quotes.create(
      request_id,
      id=quote_id or str(uuid.uuid4()),
      nonce=str(uuid.uuid4()),
      price=price,
      currency=currency,
      payment={},
      pickup_location={
        "coordinates": {"latitude": pickup_lat, "longitude": pickup_lng},
      },
      dropoff_location={
        "coordinates": {"latitude": dropoff_lat, "longitude": dropoff_lng},
      },
      pickup_estimate=pickup_estimate
      or (now + timedelta(minutes=25)).isoformat(),
      dropoff_estimate=dropoff_estimate
      or (now + timedelta(minutes=55)).isoformat(),
    )

  def create_delivery(
    self,
    request_id: str,
    quote_id: str,
    webhook_url: str | None = None,
  ):
    """Create a delivery via SDK."""
    kwargs: dict[str, Any] = {
      "nonce": str(uuid.uuid4()),
      "request_id": request_id,
      "quote_id": quote_id,
    }
    if webhook_url is not None:
      kwargs["webhook_url"] = webhook_url
    return self.sdk.deliveries.create(**kwargs)

  def update_event(
    self,
    delivery_id: str,
    event: str,
    event_description: str | None = None,
  ):
    """Update a delivery event via SDK."""
    if event_description is None:
      event_description = f"Event changed to {event}"
    return self.sdk.deliveries.update_event(
      delivery_id,
      event=event,
      event_description=event_description,
    )

  # -------------------------------------------------------------------------
  # Raw-payload helpers (for error-path and backward-compat tests)
  # -------------------------------------------------------------------------

  def create_request_payload(
    self,
    request_id: str | None = None,
    pickup_lat: float = 37.7749,
    pickup_lng: float = -122.4194,
    dropoff_lat: float = 37.7849,
    dropoff_lng: float = -122.4094,
    pickup_time: str | None = None,
    dropoff_time: str | None = None,
  ) -> dict[str, Any]:
    """Create a valid delivery request payload dict."""
    from datetime import datetime, timedelta, timezone

    now = datetime.now(timezone.utc)

    return {
      "id": request_id or str(uuid.uuid4()),
      "nonce": str(uuid.uuid4()),
      "pickup_location": {
        "coordinates": {"latitude": pickup_lat, "longitude": pickup_lng},
      },
      "dropoff_location": {
        "coordinates": {"latitude": dropoff_lat, "longitude": dropoff_lng},
      },
      "pickup_time": pickup_time or (now + timedelta(minutes=30)).isoformat(),
      "dropoff_time": dropoff_time or (now + timedelta(minutes=60)).isoformat(),
    }

  def create_quote_payload(
    self,
    quote_id: str | None = None,
    price: int = 1500,
    currency: str = "USD",
    pickup_lat: float = 37.7749,
    pickup_lng: float = -122.4194,
    dropoff_lat: float = 37.7849,
    dropoff_lng: float = -122.4094,
    pickup_estimate: str | None = None,
    dropoff_estimate: str | None = None,
  ) -> dict[str, Any]:
    """Create a valid delivery quote payload dict."""
    from datetime import datetime, timedelta, timezone

    now = datetime.now(timezone.utc)

    return {
      "id": quote_id or str(uuid.uuid4()),
      "nonce": str(uuid.uuid4()),
      "price": price,
      "currency": currency,
      "payment": {},
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

  def post_request(
    self,
    request_payload: dict[str, Any] | None = None,
    headers: dict[str, str] | None = None,
  ) -> httpx.Response:
    """Post a delivery request via raw httpx."""
    if request_payload is None:
      request_payload = self.create_request_payload()

    request_headers = self.get_headers()
    if headers:
      request_headers.update(headers)

    return self.http_client.post(
      "/requests",
      json=request_payload,
      headers=request_headers,
    )

  def post_quote(
    self,
    request_id: str,
    quote_payload: dict[str, Any] | None = None,
    headers: dict[str, str] | None = None,
  ) -> httpx.Response:
    """Post a delivery quote via raw httpx."""
    if quote_payload is None:
      quote_payload = self.create_quote_payload()

    request_headers = self.get_headers()
    if headers:
      request_headers.update(headers)

    return self.http_client.post(
      f"/requests/{request_id}/quotes",
      json=quote_payload,
      headers=request_headers,
    )

  def create_delivery_payload(
    self,
    request_id: str,
    quote_id: str,
    webhook_url: str | None = None,
    event_vocabulary: str = "xyz.localprotocol.delivery.courier@2026-01-30",
  ) -> dict[str, Any]:
    """Create a valid delivery creation payload dict."""
    payload: dict[str, Any] = {
      "request_id": request_id,
      "quote_id": quote_id,
      "nonce": str(uuid.uuid4()),
      "event_vocabulary": event_vocabulary,
    }
    if webhook_url:
      payload["webhook_url"] = webhook_url
    return payload

  def post_delivery(
    self,
    request_id: str,
    quote_id: str,
    webhook_url: str | None = None,
    headers: dict[str, str] | None = None,
  ) -> httpx.Response:
    """Create a delivery via raw httpx."""
    payload = self.create_delivery_payload(request_id, quote_id, webhook_url)

    request_headers = self.get_headers()
    if headers:
      request_headers.update(headers)

    return self.http_client.post(
      "/deliveries",
      json=payload,
      headers=request_headers,
    )

  # -------------------------------------------------------------------------
  # Full-flow helper (returns dict for backward compat with webhook tests)
  # -------------------------------------------------------------------------

  def create_full_delivery(
    self,
    webhook_url: str | None = None,
  ) -> dict[str, Any]:
    """Create a request, quote, and delivery via SDK (full flow).

    Returns a dict for backward compatibility with webhook/dict-access tests.
    """
    req = self.create_request()
    quote = self.create_quote(req.id)
    delivery = self.create_delivery(req.id, quote.id, webhook_url)
    return delivery.model_dump(mode="json")

  def update_delivery_event(
    self,
    delivery_id: str,
    event: str,
    event_description: str | None = None,
  ) -> httpx.Response:
    """Update a delivery event via raw httpx (for response-level assertions)."""
    if event_description is None:
      event_description = f"Event changed to {event}"

    return self.http_client.patch(
      f"/deliveries/{delivery_id}/event",
      json={"event": event, "event_description": event_description},
    )
