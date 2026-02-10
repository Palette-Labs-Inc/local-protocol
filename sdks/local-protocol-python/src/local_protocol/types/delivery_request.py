# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .location import Location

__all__ = ["DeliveryRequest"]


class DeliveryRequest(BaseModel):
    """A delivery request."""

    id: str
    """Unique request identifier."""

    dropoff_location: Location
    """A location specified by coordinates and/or postal address.

    At least one must be provided.
    """

    dropoff_time: datetime
    """Requested dropoff time (RFC 3339)."""

    nonce: str
    """Client-generated idempotency key."""

    pickup_location: Location
    """A location specified by coordinates and/or postal address.

    At least one must be provided.
    """

    pickup_time: datetime
    """Requested pickup time (RFC 3339)."""

    dropoff_instructions: Optional[str] = None
    """Dropoff directions, access codes, or delivery notes."""

    pickup_instructions: Optional[str] = None
    """Pickup directions, access codes, or handling notes."""
