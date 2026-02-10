# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["EvmCurrencyParam"]


class EvmCurrencyParam(TypedDict, total=False):
    """EVM token currency descriptor."""

    address: Required[str]
    """Token contract address."""

    chain_id: Required[int]
    """EVM chain id."""

    decimals: Required[int]
    """Decimal places for the token."""
