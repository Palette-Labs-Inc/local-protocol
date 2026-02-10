# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import payment_instrument_register_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.postal_address_param import PostalAddressParam
from ..types.evm_auth_capture_escrow_instrument import EvmAuthCaptureEscrowInstrument

__all__ = ["PaymentInstrumentsResource", "AsyncPaymentInstrumentsResource"]


class PaymentInstrumentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PaymentInstrumentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/local-protocol-python#accessing-raw-response-data-eg-headers
        """
        return PaymentInstrumentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PaymentInstrumentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/local-protocol-python#with_streaming_response
        """
        return PaymentInstrumentsResourceWithStreamingResponse(self)

    def register(
        self,
        *,
        id: str,
        token: payment_instrument_register_params.Token,
        amount: payment_instrument_register_params.Amount,
        authorization_expires_at: Union[str, datetime],
        chain_id: int,
        contract: str,
        handler_id: str,
        max_amount: payment_instrument_register_params.MaxAmount,
        nonce: str,
        operator: str,
        payer: str,
        payment_info_hash: str,
        preapproval_expires_at: Union[str, datetime],
        receiver: str,
        refund_expires_at: Union[str, datetime],
        type: Literal["evm_auth_capture_escrow"],
        billing_address: PostalAddressParam | Omit = omit,
        credential: payment_instrument_register_params.Credential | Omit = omit,
        display: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvmAuthCaptureEscrowInstrument:
        """
        Register a payment instrument for use in order creation.

        Args:
          id: Unique instrument identifier.

          token: EVM token identifier used for auth/capture settlement.

          amount: Amount in atomic units. Currency chain_id MUST match the instrument chain_id;
              currency address and decimals MUST match token address and decimals.

          authorization_expires_at: Authorization expiration (RFC 3339).

          chain_id: EVM chain id.

          contract: Escrow contract address.

          handler_id: Handler instance identifier.

          max_amount: Maximum amount that can be authorized (atomic units). Currency chain_id MUST
              match the instrument chain_id; currency address and decimals MUST match token
              address and decimals.

          nonce: Unique nonce for payment info hash computation.

          operator: Operator address.

          payer: Payer address.

          payment_info_hash: Hash identifying the on-chain payment authorization.

          preapproval_expires_at: Pre-approval expiration (RFC 3339).

          receiver: Receiver address for captures.

          refund_expires_at: Refund expiration (RFC 3339).

          billing_address: Billing address.

          credential: Base definition for any payment credential.

          display: Display information for the instrument.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/payment-instruments",
            body=maybe_transform(
                {
                    "id": id,
                    "token": token,
                    "amount": amount,
                    "authorization_expires_at": authorization_expires_at,
                    "chain_id": chain_id,
                    "contract": contract,
                    "handler_id": handler_id,
                    "max_amount": max_amount,
                    "nonce": nonce,
                    "operator": operator,
                    "payer": payer,
                    "payment_info_hash": payment_info_hash,
                    "preapproval_expires_at": preapproval_expires_at,
                    "receiver": receiver,
                    "refund_expires_at": refund_expires_at,
                    "type": type,
                    "billing_address": billing_address,
                    "credential": credential,
                    "display": display,
                },
                payment_instrument_register_params.PaymentInstrumentRegisterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvmAuthCaptureEscrowInstrument,
        )


class AsyncPaymentInstrumentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPaymentInstrumentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/local-protocol-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPaymentInstrumentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPaymentInstrumentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/local-protocol-python#with_streaming_response
        """
        return AsyncPaymentInstrumentsResourceWithStreamingResponse(self)

    async def register(
        self,
        *,
        id: str,
        token: payment_instrument_register_params.Token,
        amount: payment_instrument_register_params.Amount,
        authorization_expires_at: Union[str, datetime],
        chain_id: int,
        contract: str,
        handler_id: str,
        max_amount: payment_instrument_register_params.MaxAmount,
        nonce: str,
        operator: str,
        payer: str,
        payment_info_hash: str,
        preapproval_expires_at: Union[str, datetime],
        receiver: str,
        refund_expires_at: Union[str, datetime],
        type: Literal["evm_auth_capture_escrow"],
        billing_address: PostalAddressParam | Omit = omit,
        credential: payment_instrument_register_params.Credential | Omit = omit,
        display: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvmAuthCaptureEscrowInstrument:
        """
        Register a payment instrument for use in order creation.

        Args:
          id: Unique instrument identifier.

          token: EVM token identifier used for auth/capture settlement.

          amount: Amount in atomic units. Currency chain_id MUST match the instrument chain_id;
              currency address and decimals MUST match token address and decimals.

          authorization_expires_at: Authorization expiration (RFC 3339).

          chain_id: EVM chain id.

          contract: Escrow contract address.

          handler_id: Handler instance identifier.

          max_amount: Maximum amount that can be authorized (atomic units). Currency chain_id MUST
              match the instrument chain_id; currency address and decimals MUST match token
              address and decimals.

          nonce: Unique nonce for payment info hash computation.

          operator: Operator address.

          payer: Payer address.

          payment_info_hash: Hash identifying the on-chain payment authorization.

          preapproval_expires_at: Pre-approval expiration (RFC 3339).

          receiver: Receiver address for captures.

          refund_expires_at: Refund expiration (RFC 3339).

          billing_address: Billing address.

          credential: Base definition for any payment credential.

          display: Display information for the instrument.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/payment-instruments",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "token": token,
                    "amount": amount,
                    "authorization_expires_at": authorization_expires_at,
                    "chain_id": chain_id,
                    "contract": contract,
                    "handler_id": handler_id,
                    "max_amount": max_amount,
                    "nonce": nonce,
                    "operator": operator,
                    "payer": payer,
                    "payment_info_hash": payment_info_hash,
                    "preapproval_expires_at": preapproval_expires_at,
                    "receiver": receiver,
                    "refund_expires_at": refund_expires_at,
                    "type": type,
                    "billing_address": billing_address,
                    "credential": credential,
                    "display": display,
                },
                payment_instrument_register_params.PaymentInstrumentRegisterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvmAuthCaptureEscrowInstrument,
        )


class PaymentInstrumentsResourceWithRawResponse:
    def __init__(self, payment_instruments: PaymentInstrumentsResource) -> None:
        self._payment_instruments = payment_instruments

        self.register = to_raw_response_wrapper(
            payment_instruments.register,
        )


class AsyncPaymentInstrumentsResourceWithRawResponse:
    def __init__(self, payment_instruments: AsyncPaymentInstrumentsResource) -> None:
        self._payment_instruments = payment_instruments

        self.register = async_to_raw_response_wrapper(
            payment_instruments.register,
        )


class PaymentInstrumentsResourceWithStreamingResponse:
    def __init__(self, payment_instruments: PaymentInstrumentsResource) -> None:
        self._payment_instruments = payment_instruments

        self.register = to_streamed_response_wrapper(
            payment_instruments.register,
        )


class AsyncPaymentInstrumentsResourceWithStreamingResponse:
    def __init__(self, payment_instruments: AsyncPaymentInstrumentsResource) -> None:
        self._payment_instruments = payment_instruments

        self.register = async_to_streamed_response_wrapper(
            payment_instruments.register,
        )
