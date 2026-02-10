# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from local_protocol import LocalProtocol, AsyncLocalProtocol
from local_protocol.types.orders.requests import OrderQuote, QuoteListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestQuotes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: LocalProtocol) -> None:
        quote = client.orders.requests.quotes.retrieve(
            order_quote_id="order_quote_id",
            order_request_id="order_request_id",
        )
        assert_matches_type(OrderQuote, quote, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: LocalProtocol) -> None:
        response = client.orders.requests.quotes.with_raw_response.retrieve(
            order_quote_id="order_quote_id",
            order_request_id="order_request_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quote = response.parse()
        assert_matches_type(OrderQuote, quote, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: LocalProtocol) -> None:
        with client.orders.requests.quotes.with_streaming_response.retrieve(
            order_quote_id="order_quote_id",
            order_request_id="order_request_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quote = response.parse()
            assert_matches_type(OrderQuote, quote, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: LocalProtocol) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `order_request_id` but received ''"):
            client.orders.requests.quotes.with_raw_response.retrieve(
                order_quote_id="order_quote_id",
                order_request_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `order_quote_id` but received ''"):
            client.orders.requests.quotes.with_raw_response.retrieve(
                order_quote_id="",
                order_request_id="order_request_id",
            )

    @parametrize
    def test_method_list(self, client: LocalProtocol) -> None:
        quote = client.orders.requests.quotes.list(
            "order_request_id",
        )
        assert_matches_type(QuoteListResponse, quote, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: LocalProtocol) -> None:
        response = client.orders.requests.quotes.with_raw_response.list(
            "order_request_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quote = response.parse()
        assert_matches_type(QuoteListResponse, quote, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: LocalProtocol) -> None:
        with client.orders.requests.quotes.with_streaming_response.list(
            "order_request_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quote = response.parse()
            assert_matches_type(QuoteListResponse, quote, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: LocalProtocol) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `order_request_id` but received ''"):
            client.orders.requests.quotes.with_raw_response.list(
                "",
            )


class TestAsyncQuotes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLocalProtocol) -> None:
        quote = await async_client.orders.requests.quotes.retrieve(
            order_quote_id="order_quote_id",
            order_request_id="order_request_id",
        )
        assert_matches_type(OrderQuote, quote, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLocalProtocol) -> None:
        response = await async_client.orders.requests.quotes.with_raw_response.retrieve(
            order_quote_id="order_quote_id",
            order_request_id="order_request_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quote = await response.parse()
        assert_matches_type(OrderQuote, quote, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLocalProtocol) -> None:
        async with async_client.orders.requests.quotes.with_streaming_response.retrieve(
            order_quote_id="order_quote_id",
            order_request_id="order_request_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quote = await response.parse()
            assert_matches_type(OrderQuote, quote, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLocalProtocol) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `order_request_id` but received ''"):
            await async_client.orders.requests.quotes.with_raw_response.retrieve(
                order_quote_id="order_quote_id",
                order_request_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `order_quote_id` but received ''"):
            await async_client.orders.requests.quotes.with_raw_response.retrieve(
                order_quote_id="",
                order_request_id="order_request_id",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncLocalProtocol) -> None:
        quote = await async_client.orders.requests.quotes.list(
            "order_request_id",
        )
        assert_matches_type(QuoteListResponse, quote, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLocalProtocol) -> None:
        response = await async_client.orders.requests.quotes.with_raw_response.list(
            "order_request_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quote = await response.parse()
        assert_matches_type(QuoteListResponse, quote, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLocalProtocol) -> None:
        async with async_client.orders.requests.quotes.with_streaming_response.list(
            "order_request_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quote = await response.parse()
            assert_matches_type(QuoteListResponse, quote, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncLocalProtocol) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `order_request_id` but received ''"):
            await async_client.orders.requests.quotes.with_raw_response.list(
                "",
            )
