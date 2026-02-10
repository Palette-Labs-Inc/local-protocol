# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .selected_payment_instrument import SelectedPaymentInstrument

__all__ = ["Payment"]


class Payment(BaseModel):
    """Payment configuration containing instruments."""

    instruments: Optional[List[SelectedPaymentInstrument]] = None
    """Payment instruments available.

    Each instrument is associated with a handler via handler_id.
    """
