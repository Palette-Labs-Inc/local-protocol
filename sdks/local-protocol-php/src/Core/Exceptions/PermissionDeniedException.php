<?php

namespace LocalProtocol\Core\Exceptions;

class PermissionDeniedException extends APIStatusException
{
    /** @var string */
    protected const DESC = 'LocalProtocol Permission Denied Exception';
}
