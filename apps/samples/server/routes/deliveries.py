"""Delivery endpoints for the sample server."""

import logging
from dataclasses import dataclass
from typing import Any

import httpx
from fastapi import APIRouter, BackgroundTasks, HTTPException
from pydantic import BaseModel

from db import db

logger = logging.getLogger(__name__)

router = APIRouter()


class CreateDeliveryRequest(BaseModel):
  """Request body for creating a delivery."""

  ask_id: str
  bid_id: str
  nonce: str
  webhook_url: str | None = None
  event_vocabulary: str = "xyz.localprotocol.delivery.courier@2026-01-30"


class UpdateEventRequest(BaseModel):
  """Request body for updating a delivery event."""

  event: str
  event_description: str


# Frozen dataclass captures delivery state at update time. The background task
# receives this snapshot instead of the mutable delivery dict, preventing race
# conditions where delivery could be mutated again before the webhook fires.
@dataclass(frozen=True)
class WebhookEventSnapshot:
  """Immutable snapshot of delivery data for webhook delivery."""

  delivery_id: str
  event: str
  event_description: str
  event_vocabulary: str
  updated_at: str
  webhook_url: str


async def push_webhook_event(snapshot: WebhookEventSnapshot) -> None:
  """Push event notification to registered webhook URL.

  Args:
      snapshot: Immutable snapshot of delivery event data.

  """
  payload = {
    "event_type": "delivery_event",
    "delivery_id": snapshot.delivery_id,
    "event": snapshot.event,
    "event_description": snapshot.event_description,
    "event_vocabulary": snapshot.event_vocabulary,
    "updated_at": snapshot.updated_at,
  }

  try:
    async with httpx.AsyncClient() as client:
      response = await client.post(snapshot.webhook_url, json=payload, timeout=5.0)
      if response.is_error:
        logger.warning(
          f"Webhook returned error: status={response.status_code} "
          f"body={response.text} url={snapshot.webhook_url} "
          f"delivery_id={snapshot.delivery_id}"
        )
  except Exception as e:
    # Webhook failures should not block event transitions
    logger.warning(
      f"Failed to push webhook event: {e} url={snapshot.webhook_url} "
      f"delivery_id={snapshot.delivery_id}"
    )


@router.post("/deliveries", status_code=201)
async def create_delivery(
  request: CreateDeliveryRequest,
) -> dict[str, Any]:
  """Create a new delivery from an accepted bid."""
  # Check idempotency using nonce
  nonce = request.nonce
  key = f"delivery:{nonce}"
  claimed, cached = db.claim_idempotency(key)

  if not claimed:
    if cached is not None:
      return cached
    raise HTTPException(
      status_code=409,
      detail="Request with this nonce is already being processed",
    )

  try:
    # Verify ask exists
    ask = db.get_ask(request.ask_id)
    if ask is None:
      raise HTTPException(status_code=404, detail="Ask not found")

    # Verify bid exists
    bid = db.get_bid(request.bid_id)
    if bid is None:
      raise HTTPException(status_code=404, detail="Bid not found")

    # Verify bid belongs to the ask
    if bid.get("ask_id") != request.ask_id:
      raise HTTPException(
        status_code=400,
        detail=f"Bid {request.bid_id} does not belong to ask {request.ask_id}",
      )

    # Create delivery
    delivery = db.create_delivery(
      ask_id=request.ask_id,
      bid_id=request.bid_id,
      webhook_url=request.webhook_url,
      event_vocabulary=request.event_vocabulary,
    )

    db.complete_idempotency(key, delivery)
    return delivery
  except Exception:
    db.release_idempotency(key)
    raise


@router.get("/deliveries/{delivery_id}")
async def get_delivery(delivery_id: str) -> dict[str, Any]:
  """Get a delivery by ID."""
  delivery = db.get_delivery(delivery_id)
  if delivery is None:
    raise HTTPException(status_code=404, detail="Delivery not found")
  return delivery


@router.get("/deliveries")
async def list_deliveries() -> list[dict[str, Any]]:
  """List all deliveries."""
  return db.list_deliveries()


@router.patch("/deliveries/{delivery_id}/event")
async def update_delivery_event(
  delivery_id: str,
  request: UpdateEventRequest,
  background_tasks: BackgroundTasks,
) -> dict[str, Any]:
  """Update a delivery's event."""
  delivery = db.update_delivery_event(
    delivery_id=delivery_id,
    event=request.event,
    event_description=request.event_description,
  )
  if delivery is None:
    raise HTTPException(status_code=404, detail="Delivery not found")

  # Push webhook event in background with immutable snapshot
  webhook_url = delivery.get("webhook_url")
  if webhook_url:
    snapshot = WebhookEventSnapshot(
      delivery_id=delivery["id"],
      event=delivery["event"],
      event_description=delivery["event_description"],
      event_vocabulary=delivery["event_vocabulary"],
      updated_at=delivery["updated_at"],
      webhook_url=webhook_url,
    )
    background_tasks.add_task(push_webhook_event, snapshot)

  return delivery
