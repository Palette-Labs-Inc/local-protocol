<?php

declare(strict_types=1);

namespace LocalProtocol\Requests\Location;

use LocalProtocol\Core\Attributes\Required;
use LocalProtocol\Core\Concerns\SdkModel;
use LocalProtocol\Core\Contracts\BaseModel;

/**
 * Geographic coordinates.
 *
 * @phpstan-type CoordinatesShape = array{latitude: float, longitude: float}
 */
final class Coordinates implements BaseModel
{
    /** @use SdkModel<CoordinatesShape> */
    use SdkModel;

    /**
     * Latitude in decimal degrees.
     */
    #[Required]
    public float $latitude;

    /**
     * Longitude in decimal degrees.
     */
    #[Required]
    public float $longitude;

    /**
     * `new Coordinates()` is missing required properties by the API.
     *
     * To enforce required parameters use
     * ```
     * Coordinates::with(latitude: ..., longitude: ...)
     * ```
     *
     * Otherwise ensure the following setters are called
     *
     * ```
     * (new Coordinates)->withLatitude(...)->withLongitude(...)
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
    public static function with(float $latitude, float $longitude): self
    {
        $self = new self;

        $self['latitude'] = $latitude;
        $self['longitude'] = $longitude;

        return $self;
    }

    /**
     * Latitude in decimal degrees.
     */
    public function withLatitude(float $latitude): self
    {
        $self = clone $this;
        $self['latitude'] = $latitude;

        return $self;
    }

    /**
     * Longitude in decimal degrees.
     */
    public function withLongitude(float $longitude): self
    {
        $self = clone $this;
        $self['longitude'] = $longitude;

        return $self;
    }
}
