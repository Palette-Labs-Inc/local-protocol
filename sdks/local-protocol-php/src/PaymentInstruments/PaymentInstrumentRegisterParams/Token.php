<?php

declare(strict_types=1);

namespace LocalProtocol\PaymentInstruments\PaymentInstrumentRegisterParams;

use LocalProtocol\Core\Attributes\Optional;
use LocalProtocol\Core\Attributes\Required;
use LocalProtocol\Core\Concerns\SdkModel;
use LocalProtocol\Core\Contracts\BaseModel;

/**
 * EVM token identifier used for auth/capture settlement.
 *
 * @phpstan-type TokenShape = array{
 *   decimals: int, symbol: string, address?: string|null
 * }
 */
final class Token implements BaseModel
{
    /** @use SdkModel<TokenShape> */
    use SdkModel;

    /**
     * Token decimals.
     */
    #[Required]
    public int $decimals;

    /**
     * Token symbol (e.g., USDC).
     */
    #[Required]
    public string $symbol;

    /**
     * ERC-20 contract address. Omit for native gas tokens.
     */
    #[Optional]
    public ?string $address;

    /**
     * `new Token()` is missing required properties by the API.
     *
     * To enforce required parameters use
     * ```
     * Token::with(decimals: ..., symbol: ...)
     * ```
     *
     * Otherwise ensure the following setters are called
     *
     * ```
     * (new Token)->withDecimals(...)->withSymbol(...)
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
        int $decimals,
        string $symbol,
        ?string $address = null
    ): self {
        $self = new self;

        $self['decimals'] = $decimals;
        $self['symbol'] = $symbol;

        null !== $address && $self['address'] = $address;

        return $self;
    }

    /**
     * Token decimals.
     */
    public function withDecimals(int $decimals): self
    {
        $self = clone $this;
        $self['decimals'] = $decimals;

        return $self;
    }

    /**
     * Token symbol (e.g., USDC).
     */
    public function withSymbol(string $symbol): self
    {
        $self = clone $this;
        $self['symbol'] = $symbol;

        return $self;
    }

    /**
     * ERC-20 contract address. Omit for native gas tokens.
     */
    public function withAddress(string $address): self
    {
        $self = clone $this;
        $self['address'] = $address;

        return $self;
    }
}
