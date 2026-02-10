# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["RequestCreateResponse"]


class RequestCreateResponse(BaseModel):
    """An order request."""

    id: str
    """Unique request identifier."""

    intent_id: str
    """Shared intent identifier for tracing Request -> Quote -> Order."""

    nonce: str
    """Client-generated idempotency key."""
