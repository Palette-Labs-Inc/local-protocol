# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from local_protocol import LocalProtocol, AsyncLocalProtocol
from local_protocol.types import Order

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: LocalProtocol) -> None:
        order = client.orders.create(
            nonce="nonce",
            order_quote_id="order_quote_id",
            order_request_id="order_request_id",
            payment_instrument_id="payment_instrument_id",
        )
        assert_matches_type(Order, order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: LocalProtocol) -> None:
        response = client.orders.with_raw_response.create(
            nonce="nonce",
            order_quote_id="order_quote_id",
            order_request_id="order_request_id",
            payment_instrument_id="payment_instrument_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert_matches_type(Order, order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: LocalProtocol) -> None:
        with client.orders.with_streaming_response.create(
            nonce="nonce",
            order_quote_id="order_quote_id",
            order_request_id="order_request_id",
            payment_instrument_id="payment_instrument_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = response.parse()
            assert_matches_type(Order, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: LocalProtocol) -> None:
        order = client.orders.retrieve(
            "order_id",
        )
        assert_matches_type(Order, order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: LocalProtocol) -> None:
        response = client.orders.with_raw_response.retrieve(
            "order_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert_matches_type(Order, order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: LocalProtocol) -> None:
        with client.orders.with_streaming_response.retrieve(
            "order_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = response.parse()
            assert_matches_type(Order, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: LocalProtocol) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `order_id` but received ''"):
            client.orders.with_raw_response.retrieve(
                "",
            )


class TestAsyncOrders:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLocalProtocol) -> None:
        order = await async_client.orders.create(
            nonce="nonce",
            order_quote_id="order_quote_id",
            order_request_id="order_request_id",
            payment_instrument_id="payment_instrument_id",
        )
        assert_matches_type(Order, order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLocalProtocol) -> None:
        response = await async_client.orders.with_raw_response.create(
            nonce="nonce",
            order_quote_id="order_quote_id",
            order_request_id="order_request_id",
            payment_instrument_id="payment_instrument_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert_matches_type(Order, order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLocalProtocol) -> None:
        async with async_client.orders.with_streaming_response.create(
            nonce="nonce",
            order_quote_id="order_quote_id",
            order_request_id="order_request_id",
            payment_instrument_id="payment_instrument_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert_matches_type(Order, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLocalProtocol) -> None:
        order = await async_client.orders.retrieve(
            "order_id",
        )
        assert_matches_type(Order, order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLocalProtocol) -> None:
        response = await async_client.orders.with_raw_response.retrieve(
            "order_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert_matches_type(Order, order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLocalProtocol) -> None:
        async with async_client.orders.with_streaming_response.retrieve(
            "order_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert_matches_type(Order, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLocalProtocol) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `order_id` but received ''"):
            await async_client.orders.with_raw_response.retrieve(
                "",
            )
