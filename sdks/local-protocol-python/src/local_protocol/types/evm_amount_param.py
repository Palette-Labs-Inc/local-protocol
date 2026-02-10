# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .evm_currency_param import EvmCurrencyParam

__all__ = ["EvmAmountParam"]


class EvmAmountParam(TypedDict, total=False):
    """Amount denominated in an EVM token. Value is in atomic token units."""

    currency: Required[EvmCurrencyParam]
    """EVM token currency descriptor."""

    value: Required[str]
    """Value in atomic token units as an integer string."""
