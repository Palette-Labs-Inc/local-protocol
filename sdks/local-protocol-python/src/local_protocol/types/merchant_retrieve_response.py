# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .amount import Amount
from .._models import BaseModel
from .availability import Availability

__all__ = ["MerchantRetrieveResponse", "Catalog", "CatalogItem", "CatalogItemMedia"]


class CatalogItemMedia(BaseModel):
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


class CatalogItem(BaseModel):
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

    media: Optional[List[CatalogItemMedia]] = None
    """Item media (images, videos, 3D models)."""

    metadata: Optional[Dict[str, object]] = None
    """Business-defined custom data."""

    modifier_groups: Optional[List["ModifierGroup"]] = None
    """Modifier groups available for this item."""


class Catalog(BaseModel):
    """
    A catalog containing embedded categories, items, availability, and fulfillment configuration.
    """

    id: str
    """Catalog identifier."""

    categories: List["CatalogCategory"]
    """Ordered top-level categories."""

    name: str
    """Catalog name."""

    availability: Optional[Availability] = None
    """Catalog-wide availability override."""

    description: Optional[str] = None
    """Catalog description."""

    items: Optional[List[CatalogItem]] = None
    """Items not assigned to a category."""

    metadata: Optional[Dict[str, object]] = None
    """Business-defined custom data."""


class MerchantRetrieveResponse(BaseModel):
    """Merchant catalog payload containing denormalized catalogs."""

    id: str
    """Merchant identifier."""

    catalogs: List[Catalog]
    """Catalogs available for the merchant."""

    name: str
    """Merchant name."""

    timezone: str
    """IANA timezone for availability schedules."""

    last_updated: Optional[datetime] = None
    """RFC 3339 timestamp of the latest catalog update."""

    metadata: Optional[Dict[str, object]] = None
    """Business-defined custom data."""


from .modifier_group import ModifierGroup
from .catalog_category import CatalogCategory
