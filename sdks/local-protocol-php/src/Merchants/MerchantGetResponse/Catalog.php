<?php

declare(strict_types=1);

namespace LocalProtocol\Merchants\MerchantGetResponse;

use LocalProtocol\Core\Attributes\Optional;
use LocalProtocol\Core\Attributes\Required;
use LocalProtocol\Core\Concerns\SdkModel;
use LocalProtocol\Core\Contracts\BaseModel;
use LocalProtocol\Merchants\Availability;
use LocalProtocol\Merchants\CatalogCategory;
use LocalProtocol\Merchants\MerchantGetResponse\Catalog\Item;

/**
 * A catalog containing embedded categories, items, availability, and fulfillment configuration.
 *
 * @phpstan-import-type AvailabilityShape from \LocalProtocol\Merchants\Availability
 *
 * @phpstan-type CatalogShape = array{
 *   id: string,
 *   categories: list<mixed>,
 *   name: string,
 *   availability?: null|Availability|AvailabilityShape,
 *   description?: string|null,
 *   items?: list<mixed>|null,
 *   metadata?: array<string,mixed>|null,
 * }
 */
final class Catalog implements BaseModel
{
    /** @use SdkModel<CatalogShape> */
    use SdkModel;

    /**
     * Catalog identifier.
     */
    #[Required]
    public string $id;

    /**
     * Ordered top-level categories.
     *
     * @var list<mixed> $categories
     */
    #[Required(list: CatalogCategory::class)]
    public array $categories;

    /**
     * Catalog name.
     */
    #[Required]
    public string $name;

    /**
     * Catalog-wide availability override.
     */
    #[Optional]
    public ?Availability $availability;

    /**
     * Catalog description.
     */
    #[Optional]
    public ?string $description;

    /**
     * Items not assigned to a category.
     *
     * @var list<mixed>|null $items
     */
    #[Optional(list: Item::class)]
    public ?array $items;

    /**
     * Business-defined custom data.
     *
     * @var array<string,mixed>|null $metadata
     */
    #[Optional(map: 'mixed')]
    public ?array $metadata;

    /**
     * `new Catalog()` is missing required properties by the API.
     *
     * To enforce required parameters use
     * ```
     * Catalog::with(id: ..., categories: ..., name: ...)
     * ```
     *
     * Otherwise ensure the following setters are called
     *
     * ```
     * (new Catalog)->withID(...)->withCategories(...)->withName(...)
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
     * @param list<mixed> $categories
     * @param Availability|AvailabilityShape|null $availability
     * @param list<mixed>|null $items
     * @param array<string,mixed>|null $metadata
     */
    public static function with(
        string $id,
        array $categories,
        string $name,
        Availability|array|null $availability = null,
        ?string $description = null,
        ?array $items = null,
        ?array $metadata = null,
    ): self {
        $self = new self;

        $self['id'] = $id;
        $self['categories'] = $categories;
        $self['name'] = $name;

        null !== $availability && $self['availability'] = $availability;
        null !== $description && $self['description'] = $description;
        null !== $items && $self['items'] = $items;
        null !== $metadata && $self['metadata'] = $metadata;

        return $self;
    }

    /**
     * Catalog identifier.
     */
    public function withID(string $id): self
    {
        $self = clone $this;
        $self['id'] = $id;

        return $self;
    }

    /**
     * Ordered top-level categories.
     *
     * @param list<mixed> $categories
     */
    public function withCategories(array $categories): self
    {
        $self = clone $this;
        $self['categories'] = $categories;

        return $self;
    }

    /**
     * Catalog name.
     */
    public function withName(string $name): self
    {
        $self = clone $this;
        $self['name'] = $name;

        return $self;
    }

    /**
     * Catalog-wide availability override.
     *
     * @param Availability|AvailabilityShape $availability
     */
    public function withAvailability(Availability|array $availability): self
    {
        $self = clone $this;
        $self['availability'] = $availability;

        return $self;
    }

    /**
     * Catalog description.
     */
    public function withDescription(string $description): self
    {
        $self = clone $this;
        $self['description'] = $description;

        return $self;
    }

    /**
     * Items not assigned to a category.
     *
     * @param list<mixed> $items
     */
    public function withItems(array $items): self
    {
        $self = clone $this;
        $self['items'] = $items;

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
