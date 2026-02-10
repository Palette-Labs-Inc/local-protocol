# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PostalAddressParam"]


class PostalAddressParam(TypedDict, total=False):
    address_country: str
    """Country (ISO 3166-1 alpha-2 recommended)."""

    address_locality: str
    """City or locality."""

    address_region: str
    """State, province, or region."""

    extended_address: str
    """Address extension (apartment number, C/O, etc.)."""

    first_name: str
    """Contact first name."""

    last_name: str
    """Contact last name."""

    phone_number: str
    """Contact phone number."""

    postal_code: str
    """Postal code."""

    street_address: str
    """The street address."""
