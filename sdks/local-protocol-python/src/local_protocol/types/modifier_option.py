# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional

from .amount import Amount
from .._models import BaseModel

__all__ = ["ModifierOption", "ModifierItem"]


class ModifierItem(BaseModel):
    """Modifier item for this option."""

    id: str
    """Modifier item identifier."""

    name: str
    """Modifier item name."""

    price: Amount
    """Price for this modifier item."""

    description: Optional[str] = None
    """Optional modifier item description."""

    metadata: Optional[Dict[str, object]] = None
    """Business-defined custom data."""


class ModifierOption(BaseModel):
    """Selectable option within a modifier group."""

    id: str
    """Modifier option identifier."""

    modifier_item: ModifierItem
    """Modifier item for this option."""

    child_modifier_groups: Optional[List["ModifierGroup"]] = None
    """Nested modifier groups required after selecting this option."""

    is_default: Optional[bool] = None
    """Whether this option is selected by default."""

    metadata: Optional[Dict[str, object]] = None
    """Business-defined custom data."""


from .modifier_group import ModifierGroup
