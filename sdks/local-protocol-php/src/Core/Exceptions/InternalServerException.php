<?php

namespace LocalProtocol\Core\Exceptions;

class InternalServerException extends APIStatusException
{
    /** @var string */
    protected const DESC = 'LocalProtocol Internal Server Exception';
}
