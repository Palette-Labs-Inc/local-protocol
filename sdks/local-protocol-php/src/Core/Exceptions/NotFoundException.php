<?php

namespace LocalProtocol\Core\Exceptions;

class NotFoundException extends APIStatusException
{
    /** @var string */
    protected const DESC = 'LocalProtocol Not Found Exception';
}
