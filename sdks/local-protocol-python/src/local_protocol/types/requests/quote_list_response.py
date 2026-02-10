# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .delivery_quote import DeliveryQuote

__all__ = ["QuoteListResponse"]

QuoteListResponse: TypeAlias = List[DeliveryQuote]
