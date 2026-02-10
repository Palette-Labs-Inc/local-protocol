<?php

declare(strict_types=1);

namespace LocalProtocol\Merchants;

use LocalProtocol\Core\Attributes\Optional;
use LocalProtocol\Core\Attributes\Required;
use LocalProtocol\Core\Concerns\SdkModel;
use LocalProtocol\Core\Contracts\BaseModel;

/**
 * Group of modifier options with selection constraints.
 *
 * @phpstan-type ModifierGroupShape = array{
 *   id: string,
 *   modifierOptions: list<mixed>,
 *   name: string,
 *   allowQuantities?: bool|null,
 *   description?: string|null,
 *   maxPerModifier?: int|null,
 *   maximumSelections?: int|null,
 *   metadata?: array<string,mixed>|null,
 *   minimumSelections?: int|null,
 *   type?: string|null,
 * }
 */
final class ModifierGroup implements BaseModel
{
    /** @use SdkModel<ModifierGroupShape> */
    use SdkModel;

    /**
     * Modifier group identifier.
     */
    #[Required]
    public string $id;

    /**
     * Ordered modifier options within this group.
     *
     * @var list<mixed> $modifierOptions
     */
    #[Required('modifier_options', list: ModifierOption::class)]
    public array $modifierOptions;

    /**
     * Display name for the modifier group.
     */
    #[Required]
    public string $name;

    /**
     * Whether options can be selected with quantities > 1.
     */
    #[Optional('allow_quantities')]
    public ?bool $allowQuantities;

    /**
     * Optional modifier group description.
     */
    #[Optional]
    public ?string $description;

    /**
     * Maximum quantity per modifier option.
     */
    #[Optional('max_per_modifier')]
    public ?int $maxPerModifier;

    /**
     * Maximum selections allowed.
     */
    #[Optional('maximum_selections')]
    public ?int $maximumSelections;

    /**
     * Business-defined custom data.
     *
     * @var array<string,mixed>|null $metadata
     */
    #[Optional(map: 'mixed')]
    public ?array $metadata;

    /**
     * Minimum selections required.
     */
    #[Optional('minimum_selections')]
    public ?int $minimumSelections;

    /**
     * Modifier group type classification.
     */
    #[Optional]
    public ?string $type;

    /**
     * `new ModifierGroup()` is missing required properties by the API.
     *
     * To enforce required parameters use
     * ```
     * ModifierGroup::with(id: ..., modifierOptions: ..., name: ...)
     * ```
     *
     * Otherwise ensure the following setters are called
     *
     * ```
     * (new ModifierGroup)->withID(...)->withModifierOptions(...)->withName(...)
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
     * @param list<mixed> $modifierOptions
     * @param array<string,mixed>|null $metadata
     */
    public static function with(
        string $id,
        array $modifierOptions,
        string $name,
        ?bool $allowQuantities = null,
        ?string $description = null,
        ?int $maxPerModifier = null,
        ?int $maximumSelections = null,
        ?array $metadata = null,
        ?int $minimumSelections = null,
        ?string $type = null,
    ): self {
        $self = new self;

        $self['id'] = $id;
        $self['modifierOptions'] = $modifierOptions;
        $self['name'] = $name;

        null !== $allowQuantities && $self['allowQuantities'] = $allowQuantities;
        null !== $description && $self['description'] = $description;
        null !== $maxPerModifier && $self['maxPerModifier'] = $maxPerModifier;
        null !== $maximumSelections && $self['maximumSelections'] = $maximumSelections;
        null !== $metadata && $self['metadata'] = $metadata;
        null !== $minimumSelections && $self['minimumSelections'] = $minimumSelections;
        null !== $type && $self['type'] = $type;

        return $self;
    }

    /**
     * Modifier group identifier.
     */
    public function withID(string $id): self
    {
        $self = clone $this;
        $self['id'] = $id;

        return $self;
    }

    /**
     * Ordered modifier options within this group.
     *
     * @param list<mixed> $modifierOptions
     */
    public function withModifierOptions(array $modifierOptions): self
    {
        $self = clone $this;
        $self['modifierOptions'] = $modifierOptions;

        return $self;
    }

    /**
     * Display name for the modifier group.
     */
    public function withName(string $name): self
    {
        $self = clone $this;
        $self['name'] = $name;

        return $self;
    }

    /**
     * Whether options can be selected with quantities > 1.
     */
    public function withAllowQuantities(bool $allowQuantities): self
    {
        $self = clone $this;
        $self['allowQuantities'] = $allowQuantities;

        return $self;
    }

    /**
     * Optional modifier group description.
     */
    public function withDescription(string $description): self
    {
        $self = clone $this;
        $self['description'] = $description;

        return $self;
    }

    /**
     * Maximum quantity per modifier option.
     */
    public function withMaxPerModifier(int $maxPerModifier): self
    {
        $self = clone $this;
        $self['maxPerModifier'] = $maxPerModifier;

        return $self;
    }

    /**
     * Maximum selections allowed.
     */
    public function withMaximumSelections(int $maximumSelections): self
    {
        $self = clone $this;
        $self['maximumSelections'] = $maximumSelections;

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
     * Minimum selections required.
     */
    public function withMinimumSelections(int $minimumSelections): self
    {
        $self = clone $this;
        $self['minimumSelections'] = $minimumSelections;

        return $self;
    }

    /**
     * Modifier group type classification.
     */
    public function withType(string $type): self
    {
        $self = clone $this;
        $self['type'] = $type;

        return $self;
    }
}
