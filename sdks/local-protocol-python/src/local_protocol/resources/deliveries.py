# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import delivery_create_params, delivery_update_event_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.delivery import Delivery
from ..types.delivery_list_response import DeliveryListResponse

__all__ = ["DeliveriesResource", "AsyncDeliveriesResource"]


class DeliveriesResource(SyncAPIResource):
    """Accept quotes and manage delivery lifecycle state."""

    @cached_property
    def with_raw_response(self) -> DeliveriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Palette-Labs-Inc/local-protocol-python#accessing-raw-response-data-eg-headers
        """
        return DeliveriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DeliveriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Palette-Labs-Inc/local-protocol-python#with_streaming_response
        """
        return DeliveriesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        nonce: str,
        quote_id: str,
        request_id: str,
        event_vocabulary: str | Omit = omit,
        webhook_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Delivery:
        """Accept a quote and create a delivery.

        The `nonce` field provides idempotency.

        Args:
          nonce: Client-generated idempotency key.

          quote_id: The accepted quote.

          request_id: The delivery request to fulfill.

          event_vocabulary: Event vocabulary standard to use.

          webhook_url: Optional URL to receive delivery event webhook notifications.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/deliveries",
            body=maybe_transform(
                {
                    "nonce": nonce,
                    "quote_id": quote_id,
                    "request_id": request_id,
                    "event_vocabulary": event_vocabulary,
                    "webhook_url": webhook_url,
                },
                delivery_create_params.DeliveryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Delivery,
        )

    def retrieve(
        self,
        delivery_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Delivery:
        """
        Returns a single delivery by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not delivery_id:
            raise ValueError(f"Expected a non-empty value for `delivery_id` but received {delivery_id!r}")
        return self._get(
            f"/deliveries/{delivery_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Delivery,
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
    ) -> DeliveryListResponse:
        """Returns all deliveries."""
        return self._get(
            "/deliveries",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeliveryListResponse,
        )

    def update_event(
        self,
        delivery_id: str,
        *,
        event: str,
        event_description: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Delivery:
        """Transition a delivery to a new event state.

        If a webhook URL was registered, the
        server pushes an event notification in the background.

        Args:
          event: Event identifier from the delivery's event vocabulary.

          event_description: Human-readable event description.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not delivery_id:
            raise ValueError(f"Expected a non-empty value for `delivery_id` but received {delivery_id!r}")
        return self._patch(
            f"/deliveries/{delivery_id}/event",
            body=maybe_transform(
                {
                    "event": event,
                    "event_description": event_description,
                },
                delivery_update_event_params.DeliveryUpdateEventParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Delivery,
        )


class AsyncDeliveriesResource(AsyncAPIResource):
    """Accept quotes and manage delivery lifecycle state."""

    @cached_property
    def with_raw_response(self) -> AsyncDeliveriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Palette-Labs-Inc/local-protocol-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDeliveriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDeliveriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Palette-Labs-Inc/local-protocol-python#with_streaming_response
        """
        return AsyncDeliveriesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        nonce: str,
        quote_id: str,
        request_id: str,
        event_vocabulary: str | Omit = omit,
        webhook_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Delivery:
        """Accept a quote and create a delivery.

        The `nonce` field provides idempotency.

        Args:
          nonce: Client-generated idempotency key.

          quote_id: The accepted quote.

          request_id: The delivery request to fulfill.

          event_vocabulary: Event vocabulary standard to use.

          webhook_url: Optional URL to receive delivery event webhook notifications.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/deliveries",
            body=await async_maybe_transform(
                {
                    "nonce": nonce,
                    "quote_id": quote_id,
                    "request_id": request_id,
                    "event_vocabulary": event_vocabulary,
                    "webhook_url": webhook_url,
                },
                delivery_create_params.DeliveryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Delivery,
        )

    async def retrieve(
        self,
        delivery_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Delivery:
        """
        Returns a single delivery by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not delivery_id:
            raise ValueError(f"Expected a non-empty value for `delivery_id` but received {delivery_id!r}")
        return await self._get(
            f"/deliveries/{delivery_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Delivery,
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
    ) -> DeliveryListResponse:
        """Returns all deliveries."""
        return await self._get(
            "/deliveries",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeliveryListResponse,
        )

    async def update_event(
        self,
        delivery_id: str,
        *,
        event: str,
        event_description: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Delivery:
        """Transition a delivery to a new event state.

        If a webhook URL was registered, the
        server pushes an event notification in the background.

        Args:
          event: Event identifier from the delivery's event vocabulary.

          event_description: Human-readable event description.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not delivery_id:
            raise ValueError(f"Expected a non-empty value for `delivery_id` but received {delivery_id!r}")
        return await self._patch(
            f"/deliveries/{delivery_id}/event",
            body=await async_maybe_transform(
                {
                    "event": event,
                    "event_description": event_description,
                },
                delivery_update_event_params.DeliveryUpdateEventParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Delivery,
        )


class DeliveriesResourceWithRawResponse:
    def __init__(self, deliveries: DeliveriesResource) -> None:
        self._deliveries = deliveries

        self.create = to_raw_response_wrapper(
            deliveries.create,
        )
        self.retrieve = to_raw_response_wrapper(
            deliveries.retrieve,
        )
        self.list = to_raw_response_wrapper(
            deliveries.list,
        )
        self.update_event = to_raw_response_wrapper(
            deliveries.update_event,
        )


class AsyncDeliveriesResourceWithRawResponse:
    def __init__(self, deliveries: AsyncDeliveriesResource) -> None:
        self._deliveries = deliveries

        self.create = async_to_raw_response_wrapper(
            deliveries.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            deliveries.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            deliveries.list,
        )
        self.update_event = async_to_raw_response_wrapper(
            deliveries.update_event,
        )


class DeliveriesResourceWithStreamingResponse:
    def __init__(self, deliveries: DeliveriesResource) -> None:
        self._deliveries = deliveries

        self.create = to_streamed_response_wrapper(
            deliveries.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            deliveries.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            deliveries.list,
        )
        self.update_event = to_streamed_response_wrapper(
            deliveries.update_event,
        )


class AsyncDeliveriesResourceWithStreamingResponse:
    def __init__(self, deliveries: AsyncDeliveriesResource) -> None:
        self._deliveries = deliveries

        self.create = async_to_streamed_response_wrapper(
            deliveries.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            deliveries.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            deliveries.list,
        )
        self.update_event = async_to_streamed_response_wrapper(
            deliveries.update_event,
        )
