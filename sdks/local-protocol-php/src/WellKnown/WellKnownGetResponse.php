<?php

declare(strict_types=1);

namespace LocalProtocol\WellKnown;

use LocalProtocol\Core\Attributes\Required;
use LocalProtocol\Core\Concerns\SdkModel;
use LocalProtocol\Core\Contracts\BaseModel;

/**
 * Canonical UCP discovery response envelope.
 *
 * @phpstan-type WellKnownGetResponseShape = array{
 *   ucp: array<string,mixed>,
 * }
 */
final class WellKnownGetResponse implements BaseModel
{
    /** @use SdkModel<WellKnownGetResponseShape> */
    use SdkModel;

    /**
     * Canonical UCP discovery profile.
     *
     * @var array<string,mixed> $ucp
     */
    #[Required]
    public array $ucp;

    /**
     * `new WellKnownGetResponse()` is missing required properties by the API.
     *
     * To enforce required parameters use
     * ```
     * WellKnownGetResponse::with(
     *   ucp: ...
     * )
     * ```
     *
     * Otherwise ensure the following setters are called
     *
     * ```
     * (new WellKnownGetResponse)
     *   ->withUcp(...)
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
     * @param array<string,mixed> $ucp
     */
    public static function with(array $ucp): self {
        $self = new self;

        $self['ucp'] = $ucp;

        return $self;
    }

    /**
     * Canonical UCP discovery profile.
     *
     * @param array<string,mixed> $ucp
     */
    public function withUcp(array $ucp): self
    {
        $self = clone $this;
        $self['ucp'] = $ucp;

        return $self;
    }
}
