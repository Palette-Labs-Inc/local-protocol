# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["EventVocabularyRetrieveResponse", "Events"]


class Events(BaseModel):
    """A single delivery event definition."""

    description: str
    """Human-readable description of the event."""


class EventVocabularyRetrieveResponse(BaseModel):
    """Schema for delivery event vocabularies."""

    events: Dict[str, Events]
    """Map of event IDs to event definitions."""

    name: str
    """Standard identifier in reverse-domain notation."""

    title: str
    """Human-readable title."""

    version: str
    """Version in YYYY-MM-DD format."""

    description: Optional[str] = None
    """Human-readable description."""

    extends: Optional[List[str]] = None
    """Parent standard this extends (optional, max one)."""

    spec: Optional[str] = None
    """URL to specification document."""
