<?php

declare(strict_types=1);

namespace LocalProtocol\Merchants;

use LocalProtocol\Core\Attributes\Optional;
use LocalProtocol\Core\Attributes\Required;
use LocalProtocol\Core\Concerns\SdkModel;
use LocalProtocol\Core\Contracts\BaseModel;
use LocalProtocol\Merchants\CatalogCategory\Item;

/**
 * A category grouping items in a catalog.
 *
 * @phpstan-import-type AvailabilityShape from \LocalProtocol\Merchants\Availability
 *
 * @phpstan-type CatalogCategoryShape = array{
 *   id: string,
 *   items: list<mixed>,
 *   name: string,
 *   availability?: null|Availability|AvailabilityShape,
 *   categories?: list<mixed>|null,
 *   description?: string|null,
 *   metadata?: array<string,mixed>|null,
 * }
 */
final class CatalogCategory implements BaseModel
{
    /** @use SdkModel<CatalogCategoryShape> */
    use SdkModel;

    /**
     * Category identifier.
     */
    #[Required]
    public string $id;

    /**
     * Ordered items in this category.
     *
     * @var list<mixed> $items
     */
    #[Required(list: Item::class)]
    public array $items;

    /**
     * Category display name.
     */
    #[Required]
    public string $name;

    /**
     * Category availability.
     */
    #[Optional]
    public ?Availability $availability;

    /**
     * Ordered child categories for nested category trees.
     *
     * @var list<mixed>|null $categories
     */
    #[Optional(list: CatalogCategory::class)]
    public ?array $categories;

    /**
     * Optional category description.
     */
    #[Optional]
    public ?string $description;

    /**
     * Business-defined custom data.
     *
     * @var array<string,mixed>|null $metadata
     */
    #[Optional(map: 'mixed')]
    public ?array $metadata;

    /**
     * `new CatalogCategory()` is missing required properties by the API.
     *
     * To enforce required parameters use
     * ```
     * CatalogCategory::with(id: ..., items: ..., name: ...)
     * ```
     *
     * Otherwise ensure the following setters are called
     *
     * ```
     * (new CatalogCategory)->withID(...)->withItems(...)->withName(...)
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
     * @param list<mixed> $items
     * @param Availability|AvailabilityShape|null $availability
     * @param list<mixed>|null $categories
     * @param array<string,mixed>|null $metadata
     */
    public static function with(
        string $id,
        array $items,
        string $name,
        Availability|array|null $availability = null,
        ?array $categories = null,
        ?string $description = null,
        ?array $metadata = null,
    ): self {
        $self = new self;

        $self['id'] = $id;
        $self['items'] = $items;
        $self['name'] = $name;

        null !== $availability && $self['availability'] = $availability;
        null !== $categories && $self['categories'] = $categories;
        null !== $description && $self['description'] = $description;
        null !== $metadata && $self['metadata'] = $metadata;

        return $self;
    }

    /**
     * Category identifier.
     */
    public function withID(string $id): self
    {
        $self = clone $this;
        $self['id'] = $id;

        return $self;
    }

    /**
     * Ordered items in this category.
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
     * Category display name.
     */
    public function withName(string $name): self
    {
        $self = clone $this;
        $self['name'] = $name;

        return $self;
    }

    /**
     * Category availability.
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
     * Ordered child categories for nested category trees.
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
     * Optional category description.
     */
    public function withDescription(string $description): self
    {
        $self = clone $this;
        $self['description'] = $description;

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
