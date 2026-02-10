<?php

declare(strict_types=1);

namespace LocalProtocol\Requests;

use LocalProtocol\Core\Attributes\Optional;
use LocalProtocol\Core\Concerns\SdkModel;
use LocalProtocol\Core\Contracts\BaseModel;

/**
 * @phpstan-type PostalAddressShape = array{
 *   addressCountry?: string|null,
 *   addressLocality?: string|null,
 *   addressRegion?: string|null,
 *   extendedAddress?: string|null,
 *   firstName?: string|null,
 *   lastName?: string|null,
 *   phoneNumber?: string|null,
 *   postalCode?: string|null,
 *   streetAddress?: string|null,
 * }
 */
final class PostalAddress implements BaseModel
{
    /** @use SdkModel<PostalAddressShape> */
    use SdkModel;

    /**
     * Country (ISO 3166-1 alpha-2 recommended).
     */
    #[Optional('address_country')]
    public ?string $addressCountry;

    /**
     * City or locality.
     */
    #[Optional('address_locality')]
    public ?string $addressLocality;

    /**
     * State, province, or region.
     */
    #[Optional('address_region')]
    public ?string $addressRegion;

    /**
     * Address extension (apartment number, C/O, etc.).
     */
    #[Optional('extended_address')]
    public ?string $extendedAddress;

    /**
     * Contact first name.
     */
    #[Optional('first_name')]
    public ?string $firstName;

    /**
     * Contact last name.
     */
    #[Optional('last_name')]
    public ?string $lastName;

    /**
     * Contact phone number.
     */
    #[Optional('phone_number')]
    public ?string $phoneNumber;

    /**
     * Postal code.
     */
    #[Optional('postal_code')]
    public ?string $postalCode;

    /**
     * The street address.
     */
    #[Optional('street_address')]
    public ?string $streetAddress;

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
        ?string $addressCountry = null,
        ?string $addressLocality = null,
        ?string $addressRegion = null,
        ?string $extendedAddress = null,
        ?string $firstName = null,
        ?string $lastName = null,
        ?string $phoneNumber = null,
        ?string $postalCode = null,
        ?string $streetAddress = null,
    ): self {
        $self = new self;

        null !== $addressCountry && $self['addressCountry'] = $addressCountry;
        null !== $addressLocality && $self['addressLocality'] = $addressLocality;
        null !== $addressRegion && $self['addressRegion'] = $addressRegion;
        null !== $extendedAddress && $self['extendedAddress'] = $extendedAddress;
        null !== $firstName && $self['firstName'] = $firstName;
        null !== $lastName && $self['lastName'] = $lastName;
        null !== $phoneNumber && $self['phoneNumber'] = $phoneNumber;
        null !== $postalCode && $self['postalCode'] = $postalCode;
        null !== $streetAddress && $self['streetAddress'] = $streetAddress;

        return $self;
    }

    /**
     * Country (ISO 3166-1 alpha-2 recommended).
     */
    public function withAddressCountry(string $addressCountry): self
    {
        $self = clone $this;
        $self['addressCountry'] = $addressCountry;

        return $self;
    }

    /**
     * City or locality.
     */
    public function withAddressLocality(string $addressLocality): self
    {
        $self = clone $this;
        $self['addressLocality'] = $addressLocality;

        return $self;
    }

    /**
     * State, province, or region.
     */
    public function withAddressRegion(string $addressRegion): self
    {
        $self = clone $this;
        $self['addressRegion'] = $addressRegion;

        return $self;
    }

    /**
     * Address extension (apartment number, C/O, etc.).
     */
    public function withExtendedAddress(string $extendedAddress): self
    {
        $self = clone $this;
        $self['extendedAddress'] = $extendedAddress;

        return $self;
    }

    /**
     * Contact first name.
     */
    public function withFirstName(string $firstName): self
    {
        $self = clone $this;
        $self['firstName'] = $firstName;

        return $self;
    }

    /**
     * Contact last name.
     */
    public function withLastName(string $lastName): self
    {
        $self = clone $this;
        $self['lastName'] = $lastName;

        return $self;
    }

    /**
     * Contact phone number.
     */
    public function withPhoneNumber(string $phoneNumber): self
    {
        $self = clone $this;
        $self['phoneNumber'] = $phoneNumber;

        return $self;
    }

    /**
     * Postal code.
     */
    public function withPostalCode(string $postalCode): self
    {
        $self = clone $this;
        $self['postalCode'] = $postalCode;

        return $self;
    }

    /**
     * The street address.
     */
    public function withStreetAddress(string $streetAddress): self
    {
        $self = clone $this;
        $self['streetAddress'] = $streetAddress;

        return $self;
    }
}
