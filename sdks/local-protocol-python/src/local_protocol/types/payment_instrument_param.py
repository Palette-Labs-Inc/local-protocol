# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Required, TypeAlias, TypedDict

from .postal_address_param import PostalAddressParam

__all__ = ["PaymentInstrumentParam", "Credential"]


class CredentialTyped(TypedDict, total=False):
    """Base definition for any payment credential."""

    type: Required[str]
    """Credential type discriminator."""


Credential: TypeAlias = Union[CredentialTyped, Dict[str, object]]


class PaymentInstrumentParam(TypedDict, total=False):
    """Base definition for any payment instrument."""

    id: Required[str]
    """Unique instrument identifier."""

    handler_id: Required[str]
    """Handler instance identifier."""

    type: Required[str]
    """Instrument category (e.g., 'card', 'tokenized_card')."""

    billing_address: PostalAddressParam
    """Billing address."""

    credential: Credential
    """Base definition for any payment credential."""

    display: Dict[str, object]
    """Display information for the instrument.

    Each payment instrument schema defines its specific display properties, as
    outlined by the payment handler.
    """
