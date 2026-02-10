<?php

declare(strict_types=1);

namespace LocalProtocol\Requests\Quotes;

use LocalProtocol\Core\Attributes\Required;
use LocalProtocol\Core\Concerns\SdkModel;
use LocalProtocol\Core\Concerns\SdkParams;
use LocalProtocol\Core\Contracts\BaseModel;

/**
 * Returns a single quote by ID.
 *
 * @see LocalProtocol\Services\Requests\QuotesService::retrieve()
 *
 * @phpstan-type QuoteRetrieveParamsShape = array{requestID: string}
 */
final class QuoteRetrieveParams implements BaseModel
{
    /** @use SdkModel<QuoteRetrieveParamsShape> */
    use SdkModel;
    use SdkParams;

    #[Required]
    public string $requestID;

    /**
     * `new QuoteRetrieveParams()` is missing required properties by the API.
     *
     * To enforce required parameters use
     * ```
     * QuoteRetrieveParams::with(requestID: ...)
     * ```
     *
     * Otherwise ensure the following setters are called
     *
     * ```
     * (new QuoteRetrieveParams)->withRequestID(...)
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
    public static function with(string $requestID): self
    {
        $self = new self;

        $self['requestID'] = $requestID;

        return $self;
    }

    public function withRequestID(string $requestID): self
    {
        $self = clone $this;
        $self['requestID'] = $requestID;

        return $self;
    }
}
