<?php

declare(strict_types=1);

namespace LocalProtocol\PaymentInstruments;

use LocalProtocol\Core\Attributes\Optional;
use LocalProtocol\Core\Concerns\SdkModel;
use LocalProtocol\Core\Contracts\BaseModel;

/**
 * Payment configuration containing instruments.
 *
 * @phpstan-import-type SelectedPaymentInstrumentShape from \LocalProtocol\PaymentInstruments\SelectedPaymentInstrument
 *
 * @phpstan-type PaymentShape = array{
 *   instruments?: list<SelectedPaymentInstrument|SelectedPaymentInstrumentShape>|null,
 * }
 */
final class Payment implements BaseModel
{
    /** @use SdkModel<PaymentShape> */
    use SdkModel;

    /**
     * Payment instruments available. Each instrument is associated with a handler via handler_id.
     *
     * @var list<SelectedPaymentInstrument>|null $instruments
     */
    #[Optional(list: SelectedPaymentInstrument::class)]
    public ?array $instruments;

    public function __construct()
    {
        $this->initialize();
    }

    /**
     * Construct an instance from the required parameters.
     *
     * You must use named parameters to construct any parameters with a default value.
     *
     * @param list<SelectedPaymentInstrument|SelectedPaymentInstrumentShape>|null $instruments
     */
    public static function with(?array $instruments = null): self
    {
        $self = new self;

        null !== $instruments && $self['instruments'] = $instruments;

        return $self;
    }

    /**
     * Payment instruments available. Each instrument is associated with a handler via handler_id.
     *
     * @param list<SelectedPaymentInstrument|SelectedPaymentInstrumentShape> $instruments
     */
    public function withInstruments(array $instruments): self
    {
        $self = clone $this;
        $self['instruments'] = $instruments;

        return $self;
    }
}
