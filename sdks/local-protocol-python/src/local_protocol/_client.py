# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        orders,
        healthz,
        requests,
        merchants,
        deliveries,
        well_known,
        event_vocabularies,
        payment_instruments,
    )
    from .resources.healthz import HealthzResource, AsyncHealthzResource
    from .resources.merchants import MerchantsResource, AsyncMerchantsResource
    from .resources.deliveries import DeliveriesResource, AsyncDeliveriesResource
    from .resources.well_known import WellKnownResource, AsyncWellKnownResource
    from .resources.orders.orders import OrdersResource, AsyncOrdersResource
    from .resources.requests.requests import RequestsResource, AsyncRequestsResource
    from .resources.event_vocabularies import EventVocabulariesResource, AsyncEventVocabulariesResource
    from .resources.payment_instruments import PaymentInstrumentsResource, AsyncPaymentInstrumentsResource

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "LocalProtocol",
    "AsyncLocalProtocol",
    "Client",
    "AsyncClient",
]


class LocalProtocol(SyncAPIClient):
    # client options
    api_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous LocalProtocol client instance."""
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("LOCAL_PROTOCOL_BASE_URL")
        if base_url is None:
            base_url = f"http://localhost:8000"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def well_known(self) -> WellKnownResource:
        """Discover server capabilities, standards, and endpoints."""
        from .resources.well_known import WellKnownResource

        return WellKnownResource(self)

    @cached_property
    def healthz(self) -> HealthzResource:
        """Check whether the server is currently healthy."""
        from .resources.healthz import HealthzResource

        return HealthzResource(self)

    @cached_property
    def requests(self) -> RequestsResource:
        """Create and manage delivery requests."""
        from .resources.requests import RequestsResource

        return RequestsResource(self)

    @cached_property
    def deliveries(self) -> DeliveriesResource:
        """Accept quotes and manage delivery lifecycle state."""
        from .resources.deliveries import DeliveriesResource

        return DeliveriesResource(self)

    @cached_property
    def merchants(self) -> MerchantsResource:
        """Read merchant profile and denormalized catalog data."""
        from .resources.merchants import MerchantsResource

        return MerchantsResource(self)

    @cached_property
    def orders(self) -> OrdersResource:
        """Create and retrieve orders and order-level requests."""
        from .resources.orders import OrdersResource

        return OrdersResource(self)

    @cached_property
    def event_vocabularies(self) -> EventVocabulariesResource:
        """Retrieve event vocabulary definitions by name."""
        from .resources.event_vocabularies import EventVocabulariesResource

        return EventVocabulariesResource(self)

    @cached_property
    def payment_instruments(self) -> PaymentInstrumentsResource:
        """Register payment instruments and related payment models."""
        from .resources.payment_instruments import PaymentInstrumentsResource

        return PaymentInstrumentsResource(self)

    @cached_property
    def with_raw_response(self) -> LocalProtocolWithRawResponse:
        return LocalProtocolWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LocalProtocolWithStreamedResponse:
        return LocalProtocolWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"} if api_key is not None else {}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=self.api_key if api_key is None else api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncLocalProtocol(AsyncAPIClient):
    # client options
    api_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncLocalProtocol client instance."""
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("LOCAL_PROTOCOL_BASE_URL")
        if base_url is None:
            base_url = f"http://localhost:8000"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def well_known(self) -> AsyncWellKnownResource:
        """Discover server capabilities, standards, and endpoints."""
        from .resources.well_known import AsyncWellKnownResource

        return AsyncWellKnownResource(self)

    @cached_property
    def healthz(self) -> AsyncHealthzResource:
        """Check whether the server is currently healthy."""
        from .resources.healthz import AsyncHealthzResource

        return AsyncHealthzResource(self)

    @cached_property
    def requests(self) -> AsyncRequestsResource:
        """Create and manage delivery requests."""
        from .resources.requests import AsyncRequestsResource

        return AsyncRequestsResource(self)

    @cached_property
    def deliveries(self) -> AsyncDeliveriesResource:
        """Accept quotes and manage delivery lifecycle state."""
        from .resources.deliveries import AsyncDeliveriesResource

        return AsyncDeliveriesResource(self)

    @cached_property
    def merchants(self) -> AsyncMerchantsResource:
        """Read merchant profile and denormalized catalog data."""
        from .resources.merchants import AsyncMerchantsResource

        return AsyncMerchantsResource(self)

    @cached_property
    def orders(self) -> AsyncOrdersResource:
        """Create and retrieve orders and order-level requests."""
        from .resources.orders import AsyncOrdersResource

        return AsyncOrdersResource(self)

    @cached_property
    def event_vocabularies(self) -> AsyncEventVocabulariesResource:
        """Retrieve event vocabulary definitions by name."""
        from .resources.event_vocabularies import AsyncEventVocabulariesResource

        return AsyncEventVocabulariesResource(self)

    @cached_property
    def payment_instruments(self) -> AsyncPaymentInstrumentsResource:
        """Register payment instruments and related payment models."""
        from .resources.payment_instruments import AsyncPaymentInstrumentsResource

        return AsyncPaymentInstrumentsResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncLocalProtocolWithRawResponse:
        return AsyncLocalProtocolWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLocalProtocolWithStreamedResponse:
        return AsyncLocalProtocolWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"} if api_key is not None else {}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=self.api_key if api_key is None else api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class LocalProtocolWithRawResponse:
    _client: LocalProtocol

    def __init__(self, client: LocalProtocol) -> None:
        self._client = client

    @cached_property
    def well_known(self) -> well_known.WellKnownResourceWithRawResponse:
        """Discover server capabilities, standards, and endpoints."""
        from .resources.well_known import WellKnownResourceWithRawResponse

        return WellKnownResourceWithRawResponse(self._client.well_known)

    @cached_property
    def healthz(self) -> healthz.HealthzResourceWithRawResponse:
        """Check whether the server is currently healthy."""
        from .resources.healthz import HealthzResourceWithRawResponse

        return HealthzResourceWithRawResponse(self._client.healthz)

    @cached_property
    def requests(self) -> requests.RequestsResourceWithRawResponse:
        """Create and manage delivery requests."""
        from .resources.requests import RequestsResourceWithRawResponse

        return RequestsResourceWithRawResponse(self._client.requests)

    @cached_property
    def deliveries(self) -> deliveries.DeliveriesResourceWithRawResponse:
        """Accept quotes and manage delivery lifecycle state."""
        from .resources.deliveries import DeliveriesResourceWithRawResponse

        return DeliveriesResourceWithRawResponse(self._client.deliveries)

    @cached_property
    def merchants(self) -> merchants.MerchantsResourceWithRawResponse:
        """Read merchant profile and denormalized catalog data."""
        from .resources.merchants import MerchantsResourceWithRawResponse

        return MerchantsResourceWithRawResponse(self._client.merchants)

    @cached_property
    def orders(self) -> orders.OrdersResourceWithRawResponse:
        """Create and retrieve orders and order-level requests."""
        from .resources.orders import OrdersResourceWithRawResponse

        return OrdersResourceWithRawResponse(self._client.orders)

    @cached_property
    def event_vocabularies(self) -> event_vocabularies.EventVocabulariesResourceWithRawResponse:
        """Retrieve event vocabulary definitions by name."""
        from .resources.event_vocabularies import EventVocabulariesResourceWithRawResponse

        return EventVocabulariesResourceWithRawResponse(self._client.event_vocabularies)

    @cached_property
    def payment_instruments(self) -> payment_instruments.PaymentInstrumentsResourceWithRawResponse:
        """Register payment instruments and related payment models."""
        from .resources.payment_instruments import PaymentInstrumentsResourceWithRawResponse

        return PaymentInstrumentsResourceWithRawResponse(self._client.payment_instruments)


