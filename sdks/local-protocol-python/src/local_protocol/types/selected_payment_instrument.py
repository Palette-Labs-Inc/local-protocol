# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .payment_instrument import PaymentInstrument
from .selected_payment_instrument_selection_state import SelectedPaymentInstrumentSelectionState

__all__ = ["SelectedPaymentInstrument"]


class SelectedPaymentInstrument(PaymentInstrument, SelectedPaymentInstrumentSelectionState):
    """A payment instrument with selection state."""

    pass
