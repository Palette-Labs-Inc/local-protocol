<?php

declare(strict_types=1);

namespace LocalProtocol\Requests\Quotes\QuoteCreateParams;

use LocalProtocol\Core\Attributes\Optional;
use LocalProtocol\Core\Concerns\SdkModel;
use LocalProtocol\Core\Contracts\BaseModel;
use LocalProtocol\Requests\Quotes\QuoteCreateParams\Payment\Instrument;

/**
 * Payment handlers available for accepting this quote.
 *
 * @phpstan-import-type InstrumentShape from \LocalProtocol\Requests\Quotes\QuoteCreateParams\Payment\Instrument
 *
 * @phpstan-type PaymentShape = array{
 *   instruments?: list<Instrument|InstrumentShape>|null
 * }
 */
final class Payment implements BaseModel
{
    /** @use SdkModel<PaymentShape> */
    use SdkModel;

    /**
     * Payment instruments available. Each instrument is associated with a handler via handler_id.
     *
     * @var list<Instrument>|null $instruments
     */
    #[Optional(list: Instrument::class)]
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
     * @param list<Instrument|InstrumentShape>|null $instruments
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
     * @param list<Instrument|InstrumentShape> $instruments
     */
    public function withInstruments(array $instruments): self
    {
        $self = clone $this;
        $self['instruments'] = $instruments;

        return $self;
    }
}
