# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .. import payment_instrument
from ..._models import BaseModel
from ..location import Location

__all__ = ["DeliveryQuote", "Payment", "PaymentInstrument"]


class PaymentInstrument(payment_instrument.PaymentInstrument):
    """A payment instrument with selection state."""

    selected: Optional[bool] = None
    """Whether this instrument is selected by the user."""


class Payment(BaseModel):
    """Payment handlers available for accepting this quote."""

    instruments: Optional[List[PaymentInstrument]] = None
    """Payment instruments available.

    Each instrument is associated with a handler via handler_id.
    """


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
