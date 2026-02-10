<?php

declare(strict_types=1);

namespace LocalProtocol\PaymentInstruments\Amount;

use LocalProtocol\Core\Concerns\SdkUnion;
use LocalProtocol\Core\Conversion\Contracts\Converter;
use LocalProtocol\Core\Conversion\Contracts\ConverterSource;
use LocalProtocol\PaymentInstruments\Amount\Currency\FiatCurrency;
use LocalProtocol\PaymentInstruments\EvmCurrency;

/**
 * Currency descriptor (fiat or EVM token).
 *
 * @phpstan-import-type FiatCurrencyShape from \LocalProtocol\PaymentInstruments\Amount\Currency\FiatCurrency
 * @phpstan-import-type EvmCurrencyShape from \LocalProtocol\PaymentInstruments\EvmCurrency
 *
 * @phpstan-type CurrencyVariants = FiatCurrency|EvmCurrency
 * @phpstan-type CurrencyShape = CurrencyVariants|FiatCurrencyShape|EvmCurrencyShape
 */
final class Currency implements ConverterSource
{
    use SdkUnion;

    /**
     * @return list<string|Converter|ConverterSource>|array<string,string|Converter|ConverterSource>
     */
    public static function variants(): array
    {
        return [FiatCurrency::class, EvmCurrency::class];
    }
}
