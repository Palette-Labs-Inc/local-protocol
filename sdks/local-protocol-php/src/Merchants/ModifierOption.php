<?php

declare(strict_types=1);

namespace LocalProtocol\Merchants;

use LocalProtocol\Core\Attributes\Optional;
use LocalProtocol\Core\Attributes\Required;
use LocalProtocol\Core\Concerns\SdkModel;
use LocalProtocol\Core\Contracts\BaseModel;
use LocalProtocol\Merchants\ModifierOption\ModifierItem;

/**
 * Selectable option within a modifier group.
 *
 * @phpstan-import-type ModifierItemShape from \LocalProtocol\Merchants\ModifierOption\ModifierItem
 *
 * @phpstan-type ModifierOptionShape = array{
 *   id: string,
 *   modifierItem: ModifierItem|ModifierItemShape,
 *   childModifierGroups?: list<mixed>|null,
 *   isDefault?: bool|null,
 *   metadata?: array<string,mixed>|null,
 * }
 */
final class ModifierOption implements BaseModel
{
    /** @use SdkModel<ModifierOptionShape> */
    use SdkModel;

    /**
     * Modifier option identifier.
     */
    #[Required]
    public string $id;

    /**
     * Modifier item for this option.
     */
    #[Required('modifier_item')]
    public ModifierItem $modifierItem;

    /**
     * Nested modifier groups required after selecting this option.
     *
     * @var list<mixed>|null $childModifierGroups
     */
    #[Optional('child_modifier_groups', list: ModifierGroup::class)]
    public ?array $childModifierGroups;

    /**
     * Whether this option is selected by default.
     */
    #[Optional('is_default')]
    public ?bool $isDefault;

    /**
     * Business-defined custom data.
     *
     * @var array<string,mixed>|null $metadata
     */
    #[Optional(map: 'mixed')]
    public ?array $metadata;

    /**
     * `new ModifierOption()` is missing required properties by the API.
     *
     * To enforce required parameters use
     * ```
     * ModifierOption::with(id: ..., modifierItem: ...)
     * ```
     *
     * Otherwise ensure the following setters are called
     *
     * ```
     * (new ModifierOption)->withID(...)->withModifierItem(...)
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
     * @param ModifierItem|ModifierItemShape $modifierItem
     * @param list<mixed>|null $childModifierGroups
     * @param array<string,mixed>|null $metadata
     */
    public static function with(
        string $id,
        ModifierItem|array $modifierItem,
        ?array $childModifierGroups = null,
        ?bool $isDefault = null,
        ?array $metadata = null,
    ): self {
        $self = new self;

        $self['id'] = $id;
        $self['modifierItem'] = $modifierItem;

        null !== $childModifierGroups && $self['childModifierGroups'] = $childModifierGroups;
        null !== $isDefault && $self['isDefault'] = $isDefault;
        null !== $metadata && $self['metadata'] = $metadata;

        return $self;
    }

    /**
     * Modifier option identifier.
     */
    public function withID(string $id): self
    {
        $self = clone $this;
        $self['id'] = $id;

        return $self;
    }

    /**
     * Modifier item for this option.
     *
     * @param ModifierItem|ModifierItemShape $modifierItem
     */
    public function withModifierItem(ModifierItem|array $modifierItem): self
    {
        $self = clone $this;
        $self['modifierItem'] = $modifierItem;

        return $self;
    }

    /**
     * Nested modifier groups required after selecting this option.
     *
     * @param list<mixed> $childModifierGroups
     */
    public function withChildModifierGroups(array $childModifierGroups): self
    {
        $self = clone $this;
        $self['childModifierGroups'] = $childModifierGroups;

        return $self;
    }

    /**
     * Whether this option is selected by default.
     */
    public function withIsDefault(bool $isDefault): self
    {
        $self = clone $this;
        $self['isDefault'] = $isDefault;

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
