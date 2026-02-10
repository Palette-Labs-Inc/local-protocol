<?php

declare(strict_types=1);

namespace LocalProtocol\WellKnown;

use LocalProtocol\Core\Attributes\Required;
use LocalProtocol\Core\Concerns\SdkModel;
use LocalProtocol\Core\Contracts\BaseModel;

/**
 * Service discovery metadata.
 *
 * @phpstan-type WellKnownGetResponseShape = array{
 *   capabilities: array<string,mixed>,
 *   endpoints: array<string,string>,
 *   name: string,
 *   version: string,
 * }
 */
final class WellKnownGetResponse implements BaseModel
{
    /** @use SdkModel<WellKnownGetResponseShape> */
    use SdkModel;

    /**
     * Supported capabilities by domain.
     *
     * @var array<string,mixed> $capabilities
     */
    #[Required(map: 'mixed')]
    public array $capabilities;

    /**
     * Endpoint path map.
     *
     * @var array<string,string> $endpoints
     */
    #[Required(map: 'string')]
    public array $endpoints;

    /**
     * Server name.
     */
    #[Required]
    public string $name;

    /**
     * Protocol version.
     */
    #[Required]
    public string $version;

    /**
     * `new WellKnownGetResponse()` is missing required properties by the API.
     *
     * To enforce required parameters use
     * ```
     * WellKnownGetResponse::with(
     *   capabilities: ..., endpoints: ..., name: ..., version: ...
     * )
     * ```
     *
     * Otherwise ensure the following setters are called
     *
     * ```
     * (new WellKnownGetResponse)
     *   ->withCapabilities(...)
     *   ->withEndpoints(...)
     *   ->withName(...)
     *   ->withVersion(...)
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
     * @param array<string,mixed> $capabilities
     * @param array<string,string> $endpoints
     */
    public static function with(
        array $capabilities,
        array $endpoints,
        string $name,
        string $version
    ): self {
        $self = new self;

        $self['capabilities'] = $capabilities;
        $self['endpoints'] = $endpoints;
        $self['name'] = $name;
        $self['version'] = $version;

        return $self;
    }

    /**
     * Supported capabilities by domain.
     *
     * @param array<string,mixed> $capabilities
     */
    public function withCapabilities(array $capabilities): self
    {
        $self = clone $this;
        $self['capabilities'] = $capabilities;

        return $self;
    }

    /**
     * Endpoint path map.
     *
     * @param array<string,string> $endpoints
     */
    public function withEndpoints(array $endpoints): self
    {
        $self = clone $this;
        $self['endpoints'] = $endpoints;

        return $self;
    }

    /**
     * Server name.
     */
    public function withName(string $name): self
    {
        $self = clone $this;
        $self['name'] = $name;

        return $self;
    }

    /**
     * Protocol version.
     */
    public function withVersion(string $version): self
    {
        $self = clone $this;
        $self['version'] = $version;

        return $self;
    }
}
