"""Discovery and health endpoints."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/.well-known/local-protocol")
async def well_known() -> dict:
  """Service discovery endpoint."""
  return {
    "version": "0.1.0",
    "name": "Local Protocol Sample Server",
    "capabilities": {
      "delivery": {
        "asks": True,
        "bids": True,
        "conforms_to": ["xyz.localprotocol.delivery.courier@2026-01-30"],
      }
    },
    "endpoints": {
      "asks": "/asks",
      "bids": "/asks/{ask_id}/bids",
      "deliveries": "/deliveries",
      "health": "/healthz",
    },
  }


@router.get("/healthz")
async def health_check() -> dict:
  """Health check endpoint."""
  return {"status": "ok"}
