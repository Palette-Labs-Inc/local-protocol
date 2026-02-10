# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from local_protocol import LocalProtocol, AsyncLocalProtocol
from local_protocol._utils import parse_datetime
from local_protocol.types.requests import DeliveryQuote, QuoteListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestQuotes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: LocalProtocol) -> None:
        quote = client.requests.quotes.create(
            request_id="request_id",
            id="id",
            currency="SEW",
            dropoff_estimate=parse_datetime("2019-12-27T18:11:19.117Z"),
            dropoff_location={},
            nonce="nonce",
            payment={},
            pickup_estimate=parse_datetime("2019-12-27T18:11:19.117Z"),
            pickup_location={},
            price=0,
        )
        assert_matches_type(DeliveryQuote, quote, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: LocalProtocol) -> None:
        quote = client.requests.quotes.create(
            request_id="request_id",
            id="id",
            currency="SEW",
            dropoff_estimate=parse_datetime("2019-12-27T18:11:19.117Z"),
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
            nonce="nonce",
            payment={
                "instruments": [
                    {
                        "id": "id",
                        "handler_id": "handler_id",
                        "type": "type",
                        "billing_address": {
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
                        "credential": {"type": "type"},
                        "display": {},
                        "selected": True,
                    }
                ]
            },
            pickup_estimate=parse_datetime("2019-12-27T18:11:19.117Z"),
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
            price=0,
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(DeliveryQuote, quote, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: LocalProtocol) -> None:
        response = client.requests.quotes.with_raw_response.create(
            request_id="request_id",
            id="id",
            currency="SEW",
            dropoff_estimate=parse_datetime("2019-12-27T18:11:19.117Z"),
            dropoff_location={},
            nonce="nonce",
            payment={},
            pickup_estimate=parse_datetime("2019-12-27T18:11:19.117Z"),
            pickup_location={},
            price=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quote = response.parse()
        assert_matches_type(DeliveryQuote, quote, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: LocalProtocol) -> None:
        with client.requests.quotes.with_streaming_response.create(
            request_id="request_id",
            id="id",
            currency="SEW",
            dropoff_estimate=parse_datetime("2019-12-27T18:11:19.117Z"),
            dropoff_location={},
            nonce="nonce",
            payment={},
            pickup_estimate=parse_datetime("2019-12-27T18:11:19.117Z"),
            pickup_location={},
            price=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quote = response.parse()
            assert_matches_type(DeliveryQuote, quote, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: LocalProtocol) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
            client.requests.quotes.with_raw_response.create(
                request_id="",
                id="id",
                currency="SEW",
                dropoff_estimate=parse_datetime("2019-12-27T18:11:19.117Z"),
                dropoff_location={},
                nonce="nonce",
                payment={},
                pickup_estimate=parse_datetime("2019-12-27T18:11:19.117Z"),
                pickup_location={},
                price=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: LocalProtocol) -> None:
        quote = client.requests.quotes.retrieve(
            quote_id="quote_id",
            request_id="request_id",
        )
        assert_matches_type(DeliveryQuote, quote, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: LocalProtocol) -> None:
        response = client.requests.quotes.with_raw_response.retrieve(
            quote_id="quote_id",
            request_id="request_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quote = response.parse()
        assert_matches_type(DeliveryQuote, quote, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: LocalProtocol) -> None:
        with client.requests.quotes.with_streaming_response.retrieve(
            quote_id="quote_id",
            request_id="request_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quote = response.parse()
            assert_matches_type(DeliveryQuote, quote, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: LocalProtocol) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
            client.requests.quotes.with_raw_response.retrieve(
                quote_id="quote_id",
                request_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `quote_id` but received ''"):
            client.requests.quotes.with_raw_response.retrieve(
                quote_id="",
                request_id="request_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: LocalProtocol) -> None:
        quote = client.requests.quotes.list(
            "request_id",
        )
        assert_matches_type(QuoteListResponse, quote, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LocalProtocol) -> None:
        response = client.requests.quotes.with_raw_response.list(
            "request_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quote = response.parse()
        assert_matches_type(QuoteListResponse, quote, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LocalProtocol) -> None:
        with client.requests.quotes.with_streaming_response.list(
            "request_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quote = response.parse()
            assert_matches_type(QuoteListResponse, quote, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: LocalProtocol) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
            client.requests.quotes.with_raw_response.list(
                "",
            )


class TestAsyncQuotes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLocalProtocol) -> None:
        quote = await async_client.requests.quotes.create(
            request_id="request_id",
            id="id",
            currency="SEW",
            dropoff_estimate=parse_datetime("2019-12-27T18:11:19.117Z"),
            dropoff_location={},
            nonce="nonce",
            payment={},
            pickup_estimate=parse_datetime("2019-12-27T18:11:19.117Z"),
            pickup_location={},
            price=0,
        )
        assert_matches_type(DeliveryQuote, quote, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLocalProtocol) -> None:
        quote = await async_client.requests.quotes.create(
            request_id="request_id",
            id="id",
            currency="SEW",
            dropoff_estimate=parse_datetime("2019-12-27T18:11:19.117Z"),
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
            nonce="nonce",
            payment={
                "instruments": [
                    {
                        "id": "id",
                        "handler_id": "handler_id",
                        "type": "type",
                        "billing_address": {
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
                        "credential": {"type": "type"},
                        "display": {},
                        "selected": True,
                    }
                ]
            },
            pickup_estimate=parse_datetime("2019-12-27T18:11:19.117Z"),
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
            price=0,
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(DeliveryQuote, quote, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLocalProtocol) -> None:
        response = await async_client.requests.quotes.with_raw_response.create(
            request_id="request_id",
            id="id",
            currency="SEW",
            dropoff_estimate=parse_datetime("2019-12-27T18:11:19.117Z"),
            dropoff_location={},
            nonce="nonce",
            payment={},
            pickup_estimate=parse_datetime("2019-12-27T18:11:19.117Z"),
            pickup_location={},
            price=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quote = await response.parse()
        assert_matches_type(DeliveryQuote, quote, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLocalProtocol) -> None:
        async with async_client.requests.quotes.with_streaming_response.create(
            request_id="request_id",
            id="id",
            currency="SEW",
            dropoff_estimate=parse_datetime("2019-12-27T18:11:19.117Z"),
            dropoff_location={},
            nonce="nonce",
            payment={},
            pickup_estimate=parse_datetime("2019-12-27T18:11:19.117Z"),
            pickup_location={},
            price=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quote = await response.parse()
            assert_matches_type(DeliveryQuote, quote, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncLocalProtocol) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
            await async_client.requests.quotes.with_raw_response.create(
                request_id="",
                id="id",
                currency="SEW",
                dropoff_estimate=parse_datetime("2019-12-27T18:11:19.117Z"),
                dropoff_location={},
                nonce="nonce",
                payment={},
                pickup_estimate=parse_datetime("2019-12-27T18:11:19.117Z"),
                pickup_location={},
                price=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLocalProtocol) -> None:
        quote = await async_client.requests.quotes.retrieve(
            quote_id="quote_id",
            request_id="request_id",
        )
        assert_matches_type(DeliveryQuote, quote, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLocalProtocol) -> None:
        response = await async_client.requests.quotes.with_raw_response.retrieve(
            quote_id="quote_id",
            request_id="request_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quote = await response.parse()
        assert_matches_type(DeliveryQuote, quote, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLocalProtocol) -> None:
        async with async_client.requests.quotes.with_streaming_response.retrieve(
            quote_id="quote_id",
            request_id="request_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quote = await response.parse()
            assert_matches_type(DeliveryQuote, quote, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLocalProtocol) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
            await async_client.requests.quotes.with_raw_response.retrieve(
                quote_id="quote_id",
                request_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `quote_id` but received ''"):
            await async_client.requests.quotes.with_raw_response.retrieve(
                quote_id="",
                request_id="request_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLocalProtocol) -> None:
        quote = await async_client.requests.quotes.list(
            "request_id",
        )
        assert_matches_type(QuoteListResponse, quote, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLocalProtocol) -> None:
        response = await async_client.requests.quotes.with_raw_response.list(
            "request_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quote = await response.parse()
        assert_matches_type(QuoteListResponse, quote, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLocalProtocol) -> None:
        async with async_client.requests.quotes.with_streaming_response.list(
            "request_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quote = await response.parse()
            assert_matches_type(QuoteListResponse, quote, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncLocalProtocol) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
            await async_client.requests.quotes.with_raw_response.list(
                "",
            )
