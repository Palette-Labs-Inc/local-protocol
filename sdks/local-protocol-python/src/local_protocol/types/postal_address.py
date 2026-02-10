# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["PostalAddress"]


class PostalAddress(BaseModel):
    address_country: Optional[str] = None
    """Country (ISO 3166-1 alpha-2 recommended)."""

    address_locality: Optional[str] = None
    """City or locality."""

    address_region: Optional[str] = None
    """State, province, or region."""

    extended_address: Optional[str] = None
    """Address extension (apartment number, C/O, etc.)."""

    first_name: Optional[str] = None
    """Contact first name."""

    last_name: Optional[str] = None
    """Contact last name."""

    phone_number: Optional[str] = None
    """Contact phone number."""

    postal_code: Optional[str] = None
    """Postal code."""

    street_address: Optional[str] = None
    """The street address."""
