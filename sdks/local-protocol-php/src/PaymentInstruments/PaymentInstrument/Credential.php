<?php

declare(strict_types=1);

namespace LocalProtocol\PaymentInstruments\PaymentInstrument;

use LocalProtocol\Core\Attributes\Required;
use LocalProtocol\Core\Concerns\SdkModel;
use LocalProtocol\Core\Contracts\BaseModel;

/**
 * Base definition for any payment credential.
 *
 * @phpstan-type CredentialShape = array{type: string}
 */
final class Credential implements BaseModel
{
    /** @use SdkModel<CredentialShape> */
    use SdkModel;

    /**
     * Credential type discriminator.
     */
    #[Required]
    public string $type;

    /**
     * `new Credential()` is missing required properties by the API.
     *
     * To enforce required parameters use
     * ```
     * Credential::with(type: ...)
     * ```
     *
     * Otherwise ensure the following setters are called
     *
     * ```
     * (new Credential)->withType(...)
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
    public static function with(string $type): self
    {
        $self = new self;

        $self['type'] = $type;

        return $self;
    }

    /**
     * Credential type discriminator.
     */
    public function withType(string $type): self
    {
        $self = clone $this;
        $self['type'] = $type;

        return $self;
    }
}
