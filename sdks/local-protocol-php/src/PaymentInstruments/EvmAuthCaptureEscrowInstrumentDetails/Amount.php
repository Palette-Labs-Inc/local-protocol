<?php

declare(strict_types=1);

namespace LocalProtocol\PaymentInstruments\EvmAuthCaptureEscrowInstrumentDetails;

use LocalProtocol\Core\Attributes\Required;
use LocalProtocol\Core\Concerns\SdkModel;
use LocalProtocol\Core\Contracts\BaseModel;
use LocalProtocol\PaymentInstruments\Amount\Currency\FiatCurrency;
use LocalProtocol\PaymentInstruments\EvmCurrency;

/**
 * Amount in atomic units. Currency chain_id MUST match the instrument chain_id; currency address and decimals MUST match token address and decimals.
 *
 * @phpstan-import-type CurrencyVariants from \LocalProtocol\PaymentInstruments\Amount\Currency
 * @phpstan-import-type CurrencyShape from \LocalProtocol\PaymentInstruments\Amount\Currency
 *
 * @phpstan-type AmountShape = array{currency: CurrencyShape, value: string}
 */
final class Amount implements BaseModel
{
    /** @use SdkModel<AmountShape> */
    use SdkModel;

    /**
     * Currency descriptor (fiat or EVM token).
     *
     * @var CurrencyVariants $currency
     */
    #[Required]
    public FiatCurrency|EvmCurrency $currency;

    /**
     * Value in minor currency units as an integer string.
     */
    #[Required]
    public string $value;

    /**
     * `new Amount()` is missing required properties by the API.
     *
     * To enforce required parameters use
     * ```
     * Amount::with(currency: ..., value: ...)
     * ```
     *
     * Otherwise ensure the following setters are called
     *
     * ```
     * (new Amount)->withCurrency(...)->withValue(...)
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
     * @param CurrencyShape $currency
     */
    public static function with(
        FiatCurrency|array|EvmCurrency $currency,
        string $value
    ): self {
        $self = new self;

        $self['currency'] = $currency;
        $self['value'] = $value;

        return $self;
    }

    /**
     * Currency descriptor (fiat or EVM token).
     *
     * @param CurrencyShape $currency
     */
    public function withCurrency(FiatCurrency|array|EvmCurrency $currency): self
    {
        $self = clone $this;
        $self['currency'] = $currency;

        return $self;
    }

    /**
     * Value in minor currency units as an integer string.
     */
    public function withValue(string $value): self
    {
        $self = clone $this;
        $self['value'] = $value;

        return $self;
    }
}
