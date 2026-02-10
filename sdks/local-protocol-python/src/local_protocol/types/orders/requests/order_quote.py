# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ...._models import BaseModel

__all__ = ["OrderQuote"]


class OrderQuote(BaseModel):
    """An order quote."""

    id: str
    """Unique quote identifier."""

    expires_at: datetime
    """Quote expiration time (RFC 3339)."""

    intent_id: str
    """Shared intent identifier for tracing Request -> Quote -> Order."""

    nonce: str
    """Client-generated idempotency key."""

    price: int
    """Price in minor currency units."""

    ready_at: datetime
    """Estimated readiness time (RFC 3339)."""
