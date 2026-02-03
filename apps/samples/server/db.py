"""In-memory database for sample server."""

from datetime import datetime, timezone
from typing import Any


class Database:
  """Simple in-memory database for asks and bids."""

  def __init__(self) -> None:
    self.asks: dict[str, dict[str, Any]] = {}
    self.bids: dict[str, dict[str, Any]] = {}  # bid_id -> bid
    self.ask_bids: dict[str, list[str]] = {}  # ask_id -> [bid_ids]
    self.idempotency_cache: dict[str, dict[str, Any]] = {}

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

  def get_idempotent_response(
    self, key: str
  ) -> dict[str, Any] | None:
    """Get cached response for idempotency key."""
    return self.idempotency_cache.get(key)

  def set_idempotent_response(
    self, key: str, response: dict[str, Any]
  ) -> None:
    """Cache response for idempotency key."""
    self.idempotency_cache[key] = response


# Global database instance
db = Database()
