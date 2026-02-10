# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .postal_address_param import PostalAddressParam

__all__ = ["LocationParam", "Coordinates"]


class Coordinates(TypedDict, total=False):
    """Geographic coordinates."""

    latitude: Required[float]
    """Latitude in decimal degrees."""

    longitude: Required[float]
    """Longitude in decimal degrees."""


class LocationParam(TypedDict, total=False):
    """A location specified by coordinates and/or postal address.

    At least one must be provided.
    """

    coordinates: Coordinates
    """Geographic coordinates."""

    postal_address: PostalAddressParam