class AsyncLocalProtocolWithRawResponse:
    _client: AsyncLocalProtocol

    def __init__(self, client: AsyncLocalProtocol) -> None:
        self._client = client

    @cached_property
    def well_known(self) -> well_known.AsyncWellKnownResourceWithRawResponse:
        """Discover server capabilities, standards, and endpoints."""
        from .resources.well_known import AsyncWellKnownResourceWithRawResponse

        return AsyncWellKnownResourceWithRawResponse(self._client.well_known)

    @cached_property
    def healthz(self) -> healthz.AsyncHealthzResourceWithRawResponse:
        """Check whether the server is currently healthy."""
        from .resources.healthz import AsyncHealthzResourceWithRawResponse

        return AsyncHealthzResourceWithRawResponse(self._client.healthz)

    @cached_property
    def requests(self) -> requests.AsyncRequestsResourceWithRawResponse:
        """Create and manage delivery requests."""
        from .resources.requests import AsyncRequestsResourceWithRawResponse

        return AsyncRequestsResourceWithRawResponse(self._client.requests)

    @cached_property
    def deliveries(self) -> deliveries.AsyncDeliveriesResourceWithRawResponse:
        """Accept quotes and manage delivery lifecycle state."""
        from .resources.deliveries import AsyncDeliveriesResourceWithRawResponse

        return AsyncDeliveriesResourceWithRawResponse(self._client.deliveries)

    @cached_property
    def merchants(self) -> merchants.AsyncMerchantsResourceWithRawResponse:
        """Read merchant profile and denormalized catalog data."""
        from .resources.merchants import AsyncMerchantsResourceWithRawResponse

        return AsyncMerchantsResourceWithRawResponse(self._client.merchants)

    @cached_property
    def orders(self) -> orders.AsyncOrdersResourceWithRawResponse:
        """Create and retrieve orders and order-level requests."""
        from .resources.orders import AsyncOrdersResourceWithRawResponse

        return AsyncOrdersResourceWithRawResponse(self._client.orders)

    @cached_property
    def event_vocabularies(self) -> event_vocabularies.AsyncEventVocabulariesResourceWithRawResponse:
        """Retrieve event vocabulary definitions by name."""
        from .resources.event_vocabularies import AsyncEventVocabulariesResourceWithRawResponse

        return AsyncEventVocabulariesResourceWithRawResponse(self._client.event_vocabularies)

    @cached_property
    def payment_instruments(self) -> payment_instruments.AsyncPaymentInstrumentsResourceWithRawResponse:
        """Register payment instruments and related payment models."""
        from .resources.payment_instruments import AsyncPaymentInstrumentsResourceWithRawResponse

        return AsyncPaymentInstrumentsResourceWithRawResponse(self._client.payment_instruments)


