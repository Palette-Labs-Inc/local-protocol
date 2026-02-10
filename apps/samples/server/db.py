"""In-memory database for sample server."""

import copy
import threading
from datetime import datetime, timezone
from typing import Any


# Sentinel for in-progress idempotency claims. Using a unique object instance
# allows distinguishing "request in progress" from "no cached response" (None).
_PENDING = object()


def validate_nonce(nonce: str | None) -> str:
  """Validate and normalize a nonce value.

  Args:
      nonce: The nonce to validate.

  Returns:
      The trimmed nonce.

  Raises:
      ValueError: If nonce is missing or empty after trimming.

  """
  trimmed = nonce.strip() if nonce else ""
  if not trimmed:
    raise ValueError("nonce is required and cannot be empty")
  return trimmed


class Database:
  """Simple in-memory database for requests, quotes, and deliveries."""

  def __init__(self) -> None:
    self.requests: dict[str, dict[str, Any]] = {}
    self.quotes: dict[str, dict[str, Any]] = {}  # quote_id -> quote
    self.request_quotes: dict[str, list[str]] = {}  # request_id -> [quote_ids]
    self.deliveries: dict[str, dict[str, Any]] = {}  # delivery_id -> delivery
    self.idempotency_cache: dict[str, dict[str, Any] | object] = {}
    # Lock prevents race conditions where concurrent requests with the same nonce
    # could both pass the "not in cache" check before either sets _PENDING.
    self._idempotency_lock = threading.Lock()

  def create_request(self, request: dict[str, Any]) -> dict[str, Any]:
    """Create a new request."""
    request_id = request["id"]
    request["created_at"] = datetime.now(timezone.utc).isoformat()
    request["status"] = "open"
    self.requests[request_id] = request
    self.request_quotes[request_id] = []
    return request

  def get_request(self, request_id: str) -> dict[str, Any] | None:
    """Get a request by ID."""
    return self.requests.get(request_id)

  def list_requests(self) -> list[dict[str, Any]]:
    """List all requests."""
    return list(self.requests.values())

  def create_quote(self, request_id: str, quote: dict[str, Any]) -> dict[str, Any]:
    """Create a new quote for a request."""
    quote_id = quote["id"]
    quote["request_id"] = request_id
    quote["created_at"] = datetime.now(timezone.utc).isoformat()
    quote["status"] = "pending"
    self.quotes[quote_id] = quote
    self.request_quotes[request_id].append(quote_id)
    return quote

  def get_quote(self, quote_id: str) -> dict[str, Any] | None:
    """Get a quote by ID."""
    return self.quotes.get(quote_id)

  def list_quotes_for_request(self, request_id: str) -> list[dict[str, Any]]:
    """List all quotes for a request."""
    quote_ids = self.request_quotes.get(request_id, [])
    return [self.quotes[quote_id] for quote_id in quote_ids if quote_id in self.quotes]

  def claim_idempotency(self, key: str) -> tuple[bool, dict[str, Any] | None]:
    """Atomically claim an idempotency key or return cached response.

    Returns:
        (claimed, response) where:
        - (True, None): Key claimed, caller should proceed with creation
        - (False, dict): Cached response exists, return it
        - (False, None): Key is being processed by another request

    """
    with self._idempotency_lock:
      if key in self.idempotency_cache:
        value = self.idempotency_cache[key]
        if value is _PENDING:
          return False, None  # In progress
        # Return a deep copy so callers can't mutate the cached response.
        return False, copy.deepcopy(value)  # type: ignore[return-value]
      self.idempotency_cache[key] = _PENDING
      return True, None

  def complete_idempotency(self, key: str, response: dict[str, Any]) -> None:
    """Set the final response for a claimed idempotency key."""
    with self._idempotency_lock:
      # Store a deep copy so later mutations to the original (e.g., in
      # update_delivery_event) don't affect the cached idempotent response.
      self.idempotency_cache[key] = copy.deepcopy(response)

  def release_idempotency(self, key: str) -> None:
    """Release a claim on failure, allowing retry with same key."""
    with self._idempotency_lock:
      if self.idempotency_cache.get(key) is _PENDING:
        del self.idempotency_cache[key]

  def create_delivery(
    self,
    request_id: str,
    quote_id: str,
    webhook_url: str | None = None,
    event_vocabulary: str = "xyz.localprotocol.delivery.courier@2026-01-30",
  ) -> dict[str, Any]:
    """Create a new delivery from an accepted quote.

    Args:
        request_id: The request ID.
        quote_id: The quote ID.
        webhook_url: Optional webhook URL for event notifications.
        event_vocabulary: The event vocabulary to use.

    Returns:
        The created delivery object.

    """
    import uuid

    delivery_id = f"del_{uuid.uuid4().hex[:8]}"
    now = datetime.now(timezone.utc).isoformat()

    # Derive payment_instrument_id from the quote's payment instruments
    quote = self.quotes.get(quote_id, {})
    payment = quote.get("payment", {})
    instruments = payment.get("instruments", [])
    payment_instrument_id = instruments[0]["id"] if instruments else f"pi_{uuid.uuid4().hex[:8]}"

    delivery = {
      "id": delivery_id,
      "request_id": request_id,
      "quote_id": quote_id,
      "event": "created",
      "event_description": "Delivery created",
      "event_vocabulary": event_vocabulary,
      "payment_instrument_id": payment_instrument_id,
      "webhook_url": webhook_url,
      "created_at": now,
      "updated_at": now,
    }
    self.deliveries[delivery_id] = delivery
    return delivery

  def get_delivery(self, delivery_id: str) -> dict[str, Any] | None:
    """Get a delivery by ID."""
    return self.deliveries.get(delivery_id)

  def list_deliveries(self) -> list[dict[str, Any]]:
    """List all deliveries."""
    return list(self.deliveries.values())

  def update_delivery_event(
    self,
    delivery_id: str,
    event: str,
    event_description: str,
  ) -> dict[str, Any] | None:
    """Update a delivery's event.

    Args:
        delivery_id: The delivery ID.
        event: The new event ID.
        event_description: The new event description.

    Returns:
        The updated delivery object, or None if not found.

    """
    delivery = self.deliveries.get(delivery_id)
    if delivery is None:
      return None

    delivery["event"] = event
    delivery["event_description"] = event_description
    delivery["updated_at"] = datetime.now(timezone.utc).isoformat()
    return delivery


# Global database instance
db = Database()
