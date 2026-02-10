# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from local_protocol import LocalProtocol, AsyncLocalProtocol
from local_protocol.types.orders import RequestCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRequests:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: LocalProtocol) -> None:
        request = client.orders.requests.create(
            id="id",
            intent_id="intent_id",
            items=[
                {
                    "id": "id",
                    "quantity": 1,
                }
            ],
            nonce="nonce",
        )
        assert_matches_type(RequestCreateResponse, request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: LocalProtocol) -> None:
        response = client.orders.requests.with_raw_response.create(
            id="id",
            intent_id="intent_id",
            items=[
                {
                    "id": "id",
                    "quantity": 1,
                }
            ],
            nonce="nonce",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request = response.parse()
        assert_matches_type(RequestCreateResponse, request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: LocalProtocol) -> None:
        with client.orders.requests.with_streaming_response.create(
            id="id",
            intent_id="intent_id",
            items=[
                {
                    "id": "id",
                    "quantity": 1,
                }
            ],
            nonce="nonce",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request = response.parse()
            assert_matches_type(RequestCreateResponse, request, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRequests:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLocalProtocol) -> None:
        request = await async_client.orders.requests.create(
            id="id",
            intent_id="intent_id",
            items=[
                {
                    "id": "id",
                    "quantity": 1,
                }
            ],
            nonce="nonce",
        )
        assert_matches_type(RequestCreateResponse, request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLocalProtocol) -> None:
        response = await async_client.orders.requests.with_raw_response.create(
            id="id",
            intent_id="intent_id",
            items=[
                {
                    "id": "id",
                    "quantity": 1,
                }
            ],
            nonce="nonce",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request = await response.parse()
        assert_matches_type(RequestCreateResponse, request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLocalProtocol) -> None:
        async with async_client.orders.requests.with_streaming_response.create(
            id="id",
            intent_id="intent_id",
            items=[
                {
                    "id": "id",
                    "quantity": 1,
                }
            ],
            nonce="nonce",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request = await response.parse()
            assert_matches_type(RequestCreateResponse, request, path=["response"])

        assert cast(Any, response.is_closed) is True
