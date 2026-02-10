# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["ModifierGroup"]


class ModifierGroup(BaseModel):
    """Group of modifier options with selection constraints."""

    id: str
    """Modifier group identifier."""

    modifier_options: List["ModifierOption"]
    """Ordered modifier options within this group."""

    name: str
    """Display name for the modifier group."""

    allow_quantities: Optional[bool] = None
    """Whether options can be selected with quantities > 1."""

    description: Optional[str] = None
    """Optional modifier group description."""

    max_per_modifier: Optional[int] = None
    """Maximum quantity per modifier option."""

    maximum_selections: Optional[int] = None
    """Maximum selections allowed."""

    metadata: Optional[Dict[str, object]] = None
    """Business-defined custom data."""

    minimum_selections: Optional[int] = None
    """Minimum selections required."""

    type: Optional[str] = None
    """Modifier group type classification."""


from .modifier_option import ModifierOption
