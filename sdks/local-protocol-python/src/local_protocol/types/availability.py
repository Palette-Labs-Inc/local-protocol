# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List, Optional

from .._models import BaseModel

__all__ = ["Availability", "Interval"]


class Interval(BaseModel):
    """A single time interval for a day of the week or a specific date."""

    from_hour: int
    """Start hour (0-23)."""

    from_minute: int
    """Start minute (0-59)."""

    to_hour: int
    """End hour (0-23)."""

    to_minute: int
    """End minute (0-59)."""

    date: Optional[datetime.date] = None
    """Calendar date in YYYY-MM-DD."""

    day: Optional[str] = None
    """Day of week (e.g., Monday, Tuesday)."""


class Availability(BaseModel):
    """Availability schedule for a catalog, category, or item."""

    intervals: List[Interval]
    """Availability intervals (weekly or date-specific)."""

    timezone: Optional[str] = None
    """IANA timezone. Defaults to merchant timezone when omitted."""
