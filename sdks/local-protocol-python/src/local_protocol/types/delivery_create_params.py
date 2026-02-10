# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["DeliveryCreateParams"]


class DeliveryCreateParams(TypedDict, total=False):
    nonce: Required[str]
    """Client-generated idempotency key."""

    quote_id: Required[str]
    """The accepted quote."""

    request_id: Required[str]
    """The delivery request to fulfill."""

    event_vocabulary: str
    """Event vocabulary standard to use."""

    webhook_url: Optional[str]
    """Optional URL to receive delivery event webhook notifications."""
