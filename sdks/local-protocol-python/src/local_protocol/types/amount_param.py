# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

from .evm_currency_param import EvmCurrencyParam

__all__ = ["AmountParam", "Currency", "CurrencyFiatCurrency"]


class CurrencyFiatCurrency(TypedDict, total=False):
    """Fiat currency descriptor."""

    symbol: Required[str]
    """ISO 4217 currency code (e.g., 'USD', 'EUR', 'JPY')."""


Currency: TypeAlias = Union[CurrencyFiatCurrency, EvmCurrencyParam]


class AmountParam(TypedDict, total=False):
    """Amount with explicit currency.

    Value is always in minor units (e.g., cents for USD).
    """

    currency: Required[Currency]
    """Currency descriptor (fiat or EVM token)."""

    value: Required[str]
    """Value in minor currency units as an integer string."""
