# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .._models import BaseModel
from .evm_currency import EvmCurrency

__all__ = ["Amount", "Currency", "CurrencyFiatCurrency"]


class CurrencyFiatCurrency(BaseModel):
    """Fiat currency descriptor."""

    symbol: str
    """ISO 4217 currency code (e.g., 'USD', 'EUR', 'JPY')."""


Currency: TypeAlias = Union[CurrencyFiatCurrency, EvmCurrency]


class Amount(BaseModel):
    """Amount with explicit currency.

    Value is always in minor units (e.g., cents for USD).
    """

    currency: Currency
    """Currency descriptor (fiat or EVM token)."""

    value: str
    """Value in minor currency units as an integer string."""
