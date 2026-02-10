<?php

namespace LocalProtocol\Core\Exceptions;

class BadRequestException extends APIStatusException
{
    /** @var string */
    protected const DESC = 'LocalProtocol Bad Request Exception';
}
