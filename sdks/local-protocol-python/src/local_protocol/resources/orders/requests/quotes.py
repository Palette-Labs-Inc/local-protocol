# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.orders.requests.order_quote import OrderQuote
from ....types.orders.requests.quote_list_response import QuoteListResponse

__all__ = ["QuotesResource", "AsyncQuotesResource"]


class QuotesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> QuotesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/local-protocol-python#accessing-raw-response-data-eg-headers
        """
        return QuotesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QuotesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/local-protocol-python#with_streaming_response
        """
        return QuotesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        order_quote_id: str,
        *,
        order_request_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrderQuote:
        """
        Returns a single order quote by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not order_request_id:
            raise ValueError(f"Expected a non-empty value for `order_request_id` but received {order_request_id!r}")
        if not order_quote_id:
            raise ValueError(f"Expected a non-empty value for `order_quote_id` but received {order_quote_id!r}")
        return self._get(
            f"/orders/requests/{order_request_id}/quotes/{order_quote_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrderQuote,
        )

    def list(
        self,
        order_request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QuoteListResponse:
        """
        Returns all quotes for an order request.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not order_request_id:
            raise ValueError(f"Expected a non-empty value for `order_request_id` but received {order_request_id!r}")
        return self._get(
            f"/orders/requests/{order_request_id}/quotes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QuoteListResponse,
        )


class AsyncQuotesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncQuotesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/local-protocol-python#accessing-raw-response-data-eg-headers
        """
        return AsyncQuotesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQuotesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/local-protocol-python#with_streaming_response
        """
        return AsyncQuotesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        order_quote_id: str,
        *,
        order_request_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrderQuote:
        """
        Returns a single order quote by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not order_request_id:
            raise ValueError(f"Expected a non-empty value for `order_request_id` but received {order_request_id!r}")
        if not order_quote_id:
            raise ValueError(f"Expected a non-empty value for `order_quote_id` but received {order_quote_id!r}")
        return await self._get(
            f"/orders/requests/{order_request_id}/quotes/{order_quote_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrderQuote,
        )

    async def list(
        self,
        order_request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QuoteListResponse:
        """
        Returns all quotes for an order request.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not order_request_id:
            raise ValueError(f"Expected a non-empty value for `order_request_id` but received {order_request_id!r}")
        return await self._get(
            f"/orders/requests/{order_request_id}/quotes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QuoteListResponse,
        )


class QuotesResourceWithRawResponse:
    def __init__(self, quotes: QuotesResource) -> None:
        self._quotes = quotes

        self.retrieve = to_raw_response_wrapper(
            quotes.retrieve,
        )
        self.list = to_raw_response_wrapper(
            quotes.list,
        )


class AsyncQuotesResourceWithRawResponse:
    def __init__(self, quotes: AsyncQuotesResource) -> None:
        self._quotes = quotes

        self.retrieve = async_to_raw_response_wrapper(
            quotes.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            quotes.list,
        )


class QuotesResourceWithStreamingResponse:
    def __init__(self, quotes: QuotesResource) -> None:
        self._quotes = quotes

        self.retrieve = to_streamed_response_wrapper(
            quotes.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            quotes.list,
        )


class AsyncQuotesResourceWithStreamingResponse:
    def __init__(self, quotes: AsyncQuotesResource) -> None:
        self._quotes = quotes

        self.retrieve = async_to_streamed_response_wrapper(
            quotes.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            quotes.list,
        )
