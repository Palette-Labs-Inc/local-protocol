<?php

declare(strict_types=1);

namespace LocalProtocol\Merchants\ModifierOption;

use LocalProtocol\Core\Attributes\Optional;
use LocalProtocol\Core\Attributes\Required;
use LocalProtocol\Core\Concerns\SdkModel;
use LocalProtocol\Core\Contracts\BaseModel;
use LocalProtocol\PaymentInstruments\Amount;

/**
 * Modifier item for this option.
 *
 * @phpstan-import-type AmountShape from \LocalProtocol\PaymentInstruments\Amount
 *
 * @phpstan-type ModifierItemShape = array{
 *   id: string,
 *   name: string,
 *   price: Amount|AmountShape,
 *   description?: string|null,
 *   metadata?: array<string,mixed>|null,
 * }
 */
final class ModifierItem implements BaseModel
{
    /** @use SdkModel<ModifierItemShape> */
    use SdkModel;

    /**
     * Modifier item identifier.
     */
    #[Required]
    public string $id;

    /**
     * Modifier item name.
     */
    #[Required]
    public string $name;

    /**
     * Price for this modifier item.
     */
    #[Required]
    public Amount $price;

    /**
     * Optional modifier item description.
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
     * `new ModifierItem()` is missing required properties by the API.
     *
     * To enforce required parameters use
     * ```
     * ModifierItem::with(id: ..., name: ..., price: ...)
     * ```
     *
     * Otherwise ensure the following setters are called
     *
     * ```
     * (new ModifierItem)->withID(...)->withName(...)->withPrice(...)
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
     * @param array<string,mixed>|null $metadata
     */
    public static function with(
        string $id,
        string $name,
        Amount|array $price,
        ?string $description = null,
        ?array $metadata = null,
    ): self {
        $self = new self;

        $self['id'] = $id;
        $self['name'] = $name;
        $self['price'] = $price;

        null !== $description && $self['description'] = $description;
        null !== $metadata && $self['metadata'] = $metadata;

        return $self;
    }

    /**
     * Modifier item identifier.
     */
    public function withID(string $id): self
    {
        $self = clone $this;
        $self['id'] = $id;

        return $self;
    }

    /**
     * Modifier item name.
     */
    public function withName(string $name): self
    {
        $self = clone $this;
        $self['name'] = $name;

        return $self;
    }

    /**
     * Price for this modifier item.
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
     * Optional modifier item description.
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
