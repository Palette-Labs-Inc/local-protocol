<?php

namespace LocalProtocol\Core\Exceptions;

class AuthenticationException extends APIStatusException
{
    /** @var string */
    protected const DESC = 'LocalProtocol Authentication Exception';
}
