# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from .._models import BaseModel

__all__ = ["WellKnownRetrieveResponse"]


class WellKnownRetrieveResponse(BaseModel):
    """Service discovery metadata."""

    capabilities: Dict[str, Dict[str, object]]
    """Supported capabilities by domain."""

    endpoints: Dict[str, str]
    """Endpoint path map."""

    name: str
    """Server name."""

    version: str
    """Protocol version."""
