"""Ask endpoints."""

from typing import Any

from fastapi import APIRouter, HTTPException, status

from db import db

router = APIRouter(prefix="/asks", tags=["asks"])


def validate_ask(ask: dict[str, Any]) -> list[str]:
  """Validate ask payload and return list of errors."""
  errors = []
  required_fields = [
    "id",
    "nonce",
    "pickup_location",
    "dropoff_location",
    "pickup_time",
    "dropoff_time",
  ]
  for field in required_fields:
    if field not in ask:
      errors.append(f"Missing required field: {field}")

  # Validate time format (basic check)
  for time_field in ["pickup_time", "dropoff_time"]:
    if time_field in ask:
      value = ask[time_field]
      if not isinstance(value, str) or "T" not in value:
        errors.append(f"Invalid datetime format for {time_field}")

  return errors


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_ask(ask: dict[str, Any]) -> dict[str, Any]:
  """Create a new delivery ask."""
  # Validate
  errors = validate_ask(ask)
  if errors:
    raise HTTPException(
      status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
      detail={"errors": errors},
    )

  # Check idempotency using nonce
  nonce = ask["nonce"]
  key = f"ask:{nonce}"
  claimed, cached = db.claim_idempotency(key)

  if not claimed:
    if cached is not None:
      return cached
    raise HTTPException(
      status_code=status.HTTP_409_CONFLICT,
      detail="Request with this nonce is already being processed",
    )

  try:
    # Check for duplicate ID
    if db.get_ask(ask["id"]):
      raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail=f"Ask with id {ask['id']} already exists",
      )

    # Create
    created = db.create_ask(ask)
    db.complete_idempotency(key, created)
    return created
  except Exception:
    db.release_idempotency(key)
    raise


@router.get("/{ask_id}")
async def get_ask(ask_id: str) -> dict[str, Any]:
  """Get an ask by ID."""
  ask = db.get_ask(ask_id)
  if not ask:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail=f"Ask {ask_id} not found",
    )
  return ask


@router.get("")
async def list_asks() -> list[dict[str, Any]]:
  """List all asks."""
  return db.list_asks()