class LocalProtocolWithStreamedResponse:
    _client: LocalProtocol

    def __init__(self, client: LocalProtocol) -> None:
        self._client = client

    @cached_property
    def well_known(self) -> well_known.WellKnownResourceWithStreamingResponse:
        """Discover server capabilities, standards, and endpoints."""
        from .resources.well_known import WellKnownResourceWithStreamingResponse

        return WellKnownResourceWithStreamingResponse(self._client.well_known)

    @cached_property
    def healthz(self) -> healthz.HealthzResourceWithStreamingResponse:
        """Check whether the server is currently healthy."""
        from .resources.healthz import HealthzResourceWithStreamingResponse

        return HealthzResourceWithStreamingResponse(self._client.healthz)

    @cached_property
    def requests(self) -> requests.RequestsResourceWithStreamingResponse:
        """Create and manage delivery requests."""
        from .resources.requests import RequestsResourceWithStreamingResponse

        return RequestsResourceWithStreamingResponse(self._client.requests)

    @cached_property
    def deliveries(self) -> deliveries.DeliveriesResourceWithStreamingResponse:
        """Accept quotes and manage delivery lifecycle state."""
        from .resources.deliveries import DeliveriesResourceWithStreamingResponse

        return DeliveriesResourceWithStreamingResponse(self._client.deliveries)

    @cached_property
    def merchants(self) -> merchants.MerchantsResourceWithStreamingResponse:
        """Read merchant profile and denormalized catalog data."""
        from .resources.merchants import MerchantsResourceWithStreamingResponse

        return MerchantsResourceWithStreamingResponse(self._client.merchants)

    @cached_property
    def orders(self) -> orders.OrdersResourceWithStreamingResponse:
        """Create and retrieve orders and order-level requests."""
        from .resources.orders import OrdersResourceWithStreamingResponse

        return OrdersResourceWithStreamingResponse(self._client.orders)

    @cached_property
    def event_vocabularies(self) -> event_vocabularies.EventVocabulariesResourceWithStreamingResponse:
        """Retrieve event vocabulary definitions by name."""
        from .resources.event_vocabularies import EventVocabulariesResourceWithStreamingResponse

        return EventVocabulariesResourceWithStreamingResponse(self._client.event_vocabularies)

    @cached_property
    def payment_instruments(self) -> payment_instruments.PaymentInstrumentsResourceWithStreamingResponse:
        """Register payment instruments and related payment models."""
        from .resources.payment_instruments import PaymentInstrumentsResourceWithStreamingResponse

        return PaymentInstrumentsResourceWithStreamingResponse(self._client.payment_instruments)


