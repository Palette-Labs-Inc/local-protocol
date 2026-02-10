# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..payment import Payment
from ..._models import BaseModel
from ..location import Location

__all__ = ["DeliveryQuote"]


class DeliveryQuote(BaseModel):
    """A delivery quote."""

    id: str
    """Unique quote identifier."""

    currency: str
    """ISO 4217 currency code."""

    dropoff_estimate: datetime
    """Estimated dropoff time (RFC 3339)."""

    dropoff_location: Location
    """A location specified by coordinates and/or postal address.

    At least one must be provided.
    """

    nonce: str
    """Client-generated idempotency key."""

    payment: Payment
    """Payment handlers available for accepting this quote."""

    pickup_estimate: datetime
    """Estimated pickup time (RFC 3339)."""

    pickup_location: Location
    """A location specified by coordinates and/or postal address.

    At least one must be provided.
    """

    price: int
    """Price in minor currency units."""

    expires_at: Optional[datetime] = None
    """Time when the quote expires (RFC 3339)."""
