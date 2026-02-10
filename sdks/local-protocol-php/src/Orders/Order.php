<?php

declare(strict_types=1);

namespace LocalProtocol\Orders;

use LocalProtocol\Core\Attributes\Required;
use LocalProtocol\Core\Concerns\SdkModel;
use LocalProtocol\Core\Contracts\BaseModel;

/**
 * An order.
 *
 * @phpstan-type OrderShape = array{
 *   id: string, intentID: string, nonce: string, paymentInstrumentID: string
 * }
 */
final class Order implements BaseModel
{
    /** @use SdkModel<OrderShape> */
    use SdkModel;

    /**
     * Unique order identifier.
     */
    #[Required]
    public string $id;

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
     * Reference to the payment instrument used.
     */
    #[Required('payment_instrument_id')]
    public string $paymentInstrumentID;

    /**
     * `new Order()` is missing required properties by the API.
     *
     * To enforce required parameters use
     * ```
     * Order::with(id: ..., intentID: ..., nonce: ..., paymentInstrumentID: ...)
     * ```
     *
     * Otherwise ensure the following setters are called
     *
     * ```
     * (new Order)
     *   ->withID(...)
     *   ->withIntentID(...)
     *   ->withNonce(...)
     *   ->withPaymentInstrumentID(...)
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
        string $intentID,
        string $nonce,
        string $paymentInstrumentID
    ): self {
        $self = new self;

        $self['id'] = $id;
        $self['intentID'] = $intentID;
        $self['nonce'] = $nonce;
        $self['paymentInstrumentID'] = $paymentInstrumentID;

        return $self;
    }

    /**
     * Unique order identifier.
     */
    public function withID(string $id): self
    {
        $self = clone $this;
        $self['id'] = $id;

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
     * Reference to the payment instrument used.
     */
    public function withPaymentInstrumentID(string $paymentInstrumentID): self
    {
        $self = clone $this;
        $self['paymentInstrumentID'] = $paymentInstrumentID;

        return $self;
    }
}
