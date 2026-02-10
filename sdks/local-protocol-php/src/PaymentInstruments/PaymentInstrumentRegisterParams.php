<?php

declare(strict_types=1);

namespace LocalProtocol\PaymentInstruments;

use LocalProtocol\Core\Attributes\Optional;
use LocalProtocol\Core\Attributes\Required;
use LocalProtocol\Core\Concerns\SdkModel;
use LocalProtocol\Core\Concerns\SdkParams;
use LocalProtocol\Core\Contracts\BaseModel;
use LocalProtocol\PaymentInstruments\PaymentInstrumentRegisterParams\Amount;
use LocalProtocol\PaymentInstruments\PaymentInstrumentRegisterParams\Credential;
use LocalProtocol\PaymentInstruments\PaymentInstrumentRegisterParams\MaxAmount;
use LocalProtocol\PaymentInstruments\PaymentInstrumentRegisterParams\Token;
use LocalProtocol\Requests\PostalAddress;

/**
 * Register a payment instrument for use in order creation.
 *
 * @see LocalProtocol\Services\PaymentInstrumentsService::register()
 *
 * @phpstan-import-type TokenShape from \LocalProtocol\PaymentInstruments\PaymentInstrumentRegisterParams\Token
 * @phpstan-import-type AmountShape from \LocalProtocol\PaymentInstruments\PaymentInstrumentRegisterParams\Amount
 * @phpstan-import-type MaxAmountShape from \LocalProtocol\PaymentInstruments\PaymentInstrumentRegisterParams\MaxAmount
 * @phpstan-import-type PostalAddressShape from \LocalProtocol\Requests\PostalAddress
 * @phpstan-import-type CredentialShape from \LocalProtocol\PaymentInstruments\PaymentInstrumentRegisterParams\Credential
 *
 * @phpstan-type PaymentInstrumentRegisterParamsShape = array{
 *   type: 'evm_auth_capture_escrow',
 *   id: string,
 *   token: Token|TokenShape,
 *   amount: \LocalProtocol\PaymentInstruments\PaymentInstrumentRegisterParams\Amount|AmountShape,
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
 *   billingAddress?: null|PostalAddress|PostalAddressShape,
 *   credential?: null|Credential|CredentialShape,
 *   display?: array<string,mixed>|null,
 * }
 */
final class PaymentInstrumentRegisterParams implements BaseModel
{
    /** @use SdkModel<PaymentInstrumentRegisterParamsShape> */
    use SdkModel;
    use SdkParams;

    /** @var 'evm_auth_capture_escrow' $type */
    #[Required]
    public string $type = 'evm_auth_capture_escrow';

    /**
     * Unique instrument identifier.
     */
    #[Required]
    public string $id;

    /**
     * EVM token identifier used for auth/capture settlement.
     */
    #[Required]
    public Token $token;

    /**
     * Amount in atomic units. Currency chain_id MUST match the instrument chain_id; currency address and decimals MUST match token address and decimals.
     */
    #[Required]
    public Amount $amount;

    /**
     * Authorization expiration (RFC 3339).
     */
    #[Required('authorization_expires_at')]
    public \DateTimeInterface $authorizationExpiresAt;

    /**
     * EVM chain id.
     */
    #[Required('chain_id')]
    public int $chainID;

    /**
     * Escrow contract address.
     */
    #[Required]
    public string $contract;

    /**
     * Handler instance identifier.
     */
    #[Required('handler_id')]
    public string $handlerID;

    /**
     * Maximum amount that can be authorized (atomic units). Currency chain_id MUST match the instrument chain_id; currency address and decimals MUST match token address and decimals.
     */
    #[Required('max_amount')]
    public MaxAmount $maxAmount;

    /**
     * Unique nonce for payment info hash computation.
     */
    #[Required]
    public string $nonce;

    /**
     * Operator address.
     */
    #[Required]
    public string $operator;

    /**
     * Payer address.
     */
    #[Required]
    public string $payer;

    /**
     * Hash identifying the on-chain payment authorization.
     */
    #[Required('payment_info_hash')]
    public string $paymentInfoHash;

