<?php

declare(strict_types=1);

namespace LocalProtocol\Orders\Requests\Quotes;

use LocalProtocol\Core\Attributes\Required;
use LocalProtocol\Core\Concerns\SdkModel;
use LocalProtocol\Core\Contracts\BaseModel;

/**
 * An order quote.
 *
 * @phpstan-type OrderQuoteShape = array{
 *   id: string,
 *   expiresAt: \DateTimeInterface,
 *   intentID: string,
 *   nonce: string,
 *   price: int,
 *   readyAt: \DateTimeInterface,
 * }
 */
final class OrderQuote implements BaseModel
{
    /** @use SdkModel<OrderQuoteShape> */
    use SdkModel;

    /**
     * Unique quote identifier.
     */
    #[Required]
    public string $id;

    /**
     * Quote expiration time (RFC 3339).
     */
    #[Required('expires_at')]
    public \DateTimeInterface $expiresAt;

    /**
     * Shared intent identifier for tracing Request -> Quote -> Order.
     */
    #[Required('intent_id')]
    public string $intentID;

    /**
     * Client-generated idempotency key.
     */
    #[Required]
    public string $nonce;

    /**
     * Price in minor currency units.
     */
    #[Required]
    public int $price;

    /**
     * Estimated readiness time (RFC 3339).
     */
    #[Required('ready_at')]
    public \DateTimeInterface $readyAt;

    /**
     * `new OrderQuote()` is missing required properties by the API.
     *
     * To enforce required parameters use
     * ```
     * OrderQuote::with(
     *   id: ..., expiresAt: ..., intentID: ..., nonce: ..., price: ..., readyAt: ...
     * )
     * ```
     *
     * Otherwise ensure the following setters are called
     *
     * ```
     * (new OrderQuote)
     *   ->withID(...)
     *   ->withExpiresAt(...)
     *   ->withIntentID(...)
     *   ->withNonce(...)
     *   ->withPrice(...)
     *   ->withReadyAt(...)
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
     */
    public static function with(
        string $id,
        \DateTimeInterface $expiresAt,
        string $intentID,
        string $nonce,
        int $price,
        \DateTimeInterface $readyAt,
    ): self {
        $self = new self;

        $self['id'] = $id;
        $self['expiresAt'] = $expiresAt;
        $self['intentID'] = $intentID;
        $self['nonce'] = $nonce;
        $self['price'] = $price;
        $self['readyAt'] = $readyAt;

        return $self;
    }

    /**
     * Unique quote identifier.
     */
    public function withID(string $id): self
    {
        $self = clone $this;
        $self['id'] = $id;

        return $self;
    }

    /**
     * Quote expiration time (RFC 3339).
     */
    public function withExpiresAt(\DateTimeInterface $expiresAt): self
    {
        $self = clone $this;
        $self['expiresAt'] = $expiresAt;

        return $self;
    }

    /**
     * Shared intent identifier for tracing Request -> Quote -> Order.
     */
    public function withIntentID(string $intentID): self
    {
        $self = clone $this;
        $self['intentID'] = $intentID;

        return $self;
    }

    /**
     * Client-generated idempotency key.
     */
    public function withNonce(string $nonce): self
    {
        $self = clone $this;
        $self['nonce'] = $nonce;

        return $self;
    }

    /**
     * Price in minor currency units.
     */
    public function withPrice(int $price): self
    {
        $self = clone $this;
        $self['price'] = $price;

        return $self;
    }

    /**
     * Estimated readiness time (RFC 3339).
     */
    public function withReadyAt(\DateTimeInterface $readyAt): self
    {
        $self = clone $this;
        $self['readyAt'] = $readyAt;

        return $self;
    }
}
