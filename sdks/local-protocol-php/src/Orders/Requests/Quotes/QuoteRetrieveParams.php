<?php

declare(strict_types=1);

namespace LocalProtocol\Orders\Requests\Quotes;

use LocalProtocol\Core\Attributes\Required;
use LocalProtocol\Core\Concerns\SdkModel;
use LocalProtocol\Core\Concerns\SdkParams;
use LocalProtocol\Core\Contracts\BaseModel;

/**
 * Returns a single order quote by ID.
 *
 * @see LocalProtocol\Services\Orders\Requests\QuotesService::retrieve()
 *
 * @phpstan-type QuoteRetrieveParamsShape = array{orderRequestID: string}
 */
final class QuoteRetrieveParams implements BaseModel
{
    /** @use SdkModel<QuoteRetrieveParamsShape> */
    use SdkModel;
    use SdkParams;

    #[Required]
    public string $orderRequestID;

    /**
     * `new QuoteRetrieveParams()` is missing required properties by the API.
     *
     * To enforce required parameters use
     * ```
     * QuoteRetrieveParams::with(orderRequestID: ...)
     * ```
     *
     * Otherwise ensure the following setters are called
     *
     * ```
     * (new QuoteRetrieveParams)->withOrderRequestID(...)
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
    public static function with(string $orderRequestID): self
    {
        $self = new self;

        $self['orderRequestID'] = $orderRequestID;

        return $self;
    }

    public function withOrderRequestID(string $orderRequestID): self
    {
        $self = clone $this;
        $self['orderRequestID'] = $orderRequestID;

        return $self;
    }
}