    /**
     * Pre-approval expiration (RFC 3339).
     */
    #[Required('preapproval_expires_at')]
    public \DateTimeInterface $preapprovalExpiresAt;

    /**
     * Receiver address for captures.
     */
    #[Required]
    public string $receiver;

    /**
     * Refund expiration (RFC 3339).
     */
    #[Required('refund_expires_at')]
    public \DateTimeInterface $refundExpiresAt;

    /**
     * Billing address.
     */
    #[Optional('billing_address')]
    public ?PostalAddress $billingAddress;

    /**
     * Base definition for any payment credential.
     */
    #[Optional]
    public ?Credential $credential;

    /**
     * Display information for the instrument. Each payment instrument schema defines its specific display properties, as outlined by the payment handler.
     *
     * @var array<string,mixed>|null $display
     */
    #[Optional(map: 'mixed')]
    public ?array $display;

    /**
     * `new PaymentInstrumentRegisterParams()` is missing required properties by the API.
     *
     * To enforce required parameters use
     * ```
     * PaymentInstrumentRegisterParams::with(
     *   id: ...,
     *   token: ...,
     *   amount: ...,
     *   authorizationExpiresAt: ...,
     *   chainID: ...,
     *   contract: ...,
     *   handlerID: ...,
     *   maxAmount: ...,
     *   nonce: ...,
     *   operator: ...,
     *   payer: ...,
     *   paymentInfoHash: ...,
     *   preapprovalExpiresAt: ...,
     *   receiver: ...,
     *   refundExpiresAt: ...,
     * )
     * ```
     *
     * Otherwise ensure the following setters are called
     *
     * ```
     * (new PaymentInstrumentRegisterParams)
     *   ->withID(...)
     *   ->withToken(...)
     *   ->withAmount(...)
     *   ->withAuthorizationExpiresAt(...)
     *   ->withChainID(...)
     *   ->withContract(...)
     *   ->withHandlerID(...)
     *   ->withMaxAmount(...)
     *   ->withNonce(...)
     *   ->withOperator(...)
     *   ->withPayer(...)
     *   ->withPaymentInfoHash(...)
     *   ->withPreapprovalExpiresAt(...)
     *   ->withReceiver(...)
     *   ->withRefundExpiresAt(...)
     * ```
     */
    public function __construct()
    {
        $this->initialize();
    }

    /**
     * Construct an instance from the required parameters.
     *
     * You must use named parameters to construct any parameters with a default value.
     *
     * @param Token|TokenShape $token
     * @param Amount|AmountShape $amount
     * @param MaxAmount|MaxAmountShape $maxAmount
     * @param PostalAddress|PostalAddressShape|null $billingAddress
     * @param Credential|CredentialShape|null $credential
     * @param array<string,mixed>|null $display
     */
    public static function with(
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
        PostalAddress|array|null $billingAddress = null,
        Credential|array|null $credential = null,
        ?array $display = null,
    ): self {
        $self = new self;

        $self['id'] = $id;
        $self['token'] = $token;
        $self['amount'] = $amount;
        $self['authorizationExpiresAt'] = $authorizationExpiresAt;
        $self['chainID'] = $chainID;
        $self['contract'] = $contract;
        $self['handlerID'] = $handlerID;
        $self['maxAmount'] = $maxAmount;
        $self['nonce'] = $nonce;
        $self['operator'] = $operator;
        $self['payer'] = $payer;
        $self['paymentInfoHash'] = $paymentInfoHash;
        $self['preapprovalExpiresAt'] = $preapprovalExpiresAt;
        $self['receiver'] = $receiver;
        $self['refundExpiresAt'] = $refundExpiresAt;

        null !== $billingAddress && $self['billingAddress'] = $billingAddress;
        null !== $credential && $self['credential'] = $credential;
        null !== $display && $self['display'] = $display;

        return $self;
    }

    /**
     * @param 'evm_auth_capture_escrow' $type
     */
    public function withType(string $type): self
    {
        $self = clone $this;
        $self['type'] = $type;

        return $self;
    }

    /**
     * Unique instrument identifier.
     */
    public function withID(string $id): self
    {
        $self = clone $this;
        $self['id'] = $id;

        return $self;
    }

