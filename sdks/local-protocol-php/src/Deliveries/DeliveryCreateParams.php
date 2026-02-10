<?php

declare(strict_types=1);

namespace LocalProtocol\Deliveries;

use LocalProtocol\Core\Attributes\Optional;
use LocalProtocol\Core\Attributes\Required;
use LocalProtocol\Core\Concerns\SdkModel;
use LocalProtocol\Core\Concerns\SdkParams;
use LocalProtocol\Core\Contracts\BaseModel;

/**
 * Accept a quote and create a delivery. The `nonce` field provides idempotency.
 *
 * @see LocalProtocol\Services\DeliveriesService::create()
 *
 * @phpstan-type DeliveryCreateParamsShape = array{
 *   nonce: string,
 *   quoteID: string,
 *   requestID: string,
 *   eventVocabulary?: string|null,
 *   webhookURL?: string|null,
 * }
 */
final class DeliveryCreateParams implements BaseModel
{
    /** @use SdkModel<DeliveryCreateParamsShape> */
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
    #[Required('quote_id')]
    public string $quoteID;

    /**
     * The delivery request to fulfill.
     */
    #[Required('request_id')]
    public string $requestID;

    /**
     * Event vocabulary standard to use.
     */
    #[Optional('event_vocabulary')]
    public ?string $eventVocabulary;

    /**
     * Optional URL to receive delivery event webhook notifications.
     */
    #[Optional('webhook_url', nullable: true)]
    public ?string $webhookURL;

    /**
     * `new DeliveryCreateParams()` is missing required properties by the API.
     *
     * To enforce required parameters use
     * ```
     * DeliveryCreateParams::with(nonce: ..., quoteID: ..., requestID: ...)
     * ```
     *
     * Otherwise ensure the following setters are called
     *
     * ```
     * (new DeliveryCreateParams)->withNonce(...)->withQuoteID(...)->withRequestID(...)
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
        string $quoteID,
        string $requestID,
        ?string $eventVocabulary = null,
        ?string $webhookURL = null,
    ): self {
        $self = new self;

        $self['nonce'] = $nonce;
        $self['quoteID'] = $quoteID;
        $self['requestID'] = $requestID;

        null !== $eventVocabulary && $self['eventVocabulary'] = $eventVocabulary;
        null !== $webhookURL && $self['webhookURL'] = $webhookURL;

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
    public function withQuoteID(string $quoteID): self
    {
        $self = clone $this;
        $self['quoteID'] = $quoteID;

        return $self;
    }

    /**
     * The delivery request to fulfill.
     */
    public function withRequestID(string $requestID): self
    {
        $self = clone $this;
        $self['requestID'] = $requestID;

        return $self;
    }

    /**
     * Event vocabulary standard to use.
     */
    public function withEventVocabulary(string $eventVocabulary): self
    {
        $self = clone $this;
        $self['eventVocabulary'] = $eventVocabulary;

        return $self;
    }

    /**
     * Optional URL to receive delivery event webhook notifications.
     */
    public function withWebhookURL(?string $webhookURL): self
    {
        $self = clone $this;
        $self['webhookURL'] = $webhookURL;

        return $self;
    }
}
