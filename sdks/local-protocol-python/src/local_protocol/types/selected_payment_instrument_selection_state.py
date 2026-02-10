# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["SelectedPaymentInstrumentSelectionState"]


class SelectedPaymentInstrumentSelectionState(BaseModel):
    selected: Optional[bool] = None
    """Whether this instrument is selected by the user."""
