# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DeliveryUpdateEventParams"]


class DeliveryUpdateEventParams(TypedDict, total=False):
    event: Required[str]
    """Event identifier from the delivery's event vocabulary."""

    event_description: Required[str]
    """Human-readable event description."""
