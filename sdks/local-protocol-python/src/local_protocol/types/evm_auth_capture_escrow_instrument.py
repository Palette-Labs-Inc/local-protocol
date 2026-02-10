# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .payment_instrument import PaymentInstrument
from .evm_auth_capture_escrow_instrument_details import EvmAuthCaptureEscrowInstrumentDetails

__all__ = ["EvmAuthCaptureEscrowInstrument"]


class EvmAuthCaptureEscrowInstrument(PaymentInstrument, EvmAuthCaptureEscrowInstrumentDetails):
    """Payment instrument for auth/capture escrow on EVM chains."""

    type: Literal["evm_auth_capture_escrow"]  # type: ignore
