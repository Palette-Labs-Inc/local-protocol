# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CoordinatesParam"]


class CoordinatesParam(TypedDict, total=False):
    """Geographic coordinates."""

    latitude: Required[float]
    """Latitude in decimal degrees."""

    longitude: Required[float]
    """Longitude in decimal degrees."""
