<?php

declare(strict_types=1);

namespace LocalProtocol\Core\Conversion;

use LocalProtocol\Core\Conversion\Concerns\ArrayOf;
use LocalProtocol\Core\Conversion\Contracts\Converter;

/**
 * @internal
 */
final class MapOf implements Converter
{
    use ArrayOf;
}
