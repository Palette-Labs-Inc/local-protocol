<?php

declare(strict_types=1);

namespace LocalProtocol\PaymentInstruments;

use LocalProtocol\Core\Attributes\Optional;
use LocalProtocol\Core\Attributes\Required;
use LocalProtocol\Core\Concerns\SdkModel;
use LocalProtocol\Core\Contracts\BaseModel;
use LocalProtocol\PaymentInstruments\PaymentInstrument\Credential;
use LocalProtocol\Requests\PostalAddress;

/**
 * Base definition for any payment instrument.
 *
 * @phpstan-import-type PostalAddressShape from \LocalProtocol\Requests\PostalAddress
 * @phpstan-import-type CredentialShape from \LocalProtocol\PaymentInstruments\PaymentInstrument\Credential
 *
 * @phpstan-type PaymentInstrumentShape = array{
 *   id: string,
 *   handlerID: string,
 *   type: string,
 *   billingAddress?: null|PostalAddress|PostalAddressShape,
 *   credential?: null|Credential|CredentialShape,
 *   display?: array<string,mixed>|null,
 * }
 */
final class PaymentInstrument implements BaseModel
{
    /** @use SdkModel<PaymentInstrumentShape> */
    use SdkModel;

    /**
     * Unique instrument identifier.
     */
    #[Required]
    public string $id;

    /**
     * Handler instance identifier.
     */
    #[Required('handler_id')]
    public string $handlerID;

    /**
     * Instrument category (e.g., 'card', 'tokenized_card').
     */
    #[Required]
    public string $type;

    /**
     * Billing address.
     */
    #[Optional('billing_address')]
    public ?PostalAddress $billingAddress;

    /**
     * Base definition for any payment credential.
     */
    #[Optional]
    public ?Credential $credential;

    /**
     * Display information for the instrument. Each payment instrument schema defines its specific display properties, as outlined by the payment handler.
     *
     * @var array<string,mixed>|null $display
     */
    #[Optional(map: 'mixed')]
    public ?array $display;

    /**
     * `new PaymentInstrument()` is missing required properties by the API.
     *
     * To enforce required parameters use
     * ```
     * PaymentInstrument::with(id: ..., handlerID: ..., type: ...)
     * ```
     *
     * Otherwise ensure the following setters are called
     *
     * ```
     * (new PaymentInstrument)->withID(...)->withHandlerID(...)->withType(...)
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
     * @param PostalAddress|PostalAddressShape|null $billingAddress
     * @param Credential|CredentialShape|null $credential
     * @param array<string,mixed>|null $display
     */
    public static function with(
        string $id,
        string $handlerID,
        string $type,
        PostalAddress|array|null $billingAddress = null,
        Credential|array|null $credential = null,
        ?array $display = null,
    ): self {
        $self = new self;

        $self['id'] = $id;
        $self['handlerID'] = $handlerID;
        $self['type'] = $type;

        null !== $billingAddress && $self['billingAddress'] = $billingAddress;
        null !== $credential && $self['credential'] = $credential;
        null !== $display && $self['display'] = $display;

        return $self;
    }

    /**
     * Unique instrument identifier.
     */
    public function withID(string $id): self
    {
        $self = clone $this;
        $self['id'] = $id;

        return $self;
    }

    /**
     * Handler instance identifier.
     */
    public function withHandlerID(string $handlerID): self
    {
        $self = clone $this;
        $self['handlerID'] = $handlerID;

        return $self;
    }

    /**
     * Instrument category (e.g., 'card', 'tokenized_card').
     */
    public function withType(string $type): self
    {
        $self = clone $this;
        $self['type'] = $type;

        return $self;
    }

    /**
     * Billing address.
     *
     * @param PostalAddress|PostalAddressShape $billingAddress
     */
    public function withBillingAddress(
        PostalAddress|array $billingAddress
    ): self {
        $self = clone $this;
        $self['billingAddress'] = $billingAddress;

        return $self;
    }

    /**
     * Base definition for any payment credential.
     *
     * @param Credential|CredentialShape $credential
     */
    public function withCredential(Credential|array $credential): self
    {
        $self = clone $this;
        $self['credential'] = $credential;

        return $self;
    }

    /**
     * Display information for the instrument. Each payment instrument schema defines its specific display properties, as outlined by the payment handler.
     *
     * @param array<string,mixed> $display
     */
    public function withDisplay(array $display): self
    {
        $self = clone $this;
        $self['display'] = $display;

        return $self;
    }
}
