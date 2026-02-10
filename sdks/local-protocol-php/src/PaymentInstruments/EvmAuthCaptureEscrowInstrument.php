<?php

declare(strict_types=1);

namespace LocalProtocol\PaymentInstruments;

use LocalProtocol\Core\Attributes\Optional;
use LocalProtocol\Core\Attributes\Required;
use LocalProtocol\Core\Concerns\SdkModel;
use LocalProtocol\Core\Contracts\BaseModel;
use LocalProtocol\PaymentInstruments\EvmAuthCaptureEscrowInstrumentDetails\Token;
use LocalProtocol\PaymentInstruments\PaymentInstrument\Credential;
use LocalProtocol\Requests\PostalAddress;

/**
 * Payment instrument for auth/capture escrow on EVM chains.
 *
 * @phpstan-import-type PostalAddressShape from \LocalProtocol\Requests\PostalAddress
 * @phpstan-import-type CredentialShape from \LocalProtocol\PaymentInstruments\PaymentInstrument\Credential
 * @phpstan-import-type TokenShape from \LocalProtocol\PaymentInstruments\EvmAuthCaptureEscrowInstrumentDetails\Token
 * @phpstan-import-type EvmAmountShape from \LocalProtocol\PaymentInstruments\EvmAmount
 *
 * @phpstan-type EvmAuthCaptureEscrowInstrumentShape = array{
 *   id: string,
 *   handlerID: string,
 *   type: string,
 *   billingAddress?: null|PostalAddress|PostalAddressShape,
 *   credential?: null|Credential|CredentialShape,
 *   display?: array<string,mixed>|null,
 *   token: Token|TokenShape,
 *   amount: EvmAmount|EvmAmountShape,
 *   authorizationExpiresAt: \DateTimeInterface,
 *   chainID: int,
 *   contract: string,
 *   maxAmount: EvmAmount|EvmAmountShape,
 *   nonce: string,
 *   operator: string,
 *   payer: string,
 *   paymentInfoHash: string,
 *   preapprovalExpiresAt: \DateTimeInterface,
 *   receiver: string,
 *   refundExpiresAt: \DateTimeInterface,
 * }
 */
final class EvmAuthCaptureEscrowInstrument implements BaseModel
{
    /** @use SdkModel<EvmAuthCaptureEscrowInstrumentShape> */
    use SdkModel;

    /**
     * Unique instrument identifier.
     */
    #[Required]
    public string $id;

    /**
     * Handler instance identifier.
     */
    #[Required('handler_id')]
    public string $handlerID;

    /**
     * Instrument category (e.g., 'card', 'tokenized_card').
     */
    #[Required]
    public string $type;

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
     * EVM token identifier used for auth/capture settlement.
     */
    #[Required]
    public Token $token;

    /**
     * Amount denominated in an EVM token. Value is in atomic token units.
     */
    #[Required]
    public EvmAmount $amount;

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
     * Amount denominated in an EVM token. Value is in atomic token units.
     */
    #[Required('max_amount')]
    public EvmAmount $maxAmount;

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
     * `new EvmAuthCaptureEscrowInstrument()` is missing required properties by the API.
     *
     * To enforce required parameters use
     * ```
     * EvmAuthCaptureEscrowInstrument::with(
     *   id: ...,
     *   handlerID: ...,
     *   type: ...,
     *   token: ...,
     *   amount: ...,
     *   authorizationExpiresAt: ...,
     *   chainID: ...,
     *   contract: ...,
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
     * (new EvmAuthCaptureEscrowInstrument)
     *   ->withID(...)
     *   ->withHandlerID(...)
     *   ->withType(...)
     *   ->withToken(...)
     *   ->withAmount(...)
     *   ->withAuthorizationExpiresAt(...)
     *   ->withChainID(...)
     *   ->withContract(...)
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
     * @param EvmAmount|EvmAmountShape $amount
     * @param EvmAmount|EvmAmountShape $maxAmount
     * @param PostalAddress|PostalAddressShape|null $billingAddress
     * @param Credential|CredentialShape|null $credential
     * @param array<string,mixed>|null $display
     */
    public static function with(
        string $id,
        string $handlerID,
        string $type,
        Token|array $token,
        EvmAmount|array $amount,
        \DateTimeInterface $authorizationExpiresAt,
        int $chainID,
        string $contract,
        EvmAmount|array $maxAmount,
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
        $self['handlerID'] = $handlerID;
        $self['type'] = $type;
        $self['token'] = $token;
        $self['amount'] = $amount;
        $self['authorizationExpiresAt'] = $authorizationExpiresAt;
        $self['chainID'] = $chainID;
        $self['contract'] = $contract;
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
     * Unique instrument identifier.
     */
    public function withID(string $id): self
    {
        $self = clone $this;
        $self['id'] = $id;

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
     * Instrument category (e.g., 'card', 'tokenized_card').
     */
    public function withType(string $type): self
    {
        $self = clone $this;
        $self['type'] = $type;

        return $self;
    }

    /**
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
     * Amount denominated in an EVM token. Value is in atomic token units.
     *
     * @param EvmAmount|EvmAmountShape $amount
     */
    public function withAmount(EvmAmount|array $amount): self
    {
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
     * Amount denominated in an EVM token. Value is in atomic token units.
     *
     * @param EvmAmount|EvmAmountShape $maxAmount
     */
    public function withMaxAmount(EvmAmount|array $maxAmount): self
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
}
