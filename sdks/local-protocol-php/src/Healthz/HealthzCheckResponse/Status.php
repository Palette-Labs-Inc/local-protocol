<?php

declare(strict_types=1);

namespace LocalProtocol\Healthz\HealthzCheckResponse;

enum Status: string
{
    case OK = 'ok';
}
