<?php

declare(strict_types=1);

namespace LocalProtocol\Healthz;

use LocalProtocol\Core\Attributes\Required;
use LocalProtocol\Core\Concerns\SdkModel;
use LocalProtocol\Core\Contracts\BaseModel;
use LocalProtocol\Healthz\HealthzCheckResponse\Status;

/**
 * Health check response.
 *
 * @phpstan-type HealthzCheckResponseShape = array{status: Status|value-of<Status>}
 */
final class HealthzCheckResponse implements BaseModel
{
    /** @use SdkModel<HealthzCheckResponseShape> */
    use SdkModel;

    /** @var value-of<Status> $status */
    #[Required(enum: Status::class)]
    public string $status;

    /**
     * `new HealthzCheckResponse()` is missing required properties by the API.
     *
     * To enforce required parameters use
     * ```
     * HealthzCheckResponse::with(status: ...)
     * ```
     *
     * Otherwise ensure the following setters are called
     *
     * ```
     * (new HealthzCheckResponse)->withStatus(...)
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
     * @param Status|value-of<Status> $status
     */
    public static function with(Status|string $status): self
    {
        $self = new self;

        $self['status'] = $status;

        return $self;
    }

    /**
     * @param Status|value-of<Status> $status
     */
    public function withStatus(Status|string $status): self
    {
        $self = clone $this;
        $self['status'] = $status;

        return $self;
    }
}
