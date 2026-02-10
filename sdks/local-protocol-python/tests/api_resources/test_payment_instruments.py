# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from local_protocol import LocalProtocol, AsyncLocalProtocol
from local_protocol.types import EvmAuthCaptureEscrowInstrument
from local_protocol._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPaymentInstruments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_register(self, client: LocalProtocol) -> None:
        payment_instrument = client.payment_instruments.register(
            id="id",
            token={
                "decimals": 0,
                "symbol": "symbol",
            },
            amount={
                "currency": {"symbol": "SQ9_0_L1__5L"},
                "value": "269125115713",
            },
            authorization_expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            chain_id=1,
            contract="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            handler_id="handler_id",
            max_amount={
                "currency": {"symbol": "SQ9_0_L1__5L"},
                "value": "269125115713",
            },
            nonce="269125115713",
            operator="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            payer="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            payment_info_hash="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8ACa3CC53eb6CEAA2eaa0Aa6be",
            preapproval_expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            receiver="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            refund_expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            type="evm_auth_capture_escrow",
        )
        assert_matches_type(EvmAuthCaptureEscrowInstrument, payment_instrument, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_register_with_all_params(self, client: LocalProtocol) -> None:
        payment_instrument = client.payment_instruments.register(
            id="id",
            token={
                "decimals": 0,
                "symbol": "symbol",
                "address": "0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            },
            amount={
                "currency": {
                    "address": "0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
                    "chain_id": 1,
                    "decimals": 0,
                },
                "value": "269125115713",
            },
            authorization_expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            chain_id=1,
            contract="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            handler_id="handler_id",
            max_amount={
                "currency": {
                    "address": "0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
                    "chain_id": 1,
                    "decimals": 0,
                },
                "value": "269125115713",
            },
            nonce="269125115713",
            operator="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            payer="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            payment_info_hash="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8ACa3CC53eb6CEAA2eaa0Aa6be",
            preapproval_expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            receiver="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            refund_expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            type="evm_auth_capture_escrow",
            billing_address={
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
            credential={"type": "type"},
            display={"foo": "bar"},
        )
        assert_matches_type(EvmAuthCaptureEscrowInstrument, payment_instrument, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_register(self, client: LocalProtocol) -> None:
        response = client.payment_instruments.with_raw_response.register(
            id="id",
            token={
                "decimals": 0,
                "symbol": "symbol",
            },
            amount={
                "currency": {"symbol": "SQ9_0_L1__5L"},
                "value": "269125115713",
            },
            authorization_expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            chain_id=1,
            contract="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            handler_id="handler_id",
            max_amount={
                "currency": {"symbol": "SQ9_0_L1__5L"},
                "value": "269125115713",
            },
            nonce="269125115713",
            operator="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            payer="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            payment_info_hash="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8ACa3CC53eb6CEAA2eaa0Aa6be",
            preapproval_expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            receiver="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            refund_expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            type="evm_auth_capture_escrow",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_instrument = response.parse()
        assert_matches_type(EvmAuthCaptureEscrowInstrument, payment_instrument, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_register(self, client: LocalProtocol) -> None:
        with client.payment_instruments.with_streaming_response.register(
            id="id",
            token={
                "decimals": 0,
                "symbol": "symbol",
            },
            amount={
                "currency": {"symbol": "SQ9_0_L1__5L"},
                "value": "269125115713",
            },
            authorization_expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            chain_id=1,
            contract="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            handler_id="handler_id",
            max_amount={
                "currency": {"symbol": "SQ9_0_L1__5L"},
                "value": "269125115713",
            },
            nonce="269125115713",
            operator="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            payer="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            payment_info_hash="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8ACa3CC53eb6CEAA2eaa0Aa6be",
            preapproval_expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            receiver="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            refund_expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            type="evm_auth_capture_escrow",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_instrument = response.parse()
            assert_matches_type(EvmAuthCaptureEscrowInstrument, payment_instrument, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPaymentInstruments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_register(self, async_client: AsyncLocalProtocol) -> None:
        payment_instrument = await async_client.payment_instruments.register(
            id="id",
            token={
                "decimals": 0,
                "symbol": "symbol",
            },
            amount={
                "currency": {"symbol": "SQ9_0_L1__5L"},
                "value": "269125115713",
            },
            authorization_expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            chain_id=1,
            contract="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            handler_id="handler_id",
            max_amount={
                "currency": {"symbol": "SQ9_0_L1__5L"},
                "value": "269125115713",
            },
            nonce="269125115713",
            operator="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            payer="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            payment_info_hash="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8ACa3CC53eb6CEAA2eaa0Aa6be",
            preapproval_expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            receiver="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            refund_expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            type="evm_auth_capture_escrow",
        )
        assert_matches_type(EvmAuthCaptureEscrowInstrument, payment_instrument, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_register_with_all_params(self, async_client: AsyncLocalProtocol) -> None:
        payment_instrument = await async_client.payment_instruments.register(
            id="id",
            token={
                "decimals": 0,
                "symbol": "symbol",
                "address": "0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            },
            amount={
                "currency": {
                    "address": "0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
                    "chain_id": 1,
                    "decimals": 0,
                },
                "value": "269125115713",
            },
            authorization_expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            chain_id=1,
            contract="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            handler_id="handler_id",
            max_amount={
                "currency": {
                    "address": "0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
                    "chain_id": 1,
                    "decimals": 0,
                },
                "value": "269125115713",
            },
            nonce="269125115713",
            operator="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            payer="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            payment_info_hash="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8ACa3CC53eb6CEAA2eaa0Aa6be",
            preapproval_expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            receiver="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            refund_expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            type="evm_auth_capture_escrow",
            billing_address={
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
            credential={"type": "type"},
            display={"foo": "bar"},
        )
        assert_matches_type(EvmAuthCaptureEscrowInstrument, payment_instrument, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_register(self, async_client: AsyncLocalProtocol) -> None:
        response = await async_client.payment_instruments.with_raw_response.register(
            id="id",
            token={
                "decimals": 0,
                "symbol": "symbol",
            },
            amount={
                "currency": {"symbol": "SQ9_0_L1__5L"},
                "value": "269125115713",
            },
            authorization_expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            chain_id=1,
            contract="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            handler_id="handler_id",
            max_amount={
                "currency": {"symbol": "SQ9_0_L1__5L"},
                "value": "269125115713",
            },
            nonce="269125115713",
            operator="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            payer="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            payment_info_hash="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8ACa3CC53eb6CEAA2eaa0Aa6be",
            preapproval_expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            receiver="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            refund_expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            type="evm_auth_capture_escrow",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_instrument = await response.parse()
        assert_matches_type(EvmAuthCaptureEscrowInstrument, payment_instrument, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_register(self, async_client: AsyncLocalProtocol) -> None:
        async with async_client.payment_instruments.with_streaming_response.register(
            id="id",
            token={
                "decimals": 0,
                "symbol": "symbol",
            },
            amount={
                "currency": {"symbol": "SQ9_0_L1__5L"},
                "value": "269125115713",
            },
            authorization_expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            chain_id=1,
            contract="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            handler_id="handler_id",
            max_amount={
                "currency": {"symbol": "SQ9_0_L1__5L"},
                "value": "269125115713",
            },
            nonce="269125115713",
            operator="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            payer="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            payment_info_hash="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8ACa3CC53eb6CEAA2eaa0Aa6be",
            preapproval_expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            receiver="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            refund_expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            type="evm_auth_capture_escrow",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_instrument = await response.parse()
            assert_matches_type(EvmAuthCaptureEscrowInstrument, payment_instrument, path=["response"])

        assert cast(Any, response.is_closed) is True
