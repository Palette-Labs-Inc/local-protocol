# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["EvmCurrency"]


class EvmCurrency(BaseModel):
    """EVM token currency descriptor."""

    address: str
    """Token contract address."""

    chain_id: int
    """EVM chain id."""

    decimals: int
    """Decimal places for the token."""
