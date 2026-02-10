# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .payment_instrument_param import PaymentInstrumentParam
from .selected_payment_instrument_selection_state_param import SelectedPaymentInstrumentSelectionStateParam

__all__ = ["SelectedPaymentInstrumentParam"]


class SelectedPaymentInstrumentParam(PaymentInstrumentParam, SelectedPaymentInstrumentSelectionStateParam, total=False):
    """A payment instrument with selection state."""

    pass