class AsyncLocalProtocolWithStreamedResponse:
    _client: AsyncLocalProtocol

    def __init__(self, client: AsyncLocalProtocol) -> None:
        self._client = client

    @cached_property
    def well_known(self) -> well_known.AsyncWellKnownResourceWithStreamingResponse:
        """Discover server capabilities, standards, and endpoints."""
        from .resources.well_known import AsyncWellKnownResourceWithStreamingResponse

        return AsyncWellKnownResourceWithStreamingResponse(self._client.well_known)

    @cached_property
    def healthz(self) -> healthz.AsyncHealthzResourceWithStreamingResponse:
        """Check whether the server is currently healthy."""
        from .resources.healthz import AsyncHealthzResourceWithStreamingResponse

        return AsyncHealthzResourceWithStreamingResponse(self._client.healthz)

    @cached_property
    def requests(self) -> requests.AsyncRequestsResourceWithStreamingResponse:
        """Create and manage delivery requests."""
        from .resources.requests import AsyncRequestsResourceWithStreamingResponse

        return AsyncRequestsResourceWithStreamingResponse(self._client.requests)

    @cached_property
    def deliveries(self) -> deliveries.AsyncDeliveriesResourceWithStreamingResponse:
        """Accept quotes and manage delivery lifecycle state."""
        from .resources.deliveries import AsyncDeliveriesResourceWithStreamingResponse

        return AsyncDeliveriesResourceWithStreamingResponse(self._client.deliveries)

    @cached_property
    def merchants(self) -> merchants.AsyncMerchantsResourceWithStreamingResponse:
        """Read merchant profile and denormalized catalog data."""
        from .resources.merchants import AsyncMerchantsResourceWithStreamingResponse

        return AsyncMerchantsResourceWithStreamingResponse(self._client.merchants)

    @cached_property
    def orders(self) -> orders.AsyncOrdersResourceWithStreamingResponse:
        """Create and retrieve orders and order-level requests."""
        from .resources.orders import AsyncOrdersResourceWithStreamingResponse

        return AsyncOrdersResourceWithStreamingResponse(self._client.orders)

    @cached_property
    def event_vocabularies(self) -> event_vocabularies.AsyncEventVocabulariesResourceWithStreamingResponse:
        """Retrieve event vocabulary definitions by name."""
        from .resources.event_vocabularies import AsyncEventVocabulariesResourceWithStreamingResponse

        return AsyncEventVocabulariesResourceWithStreamingResponse(self._client.event_vocabularies)

    @cached_property
    def payment_instruments(self) -> payment_instruments.AsyncPaymentInstrumentsResourceWithStreamingResponse:
        """Register payment instruments and related payment models."""
        from .resources.payment_instruments import AsyncPaymentInstrumentsResourceWithStreamingResponse

        return AsyncPaymentInstrumentsResourceWithStreamingResponse(self._client.payment_instruments)


Client = LocalProtocol

AsyncClient = AsyncLocalProtocol
