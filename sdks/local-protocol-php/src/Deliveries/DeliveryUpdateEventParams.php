<?php

declare(strict_types=1);

namespace LocalProtocol\Deliveries;

use LocalProtocol\Core\Attributes\Required;
use LocalProtocol\Core\Concerns\SdkModel;
use LocalProtocol\Core\Concerns\SdkParams;
use LocalProtocol\Core\Contracts\BaseModel;

/**
 * Transition a delivery to a new event state. If a webhook URL was registered, the server pushes an event notification in the background.
 *
 * @see LocalProtocol\Services\DeliveriesService::updateEvent()
 *
 * @phpstan-type DeliveryUpdateEventParamsShape = array{
 *   event: string, eventDescription: string
 * }
 */
final class DeliveryUpdateEventParams implements BaseModel
{
    /** @use SdkModel<DeliveryUpdateEventParamsShape> */
    use SdkModel;
    use SdkParams;

    /**
     * Event identifier from the delivery's event vocabulary.
     */
    #[Required]
    public string $event;

    /**
     * Human-readable event description.
     */
    #[Required('event_description')]
    public string $eventDescription;

    /**
     * `new DeliveryUpdateEventParams()` is missing required properties by the API.
     *
     * To enforce required parameters use
     * ```
     * DeliveryUpdateEventParams::with(event: ..., eventDescription: ...)
     * ```
     *
     * Otherwise ensure the following setters are called
     *
     * ```
     * (new DeliveryUpdateEventParams)->withEvent(...)->withEventDescription(...)
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
    public static function with(string $event, string $eventDescription): self
    {
        $self = new self;

        $self['event'] = $event;
        $self['eventDescription'] = $eventDescription;

        return $self;
    }

    /**
     * Event identifier from the delivery's event vocabulary.
     */
    public function withEvent(string $event): self
    {
        $self = clone $this;
        $self['event'] = $event;

        return $self;
    }

    /**
     * Human-readable event description.
     */
    public function withEventDescription(string $eventDescription): self
    {
        $self = clone $this;
        $self['eventDescription'] = $eventDescription;

        return $self;
    }
}
