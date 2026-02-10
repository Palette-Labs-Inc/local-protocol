<?php

declare(strict_types=1);

namespace LocalProtocol\PaymentInstruments;

use LocalProtocol\Core\Attributes\Optional;
use LocalProtocol\Core\Concerns\SdkModel;
use LocalProtocol\Core\Contracts\BaseModel;

/**
 * @phpstan-type SelectedPaymentInstrumentSelectionStateShape = array{
 *   selected?: bool|null
 * }
 */
final class SelectedPaymentInstrumentSelectionState implements BaseModel
{
    /** @use SdkModel<SelectedPaymentInstrumentSelectionStateShape> */
    use SdkModel;

    /**
     * Whether this instrument is selected by the user.
     */
    #[Optional]
    public ?bool $selected;

    public function __construct()
    {
        $this->initialize();
    }

    /**
     * Construct an instance from the required parameters.
     *
     * You must use named parameters to construct any parameters with a default value.
     */
    public static function with(?bool $selected = null): self
    {
        $self = new self;

        null !== $selected && $self['selected'] = $selected;

        return $self;
    }

    /**
     * Whether this instrument is selected by the user.
     */
    public function withSelected(bool $selected): self
    {
        $self = clone $this;
        $self['selected'] = $selected;

        return $self;
    }
}
