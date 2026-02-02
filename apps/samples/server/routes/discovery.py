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
      }
    },
    "endpoints": {
      "asks": "/asks",
      "health": "/healthz",
    },
  }


@router.get("/healthz")
async def health_check() -> dict:
  """Health check endpoint."""
  return {"status": "ok"}