    /**
     * EVM token identifier used for auth/capture settlement.
     *
     * @param Token|TokenShape $token
     */
    public function withToken(Token|array $token): self
    {
        $self = clone $this;
        $self['token'] = $token;

        return $self;
    }

    /**
     * Amount in atomic units. Currency chain_id MUST match the instrument chain_id; currency address and decimals MUST match token address and decimals.
     *
     * @param Amount|AmountShape $amount
     */
    public function withAmount(
        Amount|array $amount,
    ): self {
        $self = clone $this;
        $self['amount'] = $amount;

        return $self;
    }

    /**
     * Authorization expiration (RFC 3339).
     */
    public function withAuthorizationExpiresAt(
        \DateTimeInterface $authorizationExpiresAt
    ): self {
        $self = clone $this;
        $self['authorizationExpiresAt'] = $authorizationExpiresAt;

        return $self;
    }

    /**
     * EVM chain id.
     */
    public function withChainID(int $chainID): self
    {
        $self = clone $this;
        $self['chainID'] = $chainID;

        return $self;
    }

    /**
     * Escrow contract address.
     */
    public function withContract(string $contract): self
    {
        $self = clone $this;
        $self['contract'] = $contract;

        return $self;
    }

    /**
     * Handler instance identifier.
     */
    public function withHandlerID(string $handlerID): self
    {
        $self = clone $this;
        $self['handlerID'] = $handlerID;

        return $self;
    }

    /**
     * Maximum amount that can be authorized (atomic units). Currency chain_id MUST match the instrument chain_id; currency address and decimals MUST match token address and decimals.
     *
     * @param MaxAmount|MaxAmountShape $maxAmount
     */
    public function withMaxAmount(MaxAmount|array $maxAmount): self
    {
        $self = clone $this;
        $self['maxAmount'] = $maxAmount;

        return $self;
    }

    /**
     * Unique nonce for payment info hash computation.
     */
    public function withNonce(string $nonce): self
    {
        $self = clone $this;
        $self['nonce'] = $nonce;

        return $self;
    }

    /**
     * Operator address.
     */
    public function withOperator(string $operator): self
    {
        $self = clone $this;
        $self['operator'] = $operator;

        return $self;
    }

    /**
     * Payer address.
     */
    public function withPayer(string $payer): self
    {
        $self = clone $this;
        $self['payer'] = $payer;

        return $self;
    }

    /**
     * Hash identifying the on-chain payment authorization.
     */
    public function withPaymentInfoHash(string $paymentInfoHash): self
    {
        $self = clone $this;
        $self['paymentInfoHash'] = $paymentInfoHash;

        return $self;
    }

    /**
     * Pre-approval expiration (RFC 3339).
     */
    public function withPreapprovalExpiresAt(
        \DateTimeInterface $preapprovalExpiresAt
    ): self {
        $self = clone $this;
        $self['preapprovalExpiresAt'] = $preapprovalExpiresAt;

        return $self;
    }

    /**
     * Receiver address for captures.
     */
    public function withReceiver(string $receiver): self
    {
        $self = clone $this;
        $self['receiver'] = $receiver;

        return $self;
    }

    /**
     * Refund expiration (RFC 3339).
     */
    public function withRefundExpiresAt(
        \DateTimeInterface $refundExpiresAt
    ): self {
        $self = clone $this;
        $self['refundExpiresAt'] = $refundExpiresAt;

        return $self;
    }

    /**
     * Billing address.
     *
     * @param PostalAddress|PostalAddressShape $billingAddress
     */
    public function withBillingAddress(
        PostalAddress|array $billingAddress
    ): self {
        $self = clone $this;
        $self['billingAddress'] = $billingAddress;

        return $self;
    }

    /**
     * Base definition for any payment credential.
     *
     * @param Credential|CredentialShape $credential
     */
    public function withCredential(Credential|array $credential): self
    {
        $self = clone $this;
        $self['credential'] = $credential;

        return $self;
    }

    /**
     * Display information for the instrument. Each payment instrument schema defines its specific display properties, as outlined by the payment handler.
     *
     * @param array<string,mixed> $display
     */
    public function withDisplay(array $display): self
    {
        $self = clone $this;
        $self['display'] = $display;

        return $self;
    }
}
