<?php

declare(strict_types=1);

namespace LocalProtocol\Merchants;

use LocalProtocol\Core\Attributes\Optional;
use LocalProtocol\Core\Attributes\Required;
use LocalProtocol\Core\Concerns\SdkModel;
use LocalProtocol\Core\Contracts\BaseModel;
use LocalProtocol\Merchants\MerchantGetResponse\Catalog;

/**
 * Merchant catalog payload containing denormalized catalogs.
 *
 * @phpstan-type MerchantGetResponseShape = array{
 *   id: string,
 *   catalogs: list<mixed>,
 *   name: string,
 *   timezone: string,
 *   lastUpdated?: \DateTimeInterface|null,
 *   metadata?: array<string,mixed>|null,
 * }
 */
final class MerchantGetResponse implements BaseModel
{
    /** @use SdkModel<MerchantGetResponseShape> */
    use SdkModel;

    /**
     * Merchant identifier.
     */
    #[Required]
    public string $id;

    /**
     * Catalogs available for the merchant.
     *
     * @var list<mixed> $catalogs
     */
    #[Required(list: Catalog::class)]
    public array $catalogs;

    /**
     * Merchant name.
     */
    #[Required]
    public string $name;

    /**
     * IANA timezone for availability schedules.
     */
    #[Required]
    public string $timezone;

    /**
     * RFC 3339 timestamp of the latest catalog update.
     */
    #[Optional('last_updated')]
    public ?\DateTimeInterface $lastUpdated;

    /**
     * Business-defined custom data.
     *
     * @var array<string,mixed>|null $metadata
     */
    #[Optional(map: 'mixed')]
    public ?array $metadata;

    /**
     * `new MerchantGetResponse()` is missing required properties by the API.
     *
     * To enforce required parameters use
     * ```
     * MerchantGetResponse::with(id: ..., catalogs: ..., name: ..., timezone: ...)
     * ```
     *
     * Otherwise ensure the following setters are called
     *
     * ```
     * (new MerchantGetResponse)
     *   ->withID(...)
     *   ->withCatalogs(...)
     *   ->withName(...)
     *   ->withTimezone(...)
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
     * @param list<mixed> $catalogs
     * @param array<string,mixed>|null $metadata
     */
    public static function with(
        string $id,
        array $catalogs,
        string $name,
        string $timezone,
        ?\DateTimeInterface $lastUpdated = null,
        ?array $metadata = null,
    ): self {
        $self = new self;

        $self['id'] = $id;
        $self['catalogs'] = $catalogs;
        $self['name'] = $name;
        $self['timezone'] = $timezone;

        null !== $lastUpdated && $self['lastUpdated'] = $lastUpdated;
        null !== $metadata && $self['metadata'] = $metadata;

        return $self;
    }

    /**
     * Merchant identifier.
     */
    public function withID(string $id): self
    {
        $self = clone $this;
        $self['id'] = $id;

        return $self;
    }

    /**
     * Catalogs available for the merchant.
     *
     * @param list<mixed> $catalogs
     */
    public function withCatalogs(array $catalogs): self
    {
        $self = clone $this;
        $self['catalogs'] = $catalogs;

        return $self;
    }

    /**
     * Merchant name.
     */
    public function withName(string $name): self
    {
        $self = clone $this;
        $self['name'] = $name;

        return $self;
    }

    /**
     * IANA timezone for availability schedules.
     */
    public function withTimezone(string $timezone): self
    {
        $self = clone $this;
        $self['timezone'] = $timezone;

        return $self;
    }

    /**
     * RFC 3339 timestamp of the latest catalog update.
     */
    public function withLastUpdated(\DateTimeInterface $lastUpdated): self
    {
        $self = clone $this;
        $self['lastUpdated'] = $lastUpdated;

        return $self;
    }

    /**
     * Business-defined custom data.
     *
     * @param array<string,mixed> $metadata
     */
    public function withMetadata(array $metadata): self
    {
        $self = clone $this;
        $self['metadata'] = $metadata;

        return $self;
    }
}
