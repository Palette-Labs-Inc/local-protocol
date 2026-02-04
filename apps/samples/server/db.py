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
  """Simple in-memory database for asks, bids, and deliveries."""

  def __init__(self) -> None:
    self.asks: dict[str, dict[str, Any]] = {}
    self.bids: dict[str, dict[str, Any]] = {}  # bid_id -> bid
    self.ask_bids: dict[str, list[str]] = {}  # ask_id -> [bid_ids]
    self.deliveries: dict[str, dict[str, Any]] = {}  # delivery_id -> delivery
    self.idempotency_cache: dict[str, dict[str, Any] | object] = {}
    # Lock prevents race conditions where concurrent requests with the same nonce
    # could both pass the "not in cache" check before either sets _PENDING.
    self._idempotency_lock = threading.Lock()

  def create_ask(self, ask: dict[str, Any]) -> dict[str, Any]:
    """Create a new ask."""
    ask_id = ask["id"]
    ask["created_at"] = datetime.now(timezone.utc).isoformat()
    ask["status"] = "open"
    self.asks[ask_id] = ask
    self.ask_bids[ask_id] = []
    return ask

  def get_ask(self, ask_id: str) -> dict[str, Any] | None:
    """Get an ask by ID."""
    return self.asks.get(ask_id)

  def list_asks(self) -> list[dict[str, Any]]:
    """List all asks."""
    return list(self.asks.values())

  def create_bid(self, ask_id: str, bid: dict[str, Any]) -> dict[str, Any]:
    """Create a new bid for an ask."""
    bid_id = bid["id"]
    bid["ask_id"] = ask_id
    bid["created_at"] = datetime.now(timezone.utc).isoformat()
    bid["status"] = "pending"
    self.bids[bid_id] = bid
    self.ask_bids[ask_id].append(bid_id)
    return bid

  def get_bid(self, bid_id: str) -> dict[str, Any] | None:
    """Get a bid by ID."""
    return self.bids.get(bid_id)

  def list_bids_for_ask(self, ask_id: str) -> list[dict[str, Any]]:
    """List all bids for an ask."""
    bid_ids = self.ask_bids.get(ask_id, [])
    return [self.bids[bid_id] for bid_id in bid_ids if bid_id in self.bids]

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
    ask_id: str,
    bid_id: str,
    webhook_url: str | None = None,
    event_vocabulary: str = "xyz.localprotocol.delivery.courier@2026-01-30",
  ) -> dict[str, Any]:
    """Create a new delivery from an accepted bid.

    Args:
        ask_id: The ask ID.
        bid_id: The bid ID.
        webhook_url: Optional webhook URL for event notifications.
        event_vocabulary: The event vocabulary to use.

    Returns:
        The created delivery object.

    """
    import uuid

    delivery_id = f"del_{uuid.uuid4().hex[:8]}"
    now = datetime.now(timezone.utc).isoformat()

    delivery = {
      "id": delivery_id,
      "ask_id": ask_id,
      "bid_id": bid_id,
      "event": "created",
      "event_description": "Delivery created",
      "event_vocabulary": event_vocabulary,
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
