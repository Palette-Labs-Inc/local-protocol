# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Literal

from .amount import Amount
from .._models import BaseModel
from .availability import Availability

__all__ = ["CatalogCategory", "Item", "ItemMedia"]


class ItemMedia(BaseModel):
    """Product media item (image, video, etc.)."""

    type: Literal["image", "video", "model_3d"]
    """Media type discriminator."""

    url: str
    """URL to the media resource."""

    alt_text: Optional[str] = None
    """Accessibility text describing the media."""

    height: Optional[int] = None
    """Height in pixels."""

    width: Optional[int] = None
    """Width in pixels."""


class Item(BaseModel):
    """A menu item with embedded modifier groups."""

    id: str
    """Item identifier."""

    description: str
    """Item description."""

    name: str
    """Item name."""

    price: Amount
    """Base price for the item."""

    availability: Optional[Availability] = None
    """Item availability."""

    media: Optional[List[ItemMedia]] = None
    """Item media (images, videos, 3D models)."""

    metadata: Optional[Dict[str, object]] = None
    """Business-defined custom data."""

    modifier_groups: Optional[List["ModifierGroup"]] = None
    """Modifier groups available for this item."""


class CatalogCategory(BaseModel):
    """A category grouping items in a catalog."""

    id: str
    """Category identifier."""

    items: List[Item]
    """Ordered items in this category."""

    name: str
    """Category display name."""

    availability: Optional[Availability] = None
    """Category availability."""

    categories: Optional[List["CatalogCategory"]] = None
    """Ordered child categories for nested category trees."""

    description: Optional[str] = None
    """Optional category description."""

    metadata: Optional[Dict[str, object]] = None
    """Business-defined custom data."""


from .modifier_group import ModifierGroup
