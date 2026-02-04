"""Request endpoints."""

from typing import Any

from fastapi import APIRouter, HTTPException, status

from db import db, validate_nonce

router = APIRouter(prefix="/requests", tags=["requests"])


def validate_request(request: dict[str, Any]) -> list[str]:
  """Validate request payload and return list of errors."""
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
    if field not in request:
      errors.append(f"Missing required field: {field}")

  # Validate time format (basic check)
  for time_field in ["pickup_time", "dropoff_time"]:
    if time_field in request:
      value = request[time_field]
      if not isinstance(value, str) or "T" not in value:
        errors.append(f"Invalid datetime format for {time_field}")

  return errors


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_request(request: dict[str, Any]) -> dict[str, Any]:
  """Create a new delivery request."""
  # Validate
  errors = validate_request(request)
  if errors:
    raise HTTPException(
      status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
      detail={"errors": errors},
    )

  # Check idempotency using nonce
  try:
    nonce = validate_nonce(request.get("nonce"))
  except ValueError as e:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
  key = f"request:{nonce}"
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
    if db.get_request(request["id"]):
      raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail=f"Request with id {request['id']} already exists",
      )

    # Create
    created = db.create_request(request)
    db.complete_idempotency(key, created)
    return created
  except Exception:
    db.release_idempotency(key)
    raise


@router.get("/{request_id}")
async def get_request(request_id: str) -> dict[str, Any]:
  """Get a request by ID."""
  request = db.get_request(request_id)
  if not request:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail=f"Request {request_id} not found",
    )
  return request


@router.get("")
async def list_requests() -> list[dict[str, Any]]:
  """List all requests."""
  return db.list_requests()
