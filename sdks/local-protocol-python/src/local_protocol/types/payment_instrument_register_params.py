# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .evm_amount_param import EvmAmountParam
from .postal_address_param import PostalAddressParam

__all__ = ["PaymentInstrumentRegisterParams", "Token", "Credential"]


class PaymentInstrumentRegisterParams(TypedDict, total=False):
    id: Required[str]
    """Unique instrument identifier."""

    token: Required[Token]
    """EVM token identifier used for auth/capture settlement."""

    amount: Required[EvmAmountParam]
    """Amount in atomic units.

    Currency chain_id MUST match the instrument chain_id; currency address and
    decimals MUST match token address and decimals.
    """

    authorization_expires_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Authorization expiration (RFC 3339)."""

    chain_id: Required[int]
    """EVM chain id."""

    contract: Required[str]
    """Escrow contract address."""

    handler_id: Required[str]
    """Handler instance identifier."""

    max_amount: Required[EvmAmountParam]
    """Maximum amount that can be authorized (atomic units).

    Currency chain_id MUST match the instrument chain_id; currency address and
    decimals MUST match token address and decimals.
    """

    nonce: Required[str]
    """Unique nonce for payment info hash computation."""

    operator: Required[str]
    """Operator address."""

    payer: Required[str]
    """Payer address."""

    payment_info_hash: Required[str]
    """Hash identifying the on-chain payment authorization."""

    preapproval_expires_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Pre-approval expiration (RFC 3339)."""

    receiver: Required[str]
    """Receiver address for captures."""

    refund_expires_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Refund expiration (RFC 3339)."""

    type: Required[Literal["evm_auth_capture_escrow"]]

    billing_address: PostalAddressParam
    """Billing address."""

    credential: Credential
    """Base definition for any payment credential."""

    display: Dict[str, object]
    """Display information for the instrument.

    Each payment instrument schema defines its specific display properties, as
    outlined by the payment handler.
    """


class Token(TypedDict, total=False):
    """EVM token identifier used for auth/capture settlement."""

    decimals: Required[int]
    """Token decimals."""

    symbol: Required[str]
    """Token symbol (e.g., USDC)."""

    address: str
    """ERC-20 contract address. Omit for native gas tokens."""


class CredentialTyped(TypedDict, total=False):
    """Base definition for any payment credential."""

    type: Required[str]
    """Credential type discriminator."""


Credential: TypeAlias = Union[CredentialTyped, Dict[str, object]]
