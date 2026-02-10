# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .location_param import LocationParam

__all__ = ["RequestCreateParams"]


class RequestCreateParams(TypedDict, total=False):
    id: Required[str]
    """Unique request identifier."""

    dropoff_location: Required[LocationParam]
    """A location specified by coordinates and/or postal address.

    At least one must be provided.
    """

    dropoff_time: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Requested dropoff time (RFC 3339)."""

    nonce: Required[str]
    """Client-generated idempotency key."""

    pickup_location: Required[LocationParam]
    """A location specified by coordinates and/or postal address.

    At least one must be provided.
    """

    pickup_time: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Requested pickup time (RFC 3339)."""

    dropoff_instructions: str
    """Dropoff directions, access codes, or delivery notes."""

    pickup_instructions: str
    """Pickup directions, access codes, or handling notes."""
