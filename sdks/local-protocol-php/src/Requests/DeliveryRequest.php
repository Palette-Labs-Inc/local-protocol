<?php

declare(strict_types=1);

namespace LocalProtocol\Requests;

use LocalProtocol\Core\Attributes\Optional;
use LocalProtocol\Core\Attributes\Required;
use LocalProtocol\Core\Concerns\SdkModel;
use LocalProtocol\Core\Contracts\BaseModel;

/**
 * A delivery request.
 *
 * @phpstan-import-type LocationShape from \LocalProtocol\Requests\Location
 *
 * @phpstan-type DeliveryRequestShape = array{
 *   id: string,
 *   dropoffLocation: Location|LocationShape,
 *   dropoffTime: \DateTimeInterface,
 *   nonce: string,
 *   pickupLocation: Location|LocationShape,
 *   pickupTime: \DateTimeInterface,
 *   dropoffInstructions?: string|null,
 *   pickupInstructions?: string|null,
 * }
 */
final class DeliveryRequest implements BaseModel
{
    /** @use SdkModel<DeliveryRequestShape> */
    use SdkModel;

    /**
     * Unique request identifier.
     */
    #[Required]
    public string $id;

    /**
     * A location specified by coordinates and/or postal address. At least one must be provided.
     */
    #[Required('dropoff_location')]
    public Location $dropoffLocation;

    /**
     * Requested dropoff time (RFC 3339).
     */
    #[Required('dropoff_time')]
    public \DateTimeInterface $dropoffTime;

    /**
     * Client-generated idempotency key.
     */
    #[Required]
    public string $nonce;

    /**
     * A location specified by coordinates and/or postal address. At least one must be provided.
     */
    #[Required('pickup_location')]
    public Location $pickupLocation;

    /**
     * Requested pickup time (RFC 3339).
     */
    #[Required('pickup_time')]
    public \DateTimeInterface $pickupTime;

    /**
     * Dropoff directions, access codes, or delivery notes.
     */
    #[Optional('dropoff_instructions')]
    public ?string $dropoffInstructions;

    /**
     * Pickup directions, access codes, or handling notes.
     */
    #[Optional('pickup_instructions')]
    public ?string $pickupInstructions;

    /**
     * `new DeliveryRequest()` is missing required properties by the API.
     *
     * To enforce required parameters use
     * ```
     * DeliveryRequest::with(
     *   id: ...,
     *   dropoffLocation: ...,
     *   dropoffTime: ...,
     *   nonce: ...,
     *   pickupLocation: ...,
     *   pickupTime: ...,
     * )
     * ```
     *
     * Otherwise ensure the following setters are called
     *
     * ```
     * (new DeliveryRequest)
     *   ->withID(...)
     *   ->withDropoffLocation(...)
     *   ->withDropoffTime(...)
     *   ->withNonce(...)
     *   ->withPickupLocation(...)
     *   ->withPickupTime(...)
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
     * @param Location|LocationShape $dropoffLocation
     * @param Location|LocationShape $pickupLocation
     */
    public static function with(
        string $id,
        Location|array $dropoffLocation,
        \DateTimeInterface $dropoffTime,
        string $nonce,
        Location|array $pickupLocation,
        \DateTimeInterface $pickupTime,
        ?string $dropoffInstructions = null,
        ?string $pickupInstructions = null,
    ): self {
        $self = new self;

        $self['id'] = $id;
        $self['dropoffLocation'] = $dropoffLocation;
        $self['dropoffTime'] = $dropoffTime;
        $self['nonce'] = $nonce;
        $self['pickupLocation'] = $pickupLocation;
        $self['pickupTime'] = $pickupTime;

        null !== $dropoffInstructions && $self['dropoffInstructions'] = $dropoffInstructions;
        null !== $pickupInstructions && $self['pickupInstructions'] = $pickupInstructions;

        return $self;
    }

    /**
     * Unique request identifier.
     */
    public function withID(string $id): self
    {
        $self = clone $this;
        $self['id'] = $id;

        return $self;
    }

    /**
     * A location specified by coordinates and/or postal address. At least one must be provided.
     *
     * @param Location|LocationShape $dropoffLocation
     */
    public function withDropoffLocation(Location|array $dropoffLocation): self
    {
        $self = clone $this;
        $self['dropoffLocation'] = $dropoffLocation;

        return $self;
    }

    /**
     * Requested dropoff time (RFC 3339).
     */
    public function withDropoffTime(\DateTimeInterface $dropoffTime): self
    {
        $self = clone $this;
        $self['dropoffTime'] = $dropoffTime;

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
     * A location specified by coordinates and/or postal address. At least one must be provided.
     *
     * @param Location|LocationShape $pickupLocation
     */
    public function withPickupLocation(Location|array $pickupLocation): self
    {
        $self = clone $this;
        $self['pickupLocation'] = $pickupLocation;

        return $self;
    }

    /**
     * Requested pickup time (RFC 3339).
     */
    public function withPickupTime(\DateTimeInterface $pickupTime): self
    {
        $self = clone $this;
        $self['pickupTime'] = $pickupTime;

        return $self;
    }

    /**
     * Dropoff directions, access codes, or delivery notes.
     */
    public function withDropoffInstructions(string $dropoffInstructions): self
    {
        $self = clone $this;
        $self['dropoffInstructions'] = $dropoffInstructions;

        return $self;
    }

    /**
     * Pickup directions, access codes, or handling notes.
     */
    public function withPickupInstructions(string $pickupInstructions): self
    {
        $self = clone $this;
        $self['pickupInstructions'] = $pickupInstructions;

        return $self;
    }
}
