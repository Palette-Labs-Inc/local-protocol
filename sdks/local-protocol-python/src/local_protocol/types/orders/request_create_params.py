# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["RequestCreateParams", "Item"]


class RequestCreateParams(TypedDict, total=False):
    id: Required[str]
    """Unique cart identifier."""

    intent_id: Required[str]
    """Shared intent identifier for tracing Request -> Quote -> Order."""

    items: Required[Iterable[Item]]
    """Items in the cart."""

    nonce: Required[str]
    """Client-generated idempotency key."""


class Item(TypedDict, total=False):
    """An item in a cart."""

    id: Required[str]
    """Item identifier."""

    quantity: Required[int]
    """Quantity requested."""
