<?php

declare(strict_types=1);

namespace LocalProtocol\PaymentInstruments;

use LocalProtocol\Core\Attributes\Required;
use LocalProtocol\Core\Concerns\SdkModel;
use LocalProtocol\Core\Contracts\BaseModel;

/**
 * EVM token currency descriptor.
 *
 * @phpstan-type EvmCurrencyShape = array{
 *   address: string, chainID: int, decimals: int
 * }
 */
final class EvmCurrency implements BaseModel
{
    /** @use SdkModel<EvmCurrencyShape> */
    use SdkModel;

    /**
     * Token contract address.
     */
    #[Required]
    public string $address;

    /**
     * EVM chain id.
     */
    #[Required('chain_id')]
    public int $chainID;

    /**
     * Decimal places for the token.
     */
    #[Required]
    public int $decimals;

    /**
     * `new EvmCurrency()` is missing required properties by the API.
     *
     * To enforce required parameters use
     * ```
     * EvmCurrency::with(address: ..., chainID: ..., decimals: ...)
     * ```
     *
     * Otherwise ensure the following setters are called
     *
     * ```
     * (new EvmCurrency)->withAddress(...)->withChainID(...)->withDecimals(...)
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
    public static function with(
        string $address,
        int $chainID,
        int $decimals
    ): self {
        $self = new self;

        $self['address'] = $address;
        $self['chainID'] = $chainID;
        $self['decimals'] = $decimals;

        return $self;
    }

    /**
     * Token contract address.
     */
    public function withAddress(string $address): self
    {
        $self = clone $this;
        $self['address'] = $address;

        return $self;
    }

    /**
     * EVM chain id.
     */
    public function withChainID(int $chainID): self
    {
        $self = clone $this;
        $self['chainID'] = $chainID;

        return $self;
    }

    /**
     * Decimal places for the token.
     */
    public function withDecimals(int $decimals): self
    {
        $self = clone $this;
        $self['decimals'] = $decimals;

        return $self;
    }
}
