<?php

declare(strict_types=1);

namespace LocalProtocol\Merchants\CatalogCategory;

use LocalProtocol\Core\Attributes\Optional;
use LocalProtocol\Core\Attributes\Required;
use LocalProtocol\Core\Concerns\SdkModel;
use LocalProtocol\Core\Contracts\BaseModel;
use LocalProtocol\Merchants\Availability;
use LocalProtocol\Merchants\CatalogCategory\Item\Media;
use LocalProtocol\Merchants\ModifierGroup;
use LocalProtocol\PaymentInstruments\Amount;

/**
 * A menu item with embedded modifier groups.
 *
 * @phpstan-import-type AmountShape from \LocalProtocol\PaymentInstruments\Amount
 * @phpstan-import-type AvailabilityShape from \LocalProtocol\Merchants\Availability
 * @phpstan-import-type MediaShape from \LocalProtocol\Merchants\CatalogCategory\Item\Media
 *
 * @phpstan-type ItemShape = array{
 *   id: string,
 *   description: string,
 *   name: string,
 *   price: Amount|AmountShape,
 *   availability?: null|Availability|AvailabilityShape,
 *   media?: list<Media|MediaShape>|null,
 *   metadata?: array<string,mixed>|null,
 *   modifierGroups?: list<mixed>|null,
 * }
 */
final class Item implements BaseModel
{
    /** @use SdkModel<ItemShape> */
    use SdkModel;

    /**
     * Item identifier.
     */
    #[Required]
    public string $id;

    /**
     * Item description.
     */
    #[Required]
    public string $description;

    /**
     * Item name.
     */
    #[Required]
    public string $name;

    /**
     * Base price for the item.
     */
    #[Required]
    public Amount $price;

    /**
     * Item availability.
     */
    #[Optional]
    public ?Availability $availability;

    /**
     * Item media (images, videos, 3D models).
     *
     * @var list<Media>|null $media
     */
    #[Optional(list: Media::class)]
    public ?array $media;

    /**
     * Business-defined custom data.
     *
     * @var array<string,mixed>|null $metadata
     */
    #[Optional(map: 'mixed')]
    public ?array $metadata;

    /**
     * Modifier groups available for this item.
     *
     * @var list<mixed>|null $modifierGroups
     */
    #[Optional('modifier_groups', list: ModifierGroup::class)]
    public ?array $modifierGroups;

    /**
     * `new Item()` is missing required properties by the API.
     *
     * To enforce required parameters use
     * ```
     * Item::with(id: ..., description: ..., name: ..., price: ...)
     * ```
     *
     * Otherwise ensure the following setters are called
     *
     * ```
     * (new Item)->withID(...)->withDescription(...)->withName(...)->withPrice(...)
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
     * @param Amount|AmountShape $price
     * @param Availability|AvailabilityShape|null $availability
     * @param list<Media|MediaShape>|null $media
     * @param array<string,mixed>|null $metadata
     * @param list<mixed>|null $modifierGroups
     */
    public static function with(
        string $id,
        string $description,
        string $name,
        Amount|array $price,
        Availability|array|null $availability = null,
        ?array $media = null,
        ?array $metadata = null,
        ?array $modifierGroups = null,
    ): self {
        $self = new self;

        $self['id'] = $id;
        $self['description'] = $description;
        $self['name'] = $name;
        $self['price'] = $price;

        null !== $availability && $self['availability'] = $availability;
        null !== $media && $self['media'] = $media;
        null !== $metadata && $self['metadata'] = $metadata;
        null !== $modifierGroups && $self['modifierGroups'] = $modifierGroups;

        return $self;
    }

    /**
     * Item identifier.
     */
    public function withID(string $id): self
    {
        $self = clone $this;
        $self['id'] = $id;

        return $self;
    }

    /**
     * Item description.
     */
    public function withDescription(string $description): self
    {
        $self = clone $this;
        $self['description'] = $description;

        return $self;
    }

    /**
     * Item name.
     */
    public function withName(string $name): self
    {
        $self = clone $this;
        $self['name'] = $name;

        return $self;
    }

    /**
     * Base price for the item.
     *
     * @param Amount|AmountShape $price
     */
    public function withPrice(Amount|array $price): self
    {
        $self = clone $this;
        $self['price'] = $price;

        return $self;
    }

    /**
     * Item availability.
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
     * Item media (images, videos, 3D models).
     *
     * @param list<Media|MediaShape> $media
     */
    public function withMedia(array $media): self
    {
        $self = clone $this;
        $self['media'] = $media;

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

    /**
     * Modifier groups available for this item.
     *
     * @param list<mixed> $modifierGroups
     */
    public function withModifierGroups(array $modifierGroups): self
    {
        $self = clone $this;
        $self['modifierGroups'] = $modifierGroups;

        return $self;
    }
}
