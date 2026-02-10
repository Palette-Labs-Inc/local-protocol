# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .coordinates_param import CoordinatesParam
from .postal_address_param import PostalAddressParam

__all__ = ["LocationParam"]


class LocationParam(TypedDict, total=False):
    """A location specified by coordinates and/or postal address.

    At least one must be provided.
    """

    coordinates: CoordinatesParam
    """Geographic coordinates."""

    postal_address: PostalAddressParam
