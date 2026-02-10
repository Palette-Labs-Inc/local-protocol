<?php

declare(strict_types=1);

namespace LocalProtocol\ServiceContracts;

use LocalProtocol\Core\Exceptions\APIException;
use LocalProtocol\PaymentInstruments\EvmAuthCaptureEscrowInstrument;
use LocalProtocol\PaymentInstruments\PaymentInstrumentRegisterParams\Amount;
use LocalProtocol\PaymentInstruments\PaymentInstrumentRegisterParams\Credential;
use LocalProtocol\PaymentInstruments\PaymentInstrumentRegisterParams\MaxAmount;
use LocalProtocol\PaymentInstruments\PaymentInstrumentRegisterParams\Token;
use LocalProtocol\RequestOptions;
use LocalProtocol\Requests\PostalAddress;

/**
 * @phpstan-import-type TokenShape from \LocalProtocol\PaymentInstruments\PaymentInstrumentRegisterParams\Token
 * @phpstan-import-type AmountShape from \LocalProtocol\PaymentInstruments\PaymentInstrumentRegisterParams\Amount
 * @phpstan-import-type MaxAmountShape from \LocalProtocol\PaymentInstruments\PaymentInstrumentRegisterParams\MaxAmount
 * @phpstan-import-type PostalAddressShape from \LocalProtocol\Requests\PostalAddress
 * @phpstan-import-type CredentialShape from \LocalProtocol\PaymentInstruments\PaymentInstrumentRegisterParams\Credential
 * @phpstan-import-type RequestOpts from \LocalProtocol\RequestOptions
 */
interface PaymentInstrumentsContract
{
    /**
     * @api
     *
     * @param string $id unique instrument identifier
     * @param Token|TokenShape $token EVM token identifier used for auth/capture settlement
     * @param Amount|AmountShape $amount Amount in atomic units. Currency chain_id MUST match the instrument chain_id; currency address and decimals MUST match token address and decimals.
     * @param \DateTimeInterface $authorizationExpiresAt authorization expiration (RFC 3339)
     * @param int $chainID EVM chain id
     * @param string $contract escrow contract address
     * @param string $handlerID handler instance identifier
     * @param MaxAmount|MaxAmountShape $maxAmount Maximum amount that can be authorized (atomic units). Currency chain_id MUST match the instrument chain_id; currency address and decimals MUST match token address and decimals.
     * @param string $nonce unique nonce for payment info hash computation
     * @param string $operator operator address
     * @param string $payer payer address
     * @param string $paymentInfoHash hash identifying the on-chain payment authorization
     * @param \DateTimeInterface $preapprovalExpiresAt pre-approval expiration (RFC 3339)
     * @param string $receiver receiver address for captures
     * @param \DateTimeInterface $refundExpiresAt refund expiration (RFC 3339)
     * @param 'evm_auth_capture_escrow' $type
     * @param PostalAddress|PostalAddressShape $billingAddress billing address
     * @param Credential|CredentialShape $credential base definition for any payment credential
     * @param array<string,mixed> $display Display information for the instrument. Each payment instrument schema defines its specific display properties, as outlined by the payment handler.
     * @param RequestOpts|null $requestOptions
     *
     * @throws APIException
     */
    public function register(
        string $id,
        Token|array $token,
        Amount|array $amount,
        \DateTimeInterface $authorizationExpiresAt,
        int $chainID,
        string $contract,
        string $handlerID,
        MaxAmount|array $maxAmount,
        string $nonce,
        string $operator,
        string $payer,
        string $paymentInfoHash,
        \DateTimeInterface $preapprovalExpiresAt,
        string $receiver,
        \DateTimeInterface $refundExpiresAt,
        string $type = 'evm_auth_capture_escrow',
        PostalAddress|array|null $billingAddress = null,
        Credential|array|null $credential = null,
        ?array $display = null,
        RequestOptions|array|null $requestOptions = null,
    ): EvmAuthCaptureEscrowInstrument;
}
