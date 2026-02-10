<?php

declare(strict_types=1);

namespace LocalProtocol\ServiceContracts;

use LocalProtocol\Core\Exceptions\APIException;
use LocalProtocol\RequestOptions;
use LocalProtocol\WellKnown\WellKnownGetResponse;

/**
 * @phpstan-import-type RequestOpts from \LocalProtocol\RequestOptions
 */
interface WellKnownContract
{
    /**
     * @api
     *
     * @param RequestOpts|null $requestOptions
     *
     * @throws APIException
     */
    public function retrieve(
        RequestOptions|array|null $requestOptions = null
    ): WellKnownGetResponse;
}
