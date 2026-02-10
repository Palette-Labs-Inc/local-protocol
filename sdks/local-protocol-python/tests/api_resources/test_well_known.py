# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from local_protocol import LocalProtocol, AsyncLocalProtocol
from local_protocol.types import WellKnownRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWellKnown:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: LocalProtocol) -> None:
        well_known = client.well_known.retrieve()
        assert_matches_type(WellKnownRetrieveResponse, well_known, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: LocalProtocol) -> None:
        response = client.well_known.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        well_known = response.parse()
        assert_matches_type(WellKnownRetrieveResponse, well_known, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: LocalProtocol) -> None:
        with client.well_known.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            well_known = response.parse()
            assert_matches_type(WellKnownRetrieveResponse, well_known, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWellKnown:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLocalProtocol) -> None:
        well_known = await async_client.well_known.retrieve()
        assert_matches_type(WellKnownRetrieveResponse, well_known, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLocalProtocol) -> None:
        response = await async_client.well_known.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        well_known = await response.parse()
        assert_matches_type(WellKnownRetrieveResponse, well_known, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLocalProtocol) -> None:
        async with async_client.well_known.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            well_known = await response.parse()
            assert_matches_type(WellKnownRetrieveResponse, well_known, path=["response"])

        assert cast(Any, response.is_closed) is True
