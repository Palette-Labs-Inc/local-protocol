<?php

declare(strict_types=1);

namespace LocalProtocol\Requests;

use LocalProtocol\Core\Attributes\Optional;
use LocalProtocol\Core\Concerns\SdkModel;
use LocalProtocol\Core\Contracts\BaseModel;

/**
 * A location specified by coordinates and/or postal address. At least one must be provided.
 *
 * @phpstan-import-type CoordinatesShape from \LocalProtocol\Requests\Coordinates
 * @phpstan-import-type PostalAddressShape from \LocalProtocol\Requests\PostalAddress
 *
 * @phpstan-type LocationShape = array{
 *   coordinates?: null|Coordinates|CoordinatesShape,
 *   postalAddress?: null|PostalAddress|PostalAddressShape,
 * }
 */
final class Location implements BaseModel
{
    /** @use SdkModel<LocationShape> */
    use SdkModel;

    /**
     * Geographic coordinates.
     */
    #[Optional]
    public ?Coordinates $coordinates;

    #[Optional('postal_address')]
    public ?PostalAddress $postalAddress;

    public function __construct()
    {
        $this->initialize();
    }

    /**
     * Construct an instance from the required parameters.
     *
     * You must use named parameters to construct any parameters with a default value.
     *
     * @param Coordinates|CoordinatesShape|null $coordinates
     * @param PostalAddress|PostalAddressShape|null $postalAddress
     */
    public static function with(
        Coordinates|array|null $coordinates = null,
        PostalAddress|array|null $postalAddress = null,
    ): self {
        $self = new self;

        null !== $coordinates && $self['coordinates'] = $coordinates;
        null !== $postalAddress && $self['postalAddress'] = $postalAddress;

        return $self;
    }

    /**
     * Geographic coordinates.
     *
     * @param Coordinates|CoordinatesShape $coordinates
     */
    public function withCoordinates(Coordinates|array $coordinates): self
    {
        $self = clone $this;
        $self['coordinates'] = $coordinates;

        return $self;
    }

    /**
     * @param PostalAddress|PostalAddressShape $postalAddress
     */
    public function withPostalAddress(PostalAddress|array $postalAddress): self
    {
        $self = clone $this;
        $self['postalAddress'] = $postalAddress;

        return $self;
    }
}
