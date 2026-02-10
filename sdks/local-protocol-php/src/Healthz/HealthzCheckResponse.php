<?php

declare(strict_types=1);

namespace LocalProtocol\Healthz;

use LocalProtocol\Core\Attributes\Required;
use LocalProtocol\Core\Concerns\SdkModel;
use LocalProtocol\Core\Contracts\BaseModel;

/**
 * Health check response.
 *
 * @phpstan-type HealthzCheckResponseShape = array{status: 'ok'}
 */
final class HealthzCheckResponse implements BaseModel
{
    /** @use SdkModel<HealthzCheckResponseShape> */
    use SdkModel;

    /** @var 'ok' $status */
    #[Required]
    public string $status = 'ok';

    public function __construct()
    {
        $this->initialize();
    }

    /**
     * Construct an instance from the required parameters.
     *
     * You must use named parameters to construct any parameters with a default value.
     */
    public static function with(): self
    {
        return new self;
    }

    /**
     * @param 'ok' $status
     */
    public function withStatus(string $status): self
    {
        $self = clone $this;
        $self['status'] = $status;

        return $self;
    }
}
