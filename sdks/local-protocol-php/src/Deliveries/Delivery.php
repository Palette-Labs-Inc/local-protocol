<?php

declare(strict_types=1);

namespace LocalProtocol\Deliveries;

use LocalProtocol\Core\Attributes\Optional;
use LocalProtocol\Core\Attributes\Required;
use LocalProtocol\Core\Concerns\SdkModel;
use LocalProtocol\Core\Contracts\BaseModel;

/**
 * A delivery resource.
 *
 * @phpstan-type DeliveryShape = array{
 *   id: string,
 *   createdAt: \DateTimeInterface,
 *   event: string,
 *   eventDescription: string,
 *   eventVocabulary: string,
 *   paymentInstrumentID: string,
 *   quoteID: string,
 *   requestID: string,
 *   updatedAt: \DateTimeInterface,
 *   webhookURL?: string|null,
 * }
 */
final class Delivery implements BaseModel
{
    /** @use SdkModel<DeliveryShape> */
    use SdkModel;

    /**
     * Unique delivery identifier.
     */
    #[Required]
    public string $id;

    /**
     * Creation timestamp (RFC 3339).
     */
    #[Required('created_at')]
    public \DateTimeInterface $createdAt;

    /**
     * Current event identifier.
     */
    #[Required]
    public string $event;

    /**
     * Human-readable description of the current event.
     */
    #[Required('event_description')]
    public string $eventDescription;

    /**
     * Event vocabulary standard in use.
     */
    #[Required('event_vocabulary')]
    public string $eventVocabulary;

    /**
     * Reference to the payment instrument used to create this delivery.
     */
    #[Required('payment_instrument_id')]
    public string $paymentInstrumentID;

    /**
     * Reference to the accepted quote.
     */
    #[Required('quote_id')]
    public string $quoteID;

    /**
     * Reference to the delivery request.
     */
    #[Required('request_id')]
    public string $requestID;

    /**
     * Last update timestamp (RFC 3339).
     */
    #[Required('updated_at')]
    public \DateTimeInterface $updatedAt;

    /**
     * Registered webhook URL, if any.
     */
    #[Optional('webhook_url', nullable: true)]
    public ?string $webhookURL;

    /**
     * `new Delivery()` is missing required properties by the API.
     *
     * To enforce required parameters use
     * ```
     * Delivery::with(
     *   id: ...,
     *   createdAt: ...,
     *   event: ...,
     *   eventDescription: ...,
     *   eventVocabulary: ...,
     *   paymentInstrumentID: ...,
     *   quoteID: ...,
     *   requestID: ...,
     *   updatedAt: ...,
     * )
     * ```
     *
     * Otherwise ensure the following setters are called
     *
     * ```
     * (new Delivery)
     *   ->withID(...)
     *   ->withCreatedAt(...)
     *   ->withEvent(...)
     *   ->withEventDescription(...)
     *   ->withEventVocabulary(...)
     *   ->withPaymentInstrumentID(...)
     *   ->withQuoteID(...)
     *   ->withRequestID(...)
     *   ->withUpdatedAt(...)
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
        \DateTimeInterface $createdAt,
        string $event,
        string $eventDescription,
        string $eventVocabulary,
        string $paymentInstrumentID,
        string $quoteID,
        string $requestID,
        \DateTimeInterface $updatedAt,
        ?string $webhookURL = null,
    ): self {
        $self = new self;

        $self['id'] = $id;
        $self['createdAt'] = $createdAt;
        $self['event'] = $event;
        $self['eventDescription'] = $eventDescription;
        $self['eventVocabulary'] = $eventVocabulary;
        $self['paymentInstrumentID'] = $paymentInstrumentID;
        $self['quoteID'] = $quoteID;
        $self['requestID'] = $requestID;
        $self['updatedAt'] = $updatedAt;

        null !== $webhookURL && $self['webhookURL'] = $webhookURL;

        return $self;
    }

    /**
     * Unique delivery identifier.
     */
    public function withID(string $id): self
    {
        $self = clone $this;
        $self['id'] = $id;

        return $self;
    }

    /**
     * Creation timestamp (RFC 3339).
     */
    public function withCreatedAt(\DateTimeInterface $createdAt): self
    {
        $self = clone $this;
        $self['createdAt'] = $createdAt;

        return $self;
    }

    /**
     * Current event identifier.
     */
    public function withEvent(string $event): self
    {
        $self = clone $this;
        $self['event'] = $event;

        return $self;
    }

    /**
     * Human-readable description of the current event.
     */
    public function withEventDescription(string $eventDescription): self
    {
        $self = clone $this;
        $self['eventDescription'] = $eventDescription;

        return $self;
    }

    /**
     * Event vocabulary standard in use.
     */
    public function withEventVocabulary(string $eventVocabulary): self
    {
        $self = clone $this;
        $self['eventVocabulary'] = $eventVocabulary;

        return $self;
    }

    /**
     * Reference to the payment instrument used to create this delivery.
     */
    public function withPaymentInstrumentID(string $paymentInstrumentID): self
    {
        $self = clone $this;
        $self['paymentInstrumentID'] = $paymentInstrumentID;

        return $self;
    }

    /**
     * Reference to the accepted quote.
     */
    public function withQuoteID(string $quoteID): self
    {
        $self = clone $this;
        $self['quoteID'] = $quoteID;

        return $self;
    }

    /**
     * Reference to the delivery request.
     */
    public function withRequestID(string $requestID): self
    {
        $self = clone $this;
        $self['requestID'] = $requestID;

        return $self;
    }

    /**
     * Last update timestamp (RFC 3339).
     */
    public function withUpdatedAt(\DateTimeInterface $updatedAt): self
    {
        $self = clone $this;
        $self['updatedAt'] = $updatedAt;

        return $self;
    }

    /**
     * Registered webhook URL, if any.
     */
    public function withWebhookURL(?string $webhookURL): self
    {
        $self = clone $this;
        $self['webhookURL'] = $webhookURL;

        return $self;
    }
}
