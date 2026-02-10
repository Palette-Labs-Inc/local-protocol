<?php

namespace LocalProtocol\Core\Exceptions;

class UnprocessableEntityException extends APIStatusException
{
    /** @var string */
    protected const DESC = 'LocalProtocol Unprocessable Entity Exception';
}
