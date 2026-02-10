<?php

declare(strict_types=1);

namespace LocalProtocol\Orders;

use LocalProtocol\Core\Attributes\Required;
use LocalProtocol\Core\Concerns\SdkModel;
use LocalProtocol\Core\Concerns\SdkParams;
use LocalProtocol\Core\Contracts\BaseModel;

/**
 * Accept a quote and create an order. The `nonce` field provides idempotency.
 *
 * @see LocalProtocol\Services\OrdersService::create()
 *
 * @phpstan-type OrderCreateParamsShape = array{
 *   nonce: string,
 *   orderQuoteID: string,
 *   orderRequestID: string,
 *   paymentInstrumentID: string,
 * }
 */
final class OrderCreateParams implements BaseModel
{
    /** @use SdkModel<OrderCreateParamsShape> */
    use SdkModel;
    use SdkParams;

    /**
     * Client-generated idempotency key.
     */
    #[Required]
    public string $nonce;

    /**
     * The accepted quote.
     */
    #[Required('order_quote_id')]
    public string $orderQuoteID;

    /**
     * The order request to fulfill.
     */
    #[Required('order_request_id')]
    public string $orderRequestID;

    /**
     * Reference to the registered payment instrument.
     */
    #[Required('payment_instrument_id')]
    public string $paymentInstrumentID;

    /**
     * `new OrderCreateParams()` is missing required properties by the API.
     *
     * To enforce required parameters use
     * ```
     * OrderCreateParams::with(
     *   nonce: ..., orderQuoteID: ..., orderRequestID: ..., paymentInstrumentID: ...
     * )
     * ```
     *
     * Otherwise ensure the following setters are called
     *
     * ```
     * (new OrderCreateParams)
     *   ->withNonce(...)
     *   ->withOrderQuoteID(...)
     *   ->withOrderRequestID(...)
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
        string $nonce,
        string $orderQuoteID,
        string $orderRequestID,
        string $paymentInstrumentID,
    ): self {
        $self = new self;

        $self['nonce'] = $nonce;
        $self['orderQuoteID'] = $orderQuoteID;
        $self['orderRequestID'] = $orderRequestID;
        $self['paymentInstrumentID'] = $paymentInstrumentID;

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
     * The accepted quote.
     */
    public function withOrderQuoteID(string $orderQuoteID): self
    {
        $self = clone $this;
        $self['orderQuoteID'] = $orderQuoteID;

        return $self;
    }

    /**
     * The order request to fulfill.
     */
    public function withOrderRequestID(string $orderRequestID): self
    {
        $self = clone $this;
        $self['orderRequestID'] = $orderRequestID;

        return $self;
    }

    /**
     * Reference to the registered payment instrument.
     */
    public function withPaymentInstrumentID(string $paymentInstrumentID): self
    {
        $self = clone $this;
        $self['paymentInstrumentID'] = $paymentInstrumentID;

        return $self;
    }
}
