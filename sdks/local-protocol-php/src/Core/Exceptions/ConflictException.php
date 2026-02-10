<?php

namespace LocalProtocol\Core\Exceptions;

class ConflictException extends APIStatusException
{
    /** @var string */
    protected const DESC = 'LocalProtocol Conflict Exception';
}
