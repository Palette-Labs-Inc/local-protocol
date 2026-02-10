<?php

declare(strict_types=1);

namespace LocalProtocol\Services;

use LocalProtocol\Client;
use LocalProtocol\Core\Contracts\BaseResponse;
use LocalProtocol\Core\Exceptions\APIException;
use LocalProtocol\PaymentInstruments\EvmAuthCaptureEscrowInstrument;
use LocalProtocol\PaymentInstruments\PaymentInstrumentRegisterParams;
use LocalProtocol\PaymentInstruments\PaymentInstrumentRegisterParams\Amount;
use LocalProtocol\PaymentInstruments\PaymentInstrumentRegisterParams\Credential;
use LocalProtocol\PaymentInstruments\PaymentInstrumentRegisterParams\MaxAmount;
use LocalProtocol\PaymentInstruments\PaymentInstrumentRegisterParams\Token;
use LocalProtocol\RequestOptions;
use LocalProtocol\Requests\PostalAddress;
use LocalProtocol\ServiceContracts\PaymentInstrumentsRawContract;

/**
 * @phpstan-import-type TokenShape from \LocalProtocol\PaymentInstruments\PaymentInstrumentRegisterParams\Token
 * @phpstan-import-type AmountShape from \LocalProtocol\PaymentInstruments\PaymentInstrumentRegisterParams\Amount
 * @phpstan-import-type MaxAmountShape from \LocalProtocol\PaymentInstruments\PaymentInstrumentRegisterParams\MaxAmount
 * @phpstan-import-type PostalAddressShape from \LocalProtocol\Requests\PostalAddress
 * @phpstan-import-type CredentialShape from \LocalProtocol\PaymentInstruments\PaymentInstrumentRegisterParams\Credential
 * @phpstan-import-type RequestOpts from \LocalProtocol\RequestOptions
 */
final class PaymentInstrumentsRawService implements PaymentInstrumentsRawContract
{
    // @phpstan-ignore-next-line
    /**
     * @internal
     */
    public function __construct(private Client $client) {}

    /**
     * @api
     *
     * Register a payment instrument for use in order creation.
     *
     * @param array{
     *   id: string,
     *   token: Token|TokenShape,
     *   amount: Amount|AmountShape,
     *   authorizationExpiresAt: \DateTimeInterface,
     *   chainID: int,
     *   contract: string,
     *   handlerID: string,
     *   maxAmount: MaxAmount|MaxAmountShape,
     *   nonce: string,
     *   operator: string,
     *   payer: string,
     *   paymentInfoHash: string,
     *   preapprovalExpiresAt: \DateTimeInterface,
     *   receiver: string,
     *   refundExpiresAt: \DateTimeInterface,
     *   type?: 'evm_auth_capture_escrow',
     *   billingAddress?: PostalAddress|PostalAddressShape,
     *   credential?: Credential|CredentialShape,
     *   display?: array<string,mixed>,
     * }|PaymentInstrumentRegisterParams $params
     * @param RequestOpts|null $requestOptions
     *
     * @return BaseResponse<EvmAuthCaptureEscrowInstrument>
     *
     * @throws APIException
     */
    public function register(
        array|PaymentInstrumentRegisterParams $params,
        RequestOptions|array|null $requestOptions = null,
    ): BaseResponse {
        [$parsed, $options] = PaymentInstrumentRegisterParams::parseRequest(
            $params,
            $requestOptions,
        );

        // @phpstan-ignore-next-line return.type
        return $this->client->request(
            method: 'post',
            path: 'payment-instruments',
            body: (object) $parsed,
            options: $options,
            convert: EvmAuthCaptureEscrowInstrument::class,
        );
    }
}
