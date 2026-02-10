<?php

declare(strict_types=1);

namespace LocalProtocol\PaymentInstruments\Amount\Currency;

use LocalProtocol\Core\Attributes\Required;
use LocalProtocol\Core\Concerns\SdkModel;
use LocalProtocol\Core\Contracts\BaseModel;

/**
 * Fiat currency descriptor.
 *
 * @phpstan-type FiatCurrencyShape = array{symbol: string}
 */
final class FiatCurrency implements BaseModel
{
    /** @use SdkModel<FiatCurrencyShape> */
    use SdkModel;

    /**
     * ISO 4217 currency code (e.g., 'USD', 'EUR', 'JPY').
     */
    #[Required]
    public string $symbol;

    /**
     * `new FiatCurrency()` is missing required properties by the API.
     *
     * To enforce required parameters use
     * ```
     * FiatCurrency::with(symbol: ...)
     * ```
     *
     * Otherwise ensure the following setters are called
     *
     * ```
     * (new FiatCurrency)->withSymbol(...)
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
     */
    public static function with(string $symbol): self
    {
        $self = new self;

        $self['symbol'] = $symbol;

        return $self;
    }

    /**
     * ISO 4217 currency code (e.g., 'USD', 'EUR', 'JPY').
     */
    public function withSymbol(string $symbol): self
    {
        $self = clone $this;
        $self['symbol'] = $symbol;

        return $self;
    }
}
