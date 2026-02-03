"""Bid endpoints."""

import re
from typing import Any

from fastapi import APIRouter, HTTPException, status

from db import db, validate_nonce

router = APIRouter(prefix="/asks/{ask_id}/bids", tags=["bids"])

CURRENCY_PATTERN = re.compile(r"^[A-Z]{3}$")


def validate_bid(bid: dict[str, Any]) -> list[str]:
  """Validate bid payload and return list of errors."""
  errors = []
  required_fields = [
    "id",
    "nonce",
    "price",
    "currency",
    "pickup_location",
    "dropoff_location",
    "pickup_estimate",
    "dropoff_estimate",
  ]
  for field in required_fields:
    if field not in bid:
      errors.append(f"Missing required field: {field}")

  # Validate price
  if "price" in bid:
    price = bid["price"]
    if not isinstance(price, int) or price < 0:
      errors.append("Price must be a non-negative integer")

  # Validate currency format
  if "currency" in bid:
    currency = bid["currency"]
    if not isinstance(currency, str) or not CURRENCY_PATTERN.match(currency):
      errors.append("Currency must be a 3-letter ISO 4217 code")

  # Validate time format (basic check)
  for time_field in ["pickup_estimate", "dropoff_estimate"]:
    if time_field in bid:
      value = bid[time_field]
      if not isinstance(value, str) or "T" not in value:
        errors.append(f"Invalid datetime format for {time_field}")

  return errors


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_bid(ask_id: str, bid: dict[str, Any]) -> dict[str, Any]:
  """Create a new bid for an ask."""
  # Check ask exists
  ask = db.get_ask(ask_id)
  if not ask:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail=f"Ask {ask_id} not found",
    )

  # Validate
  errors = validate_bid(bid)
  if errors:
    raise HTTPException(
      status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
      detail={"errors": errors},
    )

  # Check idempotency using nonce
  try:
    nonce = validate_nonce(bid.get("nonce"))
  except ValueError as e:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
  key = f"bid:{ask_id}:{nonce}"
  claimed, cached = db.claim_idempotency(key)

  if not claimed:
    if cached is not None:
      return cached
    raise HTTPException(
      status_code=status.HTTP_409_CONFLICT,
      detail="Request with this nonce is already being processed",
    )

  try:
    # Check for duplicate bid ID
    if db.get_bid(bid["id"]):
      raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail="Bid ID already exists",
      )

    # Create
    created = db.create_bid(ask_id, bid)
    db.complete_idempotency(key, created)
    return created
  except Exception:
    db.release_idempotency(key)
    raise


@router.get("")
async def list_bids(ask_id: str) -> list[dict[str, Any]]:
  """List all bids for an ask."""
  # Check ask exists
  ask = db.get_ask(ask_id)
  if not ask:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail=f"Ask {ask_id} not found",
    )

  return db.list_bids_for_ask(ask_id)


@router.get("/{bid_id}")
async def get_bid(ask_id: str, bid_id: str) -> dict[str, Any]:
  """Get a specific bid."""
  # Check ask exists
  ask = db.get_ask(ask_id)
  if not ask:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail=f"Ask {ask_id} not found",
    )

  bid = db.get_bid(bid_id)
  if not bid or bid.get("ask_id") != ask_id:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail=f"Bid {bid_id} not found for ask {ask_id}",
    )

  return bid
