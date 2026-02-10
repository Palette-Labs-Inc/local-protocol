# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["Order"]


class Order(BaseModel):
    """An order."""

    id: str
    """Unique order identifier."""

    intent_id: str
    """Shared intent identifier for tracing Request -> Quote -> Order."""

    nonce: str
    """Client-generated idempotency key."""

    payment_instrument_id: str
    """Reference to the payment instrument used."""
