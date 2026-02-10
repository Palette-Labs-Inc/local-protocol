<?php

declare(strict_types=1);

namespace LocalProtocol\Core\Conversion\Contracts;

use LocalProtocol\Core\Conversion\CoerceState;
use LocalProtocol\Core\Conversion\DumpState;

/**
 * @internal
 */
interface Converter
{
    /**
     * @internal
     */
    public function coerce(mixed $value, CoerceState $state): mixed;

    /**
     * @internal
     */
    public function dump(mixed $value, DumpState $state): mixed;
}
