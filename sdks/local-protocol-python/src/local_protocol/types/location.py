# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .postal_address import PostalAddress

__all__ = ["Location", "Coordinates"]


class Coordinates(BaseModel):
    """Geographic coordinates."""

    latitude: float
    """Latitude in decimal degrees."""

    longitude: float
    """Longitude in decimal degrees."""


class Location(BaseModel):
    """A location specified by coordinates and/or postal address.

    At least one must be provided.
    """

    coordinates: Optional[Coordinates] = None
    """Geographic coordinates."""

    postal_address: Optional[PostalAddress] = None
