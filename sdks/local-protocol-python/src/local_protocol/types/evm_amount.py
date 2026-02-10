# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .evm_currency import EvmCurrency

__all__ = ["EvmAmount"]


class EvmAmount(BaseModel):
    """Amount denominated in an EVM token. Value is in atomic token units."""

    currency: EvmCurrency
    """EVM token currency descriptor."""

    value: str
    """Value in atomic token units as an integer string."""
