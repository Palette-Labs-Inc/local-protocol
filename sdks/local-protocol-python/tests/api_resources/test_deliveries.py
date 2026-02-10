# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from local_protocol import LocalProtocol, AsyncLocalProtocol
from local_protocol.types import Delivery, DeliveryListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDeliveries:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: LocalProtocol) -> None:
        delivery = client.deliveries.create(
            nonce="nonce",
            quote_id="quote_id",
            request_id="request_id",
        )
        assert_matches_type(Delivery, delivery, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: LocalProtocol) -> None:
        delivery = client.deliveries.create(
            nonce="nonce",
            quote_id="quote_id",
            request_id="request_id",
            event_vocabulary="event_vocabulary",
            webhook_url="webhook_url",
        )
        assert_matches_type(Delivery, delivery, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: LocalProtocol) -> None:
        response = client.deliveries.with_raw_response.create(
            nonce="nonce",
            quote_id="quote_id",
            request_id="request_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delivery = response.parse()
        assert_matches_type(Delivery, delivery, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: LocalProtocol) -> None:
        with client.deliveries.with_streaming_response.create(
            nonce="nonce",
            quote_id="quote_id",
            request_id="request_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delivery = response.parse()
            assert_matches_type(Delivery, delivery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: LocalProtocol) -> None:
        delivery = client.deliveries.retrieve(
            "delivery_id",
        )
        assert_matches_type(Delivery, delivery, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: LocalProtocol) -> None:
        response = client.deliveries.with_raw_response.retrieve(
            "delivery_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delivery = response.parse()
        assert_matches_type(Delivery, delivery, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: LocalProtocol) -> None:
        with client.deliveries.with_streaming_response.retrieve(
            "delivery_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delivery = response.parse()
            assert_matches_type(Delivery, delivery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: LocalProtocol) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `delivery_id` but received ''"):
            client.deliveries.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: LocalProtocol) -> None:
        delivery = client.deliveries.list()
        assert_matches_type(DeliveryListResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LocalProtocol) -> None:
        response = client.deliveries.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delivery = response.parse()
        assert_matches_type(DeliveryListResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LocalProtocol) -> None:
        with client.deliveries.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delivery = response.parse()
            assert_matches_type(DeliveryListResponse, delivery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_event(self, client: LocalProtocol) -> None:
        delivery = client.deliveries.update_event(
            delivery_id="delivery_id",
            event="event",
            event_description="event_description",
        )
        assert_matches_type(Delivery, delivery, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_event(self, client: LocalProtocol) -> None:
        response = client.deliveries.with_raw_response.update_event(
            delivery_id="delivery_id",
            event="event",
            event_description="event_description",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delivery = response.parse()
        assert_matches_type(Delivery, delivery, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_event(self, client: LocalProtocol) -> None:
        with client.deliveries.with_streaming_response.update_event(
            delivery_id="delivery_id",
            event="event",
            event_description="event_description",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delivery = response.parse()
            assert_matches_type(Delivery, delivery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_event(self, client: LocalProtocol) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `delivery_id` but received ''"):
            client.deliveries.with_raw_response.update_event(
                delivery_id="",
                event="event",
                event_description="event_description",
            )


class TestAsyncDeliveries:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLocalProtocol) -> None:
        delivery = await async_client.deliveries.create(
            nonce="nonce",
            quote_id="quote_id",
            request_id="request_id",
        )
        assert_matches_type(Delivery, delivery, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLocalProtocol) -> None:
        delivery = await async_client.deliveries.create(
            nonce="nonce",
            quote_id="quote_id",
            request_id="request_id",
            event_vocabulary="event_vocabulary",
            webhook_url="webhook_url",
        )
        assert_matches_type(Delivery, delivery, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLocalProtocol) -> None:
        response = await async_client.deliveries.with_raw_response.create(
            nonce="nonce",
            quote_id="quote_id",
            request_id="request_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delivery = await response.parse()
        assert_matches_type(Delivery, delivery, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLocalProtocol) -> None:
        async with async_client.deliveries.with_streaming_response.create(
            nonce="nonce",
            quote_id="quote_id",
            request_id="request_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delivery = await response.parse()
            assert_matches_type(Delivery, delivery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLocalProtocol) -> None:
        delivery = await async_client.deliveries.retrieve(
            "delivery_id",
        )
        assert_matches_type(Delivery, delivery, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLocalProtocol) -> None:
        response = await async_client.deliveries.with_raw_response.retrieve(
            "delivery_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delivery = await response.parse()
        assert_matches_type(Delivery, delivery, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLocalProtocol) -> None:
        async with async_client.deliveries.with_streaming_response.retrieve(
            "delivery_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delivery = await response.parse()
            assert_matches_type(Delivery, delivery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLocalProtocol) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `delivery_id` but received ''"):
            await async_client.deliveries.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLocalProtocol) -> None:
        delivery = await async_client.deliveries.list()
        assert_matches_type(DeliveryListResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLocalProtocol) -> None:
        response = await async_client.deliveries.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delivery = await response.parse()
        assert_matches_type(DeliveryListResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLocalProtocol) -> None:
        async with async_client.deliveries.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delivery = await response.parse()
            assert_matches_type(DeliveryListResponse, delivery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_event(self, async_client: AsyncLocalProtocol) -> None:
        delivery = await async_client.deliveries.update_event(
            delivery_id="delivery_id",
            event="event",
            event_description="event_description",
        )
        assert_matches_type(Delivery, delivery, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_event(self, async_client: AsyncLocalProtocol) -> None:
        response = await async_client.deliveries.with_raw_response.update_event(
            delivery_id="delivery_id",
            event="event",
            event_description="event_description",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delivery = await response.parse()
        assert_matches_type(Delivery, delivery, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_event(self, async_client: AsyncLocalProtocol) -> None:
        async with async_client.deliveries.with_streaming_response.update_event(
            delivery_id="delivery_id",
            event="event",
            event_description="event_description",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delivery = await response.parse()
            assert_matches_type(Delivery, delivery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_event(self, async_client: AsyncLocalProtocol) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `delivery_id` but received ''"):
            await async_client.deliveries.with_raw_response.update_event(
                delivery_id="",
                event="event",
                event_description="event_description",
            )
