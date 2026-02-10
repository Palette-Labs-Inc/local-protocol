# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .evm_amount import EvmAmount

__all__ = ["EvmAuthCaptureEscrowInstrumentDetails", "Token"]


class Token(BaseModel):
    """EVM token identifier used for auth/capture settlement."""

    decimals: int
    """Token decimals."""

    symbol: str
    """Token symbol (e.g., USDC)."""

    address: Optional[str] = None
    """ERC-20 contract address. Omit for native gas tokens."""


class EvmAuthCaptureEscrowInstrumentDetails(BaseModel):
    token: Token
    """EVM token identifier used for auth/capture settlement."""

    amount: EvmAmount
    """Amount in atomic units.

    Currency chain_id MUST match the instrument chain_id; currency address and
    decimals MUST match token address and decimals.
    """

    authorization_expires_at: datetime
    """Authorization expiration (RFC 3339)."""

    chain_id: int
    """EVM chain id."""

    contract: str
    """Escrow contract address."""

    max_amount: EvmAmount
    """Maximum amount that can be authorized (atomic units).

    Currency chain_id MUST match the instrument chain_id; currency address and
    decimals MUST match token address and decimals.
    """

    nonce: str
    """Unique nonce for payment info hash computation."""

    operator: str
    """Operator address."""

    payer: str
    """Payer address."""

    payment_info_hash: str
    """Hash identifying the on-chain payment authorization."""

    preapproval_expires_at: datetime
    """Pre-approval expiration (RFC 3339)."""

    receiver: str
    """Receiver address for captures."""

    refund_expires_at: datetime
    """Refund expiration (RFC 3339)."""

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
