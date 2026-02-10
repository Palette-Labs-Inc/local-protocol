# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["OrderCreateParams"]


class OrderCreateParams(TypedDict, total=False):
    nonce: Required[str]
    """Client-generated idempotency key."""

    order_quote_id: Required[str]
    """The accepted quote."""

    order_request_id: Required[str]
    """The order request to fulfill."""

    payment_instrument_id: Required[str]
    """Reference to the registered payment instrument."""
