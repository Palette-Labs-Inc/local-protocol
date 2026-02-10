<?php

declare(strict_types=1);

namespace LocalProtocol\PaymentInstruments;

use LocalProtocol\Core\Attributes\Required;
use LocalProtocol\Core\Concerns\SdkModel;
use LocalProtocol\Core\Contracts\BaseModel;

/**
 * Amount denominated in an EVM token. Value is in atomic token units.
 *
 * @phpstan-import-type EvmCurrencyShape from \LocalProtocol\PaymentInstruments\EvmCurrency
 *
 * @phpstan-type EvmAmountShape = array{
 *   currency: EvmCurrency|EvmCurrencyShape, value: string
 * }
 */
final class EvmAmount implements BaseModel
{
    /** @use SdkModel<EvmAmountShape> */
    use SdkModel;

    /**
     * EVM token currency descriptor.
     */
    #[Required]
    public EvmCurrency $currency;

    /**
     * Value in atomic token units as an integer string.
     */
    #[Required]
    public string $value;

    /**
     * `new EvmAmount()` is missing required properties by the API.
     *
     * To enforce required parameters use
     * ```
     * EvmAmount::with(currency: ..., value: ...)
     * ```
     *
     * Otherwise ensure the following setters are called
     *
     * ```
     * (new EvmAmount)->withCurrency(...)->withValue(...)
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
     * @param EvmCurrency|EvmCurrencyShape $currency
     */
    public static function with(
        EvmCurrency|array $currency,
        string $value
    ): self {
        $self = new self;

        $self['currency'] = $currency;
        $self['value'] = $value;

        return $self;
    }

    /**
     * EVM token currency descriptor.
     *
     * @param EvmCurrency|EvmCurrencyShape $currency
     */
    public function withCurrency(EvmCurrency|array $currency): self
    {
        $self = clone $this;
        $self['currency'] = $currency;

        return $self;
    }

    /**
     * Value in atomic token units as an integer string.
     */
    public function withValue(string $value): self
    {
        $self = clone $this;
        $self['value'] = $value;

        return $self;
    }
}
