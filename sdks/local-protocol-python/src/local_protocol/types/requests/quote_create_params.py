# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..payment_param import PaymentParam
from ..location_param import LocationParam

__all__ = ["QuoteCreateParams"]


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

    payment: Required[PaymentParam]
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
