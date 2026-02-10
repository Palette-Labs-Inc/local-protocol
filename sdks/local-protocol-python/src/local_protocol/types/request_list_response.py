# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .delivery_request import DeliveryRequest

__all__ = ["RequestListResponse"]

RequestListResponse: TypeAlias = List[DeliveryRequest]
