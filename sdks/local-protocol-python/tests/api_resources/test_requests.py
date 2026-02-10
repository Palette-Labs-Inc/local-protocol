# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from local_protocol import LocalProtocol, AsyncLocalProtocol
from local_protocol.types import DeliveryRequest, RequestListResponse
from local_protocol._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRequests:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: LocalProtocol) -> None:
        request = client.requests.create(
            id="id",
            dropoff_location={},
            dropoff_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            nonce="nonce",
            pickup_location={},
            pickup_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(DeliveryRequest, request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: LocalProtocol) -> None:
        request = client.requests.create(
            id="id",
            dropoff_location={
                "coordinates": {
                    "latitude": -90,
                    "longitude": -180,
                },
                "postal_address": {
                    "address_country": "address_country",
                    "address_locality": "address_locality",
                    "address_region": "address_region",
                    "extended_address": "extended_address",
                    "first_name": "first_name",
                    "last_name": "last_name",
                    "phone_number": "phone_number",
                    "postal_code": "postal_code",
                    "street_address": "street_address",
                },
            },
            dropoff_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            nonce="nonce",
            pickup_location={
                "coordinates": {
                    "latitude": -90,
                    "longitude": -180,
                },
                "postal_address": {
                    "address_country": "address_country",
                    "address_locality": "address_locality",
                    "address_region": "address_region",
                    "extended_address": "extended_address",
                    "first_name": "first_name",
                    "last_name": "last_name",
                    "phone_number": "phone_number",
                    "postal_code": "postal_code",
                    "street_address": "street_address",
                },
            },
            pickup_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            dropoff_instructions="dropoff_instructions",
            pickup_instructions="pickup_instructions",
        )
        assert_matches_type(DeliveryRequest, request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: LocalProtocol) -> None:
        response = client.requests.with_raw_response.create(
            id="id",
            dropoff_location={},
            dropoff_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            nonce="nonce",
            pickup_location={},
            pickup_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request = response.parse()
        assert_matches_type(DeliveryRequest, request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: LocalProtocol) -> None:
        with client.requests.with_streaming_response.create(
            id="id",
            dropoff_location={},
            dropoff_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            nonce="nonce",
            pickup_location={},
            pickup_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request = response.parse()
            assert_matches_type(DeliveryRequest, request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: LocalProtocol) -> None:
        request = client.requests.retrieve(
            "request_id",
        )
        assert_matches_type(DeliveryRequest, request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: LocalProtocol) -> None:
        response = client.requests.with_raw_response.retrieve(
            "request_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request = response.parse()
        assert_matches_type(DeliveryRequest, request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: LocalProtocol) -> None:
        with client.requests.with_streaming_response.retrieve(
            "request_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request = response.parse()
            assert_matches_type(DeliveryRequest, request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: LocalProtocol) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
            client.requests.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: LocalProtocol) -> None:
        request = client.requests.list()
        assert_matches_type(RequestListResponse, request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LocalProtocol) -> None:
        response = client.requests.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request = response.parse()
        assert_matches_type(RequestListResponse, request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LocalProtocol) -> None:
        with client.requests.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request = response.parse()
            assert_matches_type(RequestListResponse, request, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRequests:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLocalProtocol) -> None:
        request = await async_client.requests.create(
            id="id",
            dropoff_location={},
            dropoff_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            nonce="nonce",
            pickup_location={},
            pickup_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(DeliveryRequest, request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLocalProtocol) -> None:
        request = await async_client.requests.create(
            id="id",
            dropoff_location={
                "coordinates": {
                    "latitude": -90,
                    "longitude": -180,
                },
                "postal_address": {
                    "address_country": "address_country",
                    "address_locality": "address_locality",
                    "address_region": "address_region",
                    "extended_address": "extended_address",
                    "first_name": "first_name",
                    "last_name": "last_name",
                    "phone_number": "phone_number",
                    "postal_code": "postal_code",
                    "street_address": "street_address",
                },
            },
            dropoff_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            nonce="nonce",
            pickup_location={
                "coordinates": {
                    "latitude": -90,
                    "longitude": -180,
                },
                "postal_address": {
                    "address_country": "address_country",
                    "address_locality": "address_locality",
                    "address_region": "address_region",
                    "extended_address": "extended_address",
                    "first_name": "first_name",
                    "last_name": "last_name",
                    "phone_number": "phone_number",
                    "postal_code": "postal_code",
                    "street_address": "street_address",
                },
            },
            pickup_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            dropoff_instructions="dropoff_instructions",
            pickup_instructions="pickup_instructions",
        )
        assert_matches_type(DeliveryRequest, request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLocalProtocol) -> None:
        response = await async_client.requests.with_raw_response.create(
            id="id",
            dropoff_location={},
            dropoff_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            nonce="nonce",
            pickup_location={},
            pickup_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request = await response.parse()
        assert_matches_type(DeliveryRequest, request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLocalProtocol) -> None:
        async with async_client.requests.with_streaming_response.create(
            id="id",
            dropoff_location={},
            dropoff_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            nonce="nonce",
            pickup_location={},
            pickup_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request = await response.parse()
            assert_matches_type(DeliveryRequest, request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLocalProtocol) -> None:
        request = await async_client.requests.retrieve(
            "request_id",
        )
        assert_matches_type(DeliveryRequest, request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLocalProtocol) -> None:
        response = await async_client.requests.with_raw_response.retrieve(
            "request_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request = await response.parse()
        assert_matches_type(DeliveryRequest, request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLocalProtocol) -> None:
        async with async_client.requests.with_streaming_response.retrieve(
            "request_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request = await response.parse()
            assert_matches_type(DeliveryRequest, request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLocalProtocol) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
            await async_client.requests.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLocalProtocol) -> None:
        request = await async_client.requests.list()
        assert_matches_type(RequestListResponse, request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLocalProtocol) -> None:
        response = await async_client.requests.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request = await response.parse()
        assert_matches_type(RequestListResponse, request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLocalProtocol) -> None:
        async with async_client.requests.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request = await response.parse()
            assert_matches_type(RequestListResponse, request, path=["response"])

        assert cast(Any, response.is_closed) is True
