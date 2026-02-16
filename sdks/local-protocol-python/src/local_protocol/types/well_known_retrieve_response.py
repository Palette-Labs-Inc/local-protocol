# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from .._models import BaseModel

__all__ = ["WellKnownRetrieveResponse"]


class WellKnownRetrieveResponse(BaseModel):
    """Canonical UCP discovery response envelope."""

    ucp: Dict[str, object]
    """Canonical UCP discovery profile.

    Structure:
    - version: str (YYYY-MM-DD)
    - services: dict[str, list[dict]]
    - capabilities: dict[str, list[dict]]
    - payment_handlers: dict[str, list[dict]]
    """
