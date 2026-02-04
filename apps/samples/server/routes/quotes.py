"""Quote endpoints."""

import re
from typing import Any

from fastapi import APIRouter, HTTPException, status

from db import db, validate_nonce

router = APIRouter(prefix="/requests/{request_id}/quotes", tags=["quotes"])

CURRENCY_PATTERN = re.compile(r"^[A-Z]{3}$")


def validate_quote(quote: dict[str, Any]) -> list[str]:
  """Validate quote payload and return list of errors."""
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
    if field not in quote:
      errors.append(f"Missing required field: {field}")

  # Validate price
  if "price" in quote:
    price = quote["price"]
    if not isinstance(price, int) or price < 0:
      errors.append("Price must be a non-negative integer")

  # Validate currency format
  if "currency" in quote:
    currency = quote["currency"]
    if not isinstance(currency, str) or not CURRENCY_PATTERN.match(currency):
      errors.append("Currency must be a 3-letter ISO 4217 code")

  # Validate time format (basic check)
  for time_field in ["pickup_estimate", "dropoff_estimate"]:
    if time_field in quote:
      value = quote[time_field]
      if not isinstance(value, str) or "T" not in value:
        errors.append(f"Invalid datetime format for {time_field}")

  return errors


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_quote(request_id: str, quote: dict[str, Any]) -> dict[str, Any]:
  """Create a new quote for a request."""
  # Check request exists
  request = db.get_request(request_id)
  if not request:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail=f"Request {request_id} not found",
    )

  # Validate
  errors = validate_quote(quote)
  if errors:
    raise HTTPException(
      status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
      detail={"errors": errors},
    )

  # Check idempotency using nonce
  try:
    nonce = validate_nonce(quote.get("nonce"))
  except ValueError as e:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
  key = f"quote:{request_id}:{nonce}"
  claimed, cached = db.claim_idempotency(key)

  if not claimed:
    if cached is not None:
      return cached
    raise HTTPException(
      status_code=status.HTTP_409_CONFLICT,
      detail="Request with this nonce is already being processed",
    )

  try:
    # Check for duplicate quote ID
    if db.get_quote(quote["id"]):
      raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail="Quote ID already exists",
      )

    # Create
    created = db.create_quote(request_id, quote)
    db.complete_idempotency(key, created)
    return created
  except Exception:
    db.release_idempotency(key)
    raise


@router.get("")
async def list_quotes(request_id: str) -> list[dict[str, Any]]:
  """List all quotes for a request."""
  # Check request exists
  request = db.get_request(request_id)
  if not request:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail=f"Request {request_id} not found",
    )

  return db.list_quotes_for_request(request_id)


@router.get("/{quote_id}")
async def get_quote(request_id: str, quote_id: str) -> dict[str, Any]:
  """Get a specific quote."""
  # Check request exists
  request = db.get_request(request_id)
  if not request:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail=f"Request {request_id} not found",
    )

  quote = db.get_quote(quote_id)
  if not quote or quote.get("request_id") != request_id:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail=f"Quote {quote_id} not found for request {request_id}",
    )

  return quote
