# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from .quotes import (
    QuotesResource,
    AsyncQuotesResource,
    QuotesResourceWithRawResponse,
    AsyncQuotesResourceWithRawResponse,
    QuotesResourceWithStreamingResponse,
    AsyncQuotesResourceWithStreamingResponse,
)
from ...types import request_create_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.location_param import LocationParam
from ...types.delivery_request import DeliveryRequest
from ...types.request_list_response import RequestListResponse

__all__ = ["RequestsResource", "AsyncRequestsResource"]


class RequestsResource(SyncAPIResource):
    """Create and manage delivery requests."""

    @cached_property
    def quotes(self) -> QuotesResource:
        """Create and read delivery quotes for a request."""
        return QuotesResource(self._client)

    @cached_property
    def with_raw_response(self) -> RequestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Palette-Labs-Inc/local-protocol-python#accessing-raw-response-data-eg-headers
        """
        return RequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RequestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Palette-Labs-Inc/local-protocol-python#with_streaming_response
        """
        return RequestsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        id: str,
        dropoff_location: LocationParam,
        dropoff_time: Union[str, datetime],
        nonce: str,
        pickup_location: LocationParam,
        pickup_time: Union[str, datetime],
        dropoff_instructions: str | Omit = omit,
        pickup_instructions: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeliveryRequest:
        """Submit a new delivery request.

        The `nonce` field provides idempotency.

        Args:
          id: Unique request identifier.

          dropoff_location: A location specified by coordinates and/or postal address. At least one must be
              provided.

          dropoff_time: Requested dropoff time (RFC 3339).

          nonce: Client-generated idempotency key.

          pickup_location: A location specified by coordinates and/or postal address. At least one must be
              provided.

          pickup_time: Requested pickup time (RFC 3339).

          dropoff_instructions: Dropoff directions, access codes, or delivery notes.

          pickup_instructions: Pickup directions, access codes, or handling notes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/requests",
            body=maybe_transform(
                {
                    "id": id,
                    "dropoff_location": dropoff_location,
                    "dropoff_time": dropoff_time,
                    "nonce": nonce,
                    "pickup_location": pickup_location,
                    "pickup_time": pickup_time,
                    "dropoff_instructions": dropoff_instructions,
                    "pickup_instructions": pickup_instructions,
                },
                request_create_params.RequestCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeliveryRequest,
        )

    def retrieve(
        self,
        request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeliveryRequest:
        """
        Returns a single delivery request by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return self._get(
            f"/requests/{request_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeliveryRequest,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RequestListResponse:
        """Returns all delivery requests."""
        return self._get(
            "/requests",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RequestListResponse,
        )


class AsyncRequestsResource(AsyncAPIResource):
    """Create and manage delivery requests."""

    @cached_property
    def quotes(self) -> AsyncQuotesResource:
        """Create and read delivery quotes for a request."""
        return AsyncQuotesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRequestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Palette-Labs-Inc/local-protocol-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRequestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Palette-Labs-Inc/local-protocol-python#with_streaming_response
        """
        return AsyncRequestsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        id: str,
        dropoff_location: LocationParam,
        dropoff_time: Union[str, datetime],
        nonce: str,
        pickup_location: LocationParam,
        pickup_time: Union[str, datetime],
        dropoff_instructions: str | Omit = omit,
        pickup_instructions: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeliveryRequest:
        """Submit a new delivery request.

        The `nonce` field provides idempotency.

        Args:
          id: Unique request identifier.

          dropoff_location: A location specified by coordinates and/or postal address. At least one must be
              provided.

          dropoff_time: Requested dropoff time (RFC 3339).

          nonce: Client-generated idempotency key.

          pickup_location: A location specified by coordinates and/or postal address. At least one must be
              provided.

          pickup_time: Requested pickup time (RFC 3339).

          dropoff_instructions: Dropoff directions, access codes, or delivery notes.

          pickup_instructions: Pickup directions, access codes, or handling notes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/requests",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "dropoff_location": dropoff_location,
                    "dropoff_time": dropoff_time,
                    "nonce": nonce,
                    "pickup_location": pickup_location,
                    "pickup_time": pickup_time,
                    "dropoff_instructions": dropoff_instructions,
                    "pickup_instructions": pickup_instructions,
                },
                request_create_params.RequestCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeliveryRequest,
        )

    async def retrieve(
        self,
        request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeliveryRequest:
        """
        Returns a single delivery request by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return await self._get(
            f"/requests/{request_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeliveryRequest,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RequestListResponse:
        """Returns all delivery requests."""
        return await self._get(
            "/requests",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RequestListResponse,
        )


class RequestsResourceWithRawResponse:
    def __init__(self, requests: RequestsResource) -> None:
        self._requests = requests

        self.create = to_raw_response_wrapper(
            requests.create,
        )
        self.retrieve = to_raw_response_wrapper(
            requests.retrieve,
        )
        self.list = to_raw_response_wrapper(
            requests.list,
        )

    @cached_property
    def quotes(self) -> QuotesResourceWithRawResponse:
        """Create and read delivery quotes for a request."""
        return QuotesResourceWithRawResponse(self._requests.quotes)


class AsyncRequestsResourceWithRawResponse:
    def __init__(self, requests: AsyncRequestsResource) -> None:
        self._requests = requests

        self.create = async_to_raw_response_wrapper(
            requests.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            requests.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            requests.list,
        )

    @cached_property
    def quotes(self) -> AsyncQuotesResourceWithRawResponse:
        """Create and read delivery quotes for a request."""
        return AsyncQuotesResourceWithRawResponse(self._requests.quotes)


class RequestsResourceWithStreamingResponse:
    def __init__(self, requests: RequestsResource) -> None:
        self._requests = requests

        self.create = to_streamed_response_wrapper(
            requests.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            requests.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            requests.list,
        )

    @cached_property
    def quotes(self) -> QuotesResourceWithStreamingResponse:
        """Create and read delivery quotes for a request."""
        return QuotesResourceWithStreamingResponse(self._requests.quotes)


class AsyncRequestsResourceWithStreamingResponse:
    def __init__(self, requests: AsyncRequestsResource) -> None:
        self._requests = requests

        self.create = async_to_streamed_response_wrapper(
            requests.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            requests.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            requests.list,
        )

    @cached_property
    def quotes(self) -> AsyncQuotesResourceWithStreamingResponse:
        """Create and read delivery quotes for a request."""
        return AsyncQuotesResourceWithStreamingResponse(self._requests.quotes)
