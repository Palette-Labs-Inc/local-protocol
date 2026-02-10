# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .postal_address import PostalAddress

__all__ = ["PaymentInstrument", "Credential"]


class Credential(BaseModel):
    """Base definition for any payment credential."""

    type: str
    """Credential type discriminator."""

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class PaymentInstrument(BaseModel):
    """Base definition for any payment instrument."""

    id: str
    """Unique instrument identifier."""

    handler_id: str
    """Handler instance identifier."""

    type: str
    """Instrument category (e.g., 'card', 'tokenized_card')."""

    billing_address: Optional[PostalAddress] = None
    """Billing address."""

    credential: Optional[Credential] = None
    """Base definition for any payment credential."""

    display: Optional[Dict[str, object]] = None
    """Display information for the instrument.

    Each payment instrument schema defines its specific display properties, as
    outlined by the payment handler.
    """
