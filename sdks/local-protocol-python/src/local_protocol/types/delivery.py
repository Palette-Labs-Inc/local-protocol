# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Delivery"]


class Delivery(BaseModel):
    """A delivery resource."""

    id: str
    """Unique delivery identifier."""

    created_at: datetime
    """Creation timestamp (RFC 3339)."""

    event: str
    """Current event identifier."""

    event_description: str
    """Human-readable description of the current event."""

    event_vocabulary: str
    """Event vocabulary standard in use."""

    payment_instrument_id: str
    """Reference to the payment instrument used to create this delivery."""

    quote_id: str
    """Reference to the accepted quote."""

    request_id: str
    """Reference to the delivery request."""

    updated_at: datetime
    """Last update timestamp (RFC 3339)."""

    webhook_url: Optional[str] = None
    """Registered webhook URL, if any."""
