<?php

declare(strict_types=1);

namespace LocalProtocol\Orders\Requests;

use LocalProtocol\Core\Attributes\Required;
use LocalProtocol\Core\Concerns\SdkModel;
use LocalProtocol\Core\Concerns\SdkParams;
use LocalProtocol\Core\Contracts\BaseModel;
use LocalProtocol\Orders\Requests\RequestCreateParams\Item;

/**
 * Submit a new order request with a cart. The `nonce` field provides idempotency.
 *
 * @see LocalProtocol\Services\Orders\RequestsService::create()
 *
 * @phpstan-import-type ItemShape from \LocalProtocol\Orders\Requests\RequestCreateParams\Item
 *
 * @phpstan-type RequestCreateParamsShape = array{
 *   id: string, intentID: string, items: list<Item|ItemShape>, nonce: string
 * }
 */
final class RequestCreateParams implements BaseModel
{
    /** @use SdkModel<RequestCreateParamsShape> */
    use SdkModel;
    use SdkParams;

    /**
     * Unique cart identifier.
     */
    #[Required]
    public string $id;

    /**
     * Shared intent identifier for tracing Request -> Quote -> Order.
     */
    #[Required('intent_id')]
    public string $intentID;

    /**
     * Items in the cart.
     *
     * @var list<Item> $items
     */
    #[Required(list: Item::class)]
    public array $items;

    /**
     * Client-generated idempotency key.
     */
    #[Required]
    public string $nonce;

    /**
     * `new RequestCreateParams()` is missing required properties by the API.
     *
     * To enforce required parameters use
     * ```
     * RequestCreateParams::with(id: ..., intentID: ..., items: ..., nonce: ...)
     * ```
     *
     * Otherwise ensure the following setters are called
     *
     * ```
     * (new RequestCreateParams)
     *   ->withID(...)
     *   ->withIntentID(...)
     *   ->withItems(...)
     *   ->withNonce(...)
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
     * @param list<Item|ItemShape> $items
     */
    public static function with(
        string $id,
        string $intentID,
        array $items,
        string $nonce
    ): self {
        $self = new self;

        $self['id'] = $id;
        $self['intentID'] = $intentID;
        $self['items'] = $items;
        $self['nonce'] = $nonce;

        return $self;
    }

    /**
     * Unique cart identifier.
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
     * Items in the cart.
     *
     * @param list<Item|ItemShape> $items
     */
    public function withItems(array $items): self
    {
        $self = clone $this;
        $self['items'] = $items;

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
