<?php

namespace LocalProtocol\Core\Exceptions;

class RateLimitException extends APIStatusException
{
    /** @var string */
    protected const DESC = 'LocalProtocol Rate Limit Exception';
}
