# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..location_param import LocationParam
from ..payment_instrument_param import PaymentInstrumentParam

__all__ = ["QuoteCreateParams", "Payment", "PaymentInstrument"]


class QuoteCreateParams(TypedDict, total=False):
    id: Required[str]
    """Unique quote identifier."""

    currency: Required[str]
    """ISO 4217 currency code."""

    dropoff_estimate: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Estimated dropoff time (RFC 3339)."""

    dropoff_location: Required[LocationParam]
    """A location specified by coordinates and/or postal address.

    At least one must be provided.
    """

    nonce: Required[str]
    """Client-generated idempotency key."""

    payment: Required[Payment]
    """Payment handlers available for accepting this quote."""

    pickup_estimate: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Estimated pickup time (RFC 3339)."""

    pickup_location: Required[LocationParam]
    """A location specified by coordinates and/or postal address.

    At least one must be provided.
    """

    price: Required[int]
    """Price in minor currency units."""

    expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Time when the quote expires (RFC 3339)."""


class PaymentInstrument(PaymentInstrumentParam, total=False):
    """A payment instrument with selection state."""

    selected: bool
    """Whether this instrument is selected by the user."""


class Payment(TypedDict, total=False):
    """Payment handlers available for accepting this quote."""

    instruments: Iterable[PaymentInstrument]
    """Payment instruments available.

    Each instrument is associated with a handler via handler_id.
    """
