# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.event_vocabulary_retrieve_response import EventVocabularyRetrieveResponse

__all__ = ["EventVocabulariesResource", "AsyncEventVocabulariesResource"]


class EventVocabulariesResource(SyncAPIResource):
    """Retrieve event vocabulary definitions by name."""

    @cached_property
    def with_raw_response(self) -> EventVocabulariesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Palette-Labs-Inc/local-protocol-python#accessing-raw-response-data-eg-headers
        """
        return EventVocabulariesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventVocabulariesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Palette-Labs-Inc/local-protocol-python#with_streaming_response
        """
        return EventVocabulariesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventVocabularyRetrieveResponse:
        """
        Returns a delivery event vocabulary by name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._get(
            f"/event-vocabularies/{name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventVocabularyRetrieveResponse,
        )


class AsyncEventVocabulariesResource(AsyncAPIResource):
    """Retrieve event vocabulary definitions by name."""

    @cached_property
    def with_raw_response(self) -> AsyncEventVocabulariesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Palette-Labs-Inc/local-protocol-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEventVocabulariesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventVocabulariesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Palette-Labs-Inc/local-protocol-python#with_streaming_response
        """
        return AsyncEventVocabulariesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventVocabularyRetrieveResponse:
        """
        Returns a delivery event vocabulary by name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._get(
            f"/event-vocabularies/{name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventVocabularyRetrieveResponse,
        )


class EventVocabulariesResourceWithRawResponse:
    def __init__(self, event_vocabularies: EventVocabulariesResource) -> None:
        self._event_vocabularies = event_vocabularies

        self.retrieve = to_raw_response_wrapper(
            event_vocabularies.retrieve,
        )


class AsyncEventVocabulariesResourceWithRawResponse:
    def __init__(self, event_vocabularies: AsyncEventVocabulariesResource) -> None:
        self._event_vocabularies = event_vocabularies

        self.retrieve = async_to_raw_response_wrapper(
            event_vocabularies.retrieve,
        )


class EventVocabulariesResourceWithStreamingResponse:
    def __init__(self, event_vocabularies: EventVocabulariesResource) -> None:
        self._event_vocabularies = event_vocabularies

        self.retrieve = to_streamed_response_wrapper(
            event_vocabularies.retrieve,
        )


class AsyncEventVocabulariesResourceWithStreamingResponse:
    def __init__(self, event_vocabularies: AsyncEventVocabulariesResource) -> None:
        self._event_vocabularies = event_vocabularies

        self.retrieve = async_to_streamed_response_wrapper(
            event_vocabularies.retrieve,
        )
