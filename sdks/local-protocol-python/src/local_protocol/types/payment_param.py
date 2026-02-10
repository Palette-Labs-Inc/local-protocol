# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

from .selected_payment_instrument_param import SelectedPaymentInstrumentParam

__all__ = ["PaymentParam"]


class PaymentParam(TypedDict, total=False):
    """Payment configuration containing instruments."""

    instruments: Iterable[SelectedPaymentInstrumentParam]
    """Payment instruments available.

    Each instrument is associated with a handler via handler_id.
    """
