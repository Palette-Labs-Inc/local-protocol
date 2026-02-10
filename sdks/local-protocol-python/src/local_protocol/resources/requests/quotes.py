# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

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
from ...types.requests import quote_create_params
from ...types.payment_param import PaymentParam
from ...types.location_param import LocationParam
from ...types.requests.delivery_quote import DeliveryQuote
from ...types.requests.quote_list_response import QuoteListResponse

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

    def create(
        self,
        request_id: str,
        *,
        id: str,
        currency: str,
        dropoff_estimate: Union[str, datetime],
        dropoff_location: LocationParam,
        nonce: str,
        payment: PaymentParam,
        pickup_estimate: Union[str, datetime],
        pickup_location: LocationParam,
        price: int,
        expires_at: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeliveryQuote:
        """Submit a quote for a delivery request.

        The `nonce` field provides idempotency.

        Args:
          id: Unique quote identifier.

          currency: ISO 4217 currency code.

          dropoff_estimate: Estimated dropoff time (RFC 3339).

          dropoff_location: A location specified by coordinates and/or postal address. At least one must be
              provided.

          nonce: Client-generated idempotency key.

          payment: Payment handlers available for accepting this quote.

          pickup_estimate: Estimated pickup time (RFC 3339).

          pickup_location: A location specified by coordinates and/or postal address. At least one must be
              provided.

          price: Price in minor currency units.

          expires_at: Time when the quote expires (RFC 3339).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return self._post(
            f"/requests/{request_id}/quotes",
            body=maybe_transform(
                {
                    "id": id,
                    "currency": currency,
                    "dropoff_estimate": dropoff_estimate,
                    "dropoff_location": dropoff_location,
                    "nonce": nonce,
                    "payment": payment,
                    "pickup_estimate": pickup_estimate,
                    "pickup_location": pickup_location,
                    "price": price,
                    "expires_at": expires_at,
                },
                quote_create_params.QuoteCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeliveryQuote,
        )

    def retrieve(
        self,
        quote_id: str,
        *,
        request_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeliveryQuote:
        """
        Returns a single quote by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        if not quote_id:
            raise ValueError(f"Expected a non-empty value for `quote_id` but received {quote_id!r}")
        return self._get(
            f"/requests/{request_id}/quotes/{quote_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeliveryQuote,
        )

    def list(
        self,
        request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QuoteListResponse:
        """
        Returns all quotes for a delivery request.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return self._get(
            f"/requests/{request_id}/quotes",
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

    async def create(
        self,
        request_id: str,
        *,
        id: str,
        currency: str,
        dropoff_estimate: Union[str, datetime],
        dropoff_location: LocationParam,
        nonce: str,
        payment: PaymentParam,
        pickup_estimate: Union[str, datetime],
        pickup_location: LocationParam,
        price: int,
        expires_at: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeliveryQuote:
        """Submit a quote for a delivery request.

        The `nonce` field provides idempotency.

        Args:
          id: Unique quote identifier.

          currency: ISO 4217 currency code.

          dropoff_estimate: Estimated dropoff time (RFC 3339).

          dropoff_location: A location specified by coordinates and/or postal address. At least one must be
              provided.

          nonce: Client-generated idempotency key.

          payment: Payment handlers available for accepting this quote.

          pickup_estimate: Estimated pickup time (RFC 3339).

          pickup_location: A location specified by coordinates and/or postal address. At least one must be
              provided.

          price: Price in minor currency units.

          expires_at: Time when the quote expires (RFC 3339).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return await self._post(
            f"/requests/{request_id}/quotes",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "currency": currency,
                    "dropoff_estimate": dropoff_estimate,
                    "dropoff_location": dropoff_location,
                    "nonce": nonce,
                    "payment": payment,
                    "pickup_estimate": pickup_estimate,
                    "pickup_location": pickup_location,
                    "price": price,
                    "expires_at": expires_at,
                },
                quote_create_params.QuoteCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeliveryQuote,
        )

    async def retrieve(
        self,
        quote_id: str,
        *,
        request_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeliveryQuote:
        """
        Returns a single quote by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        if not quote_id:
            raise ValueError(f"Expected a non-empty value for `quote_id` but received {quote_id!r}")
        return await self._get(
            f"/requests/{request_id}/quotes/{quote_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeliveryQuote,
        )

    async def list(
        self,
        request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QuoteListResponse:
        """
        Returns all quotes for a delivery request.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return await self._get(
            f"/requests/{request_id}/quotes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QuoteListResponse,
        )


class QuotesResourceWithRawResponse:
    def __init__(self, quotes: QuotesResource) -> None:
        self._quotes = quotes

        self.create = to_raw_response_wrapper(
            quotes.create,
        )
        self.retrieve = to_raw_response_wrapper(
            quotes.retrieve,
        )
        self.list = to_raw_response_wrapper(
            quotes.list,
        )


class AsyncQuotesResourceWithRawResponse:
    def __init__(self, quotes: AsyncQuotesResource) -> None:
        self._quotes = quotes

        self.create = async_to_raw_response_wrapper(
            quotes.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            quotes.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            quotes.list,
        )


class QuotesResourceWithStreamingResponse:
    def __init__(self, quotes: QuotesResource) -> None:
        self._quotes = quotes

        self.create = to_streamed_response_wrapper(
            quotes.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            quotes.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            quotes.list,
        )


class AsyncQuotesResourceWithStreamingResponse:
    def __init__(self, quotes: AsyncQuotesResource) -> None:
        self._quotes = quotes

        self.create = async_to_streamed_response_wrapper(
            quotes.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            quotes.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            quotes.list,
        )
