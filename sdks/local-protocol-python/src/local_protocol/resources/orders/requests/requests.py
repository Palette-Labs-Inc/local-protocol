# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from .quotes import (
    QuotesResource,
    AsyncQuotesResource,
    QuotesResourceWithRawResponse,
    AsyncQuotesResourceWithRawResponse,
    QuotesResourceWithStreamingResponse,
    AsyncQuotesResourceWithStreamingResponse,
)
from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.orders import request_create_params
from ....types.orders.request_create_response import RequestCreateResponse

__all__ = ["RequestsResource", "AsyncRequestsResource"]


class RequestsResource(SyncAPIResource):
    @cached_property
    def quotes(self) -> QuotesResource:
        return QuotesResource(self._client)

    @cached_property
    def with_raw_response(self) -> RequestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/local-protocol-python#accessing-raw-response-data-eg-headers
        """
        return RequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RequestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/local-protocol-python#with_streaming_response
        """
        return RequestsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        id: str,
        intent_id: str,
        items: Iterable[request_create_params.Item],
        nonce: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RequestCreateResponse:
        """Submit a new order request with a cart.

        The `nonce` field provides idempotency.

        Args:
          id: Unique cart identifier.

          intent_id: Shared intent identifier for tracing Request -> Quote -> Order.

          items: Items in the cart.

          nonce: Client-generated idempotency key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/orders/requests",
            body=maybe_transform(
                {
                    "id": id,
                    "intent_id": intent_id,
                    "items": items,
                    "nonce": nonce,
                },
                request_create_params.RequestCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RequestCreateResponse,
        )


class AsyncRequestsResource(AsyncAPIResource):
    @cached_property
    def quotes(self) -> AsyncQuotesResource:
        return AsyncQuotesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRequestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/local-protocol-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRequestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/local-protocol-python#with_streaming_response
        """
        return AsyncRequestsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        id: str,
        intent_id: str,
        items: Iterable[request_create_params.Item],
        nonce: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RequestCreateResponse:
        """Submit a new order request with a cart.

        The `nonce` field provides idempotency.

        Args:
          id: Unique cart identifier.

          intent_id: Shared intent identifier for tracing Request -> Quote -> Order.

          items: Items in the cart.

          nonce: Client-generated idempotency key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/orders/requests",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "intent_id": intent_id,
                    "items": items,
                    "nonce": nonce,
                },
                request_create_params.RequestCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RequestCreateResponse,
        )


class RequestsResourceWithRawResponse:
    def __init__(self, requests: RequestsResource) -> None:
        self._requests = requests

        self.create = to_raw_response_wrapper(
            requests.create,
        )

    @cached_property
    def quotes(self) -> QuotesResourceWithRawResponse:
        return QuotesResourceWithRawResponse(self._requests.quotes)


class AsyncRequestsResourceWithRawResponse:
    def __init__(self, requests: AsyncRequestsResource) -> None:
        self._requests = requests

        self.create = async_to_raw_response_wrapper(
            requests.create,
        )

    @cached_property
    def quotes(self) -> AsyncQuotesResourceWithRawResponse:
        return AsyncQuotesResourceWithRawResponse(self._requests.quotes)


class RequestsResourceWithStreamingResponse:
    def __init__(self, requests: RequestsResource) -> None:
        self._requests = requests

        self.create = to_streamed_response_wrapper(
            requests.create,
        )

    @cached_property
    def quotes(self) -> QuotesResourceWithStreamingResponse:
        return QuotesResourceWithStreamingResponse(self._requests.quotes)


class AsyncRequestsResourceWithStreamingResponse:
    def __init__(self, requests: AsyncRequestsResource) -> None:
        self._requests = requests

        self.create = async_to_streamed_response_wrapper(
            requests.create,
        )

    @cached_property
    def quotes(self) -> AsyncQuotesResourceWithStreamingResponse:
        return AsyncQuotesResourceWithStreamingResponse(self._requests.quotes)
