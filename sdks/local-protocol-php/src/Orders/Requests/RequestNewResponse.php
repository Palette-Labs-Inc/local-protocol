<?php

declare(strict_types=1);

namespace LocalProtocol\Orders\Requests;

use LocalProtocol\Core\Attributes\Required;
use LocalProtocol\Core\Concerns\SdkModel;
use LocalProtocol\Core\Contracts\BaseModel;

/**
 * An order request.
 *
 * @phpstan-type RequestNewResponseShape = array{
 *   id: string, intentID: string, nonce: string
 * }
 */
final class RequestNewResponse implements BaseModel
{
    /** @use SdkModel<RequestNewResponseShape> */
    use SdkModel;

    /**
     * Unique request identifier.
     */
    #[Required]
    public string $id;

    /**
     * Shared intent identifier for tracing Request -> Quote -> Order.
     */
    #[Required('intent_id')]
    public string $intentID;

    /**
     * Client-generated idempotency key.
     */
    #[Required]
    public string $nonce;

    /**
     * `new RequestNewResponse()` is missing required properties by the API.
     *
     * To enforce required parameters use
     * ```
     * RequestNewResponse::with(id: ..., intentID: ..., nonce: ...)
     * ```
     *
     * Otherwise ensure the following setters are called
     *
     * ```
     * (new RequestNewResponse)->withID(...)->withIntentID(...)->withNonce(...)
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
        string $id,
        string $intentID,
        string $nonce
    ): self {
        $self = new self;

        $self['id'] = $id;
        $self['intentID'] = $intentID;
        $self['nonce'] = $nonce;

        return $self;
    }

    /**
     * Unique request identifier.
     */
    public function withID(string $id): self
    {
        $self = clone $this;
        $self['id'] = $id;

        return $self;
    }

    /**
     * Shared intent identifier for tracing Request -> Quote -> Order.
     */
    public function withIntentID(string $intentID): self
    {
        $self = clone $this;
        $self['intentID'] = $intentID;

        return $self;
    }

    /**
     * Client-generated idempotency key.
     */
    public function withNonce(string $nonce): self
    {
        $self = clone $this;
        $self['nonce'] = $nonce;

        return $self;
    }
}
