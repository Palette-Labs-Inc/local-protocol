# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .order_quote import OrderQuote

__all__ = ["QuoteListResponse"]

QuoteListResponse: TypeAlias = List[OrderQuote]
