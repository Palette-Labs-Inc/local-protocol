<?php

declare(strict_types=1);

namespace LocalProtocol\ServiceContracts;

use LocalProtocol\Core\Contracts\BaseResponse;
use LocalProtocol\Core\Exceptions\APIException;
use LocalProtocol\Healthz\HealthzCheckResponse;
use LocalProtocol\RequestOptions;

/**
 * @phpstan-import-type RequestOpts from \LocalProtocol\RequestOptions
 */
interface HealthzRawContract
{
    /**
     * @api
     *
     * @param RequestOpts|null $requestOptions
     *
     * @return BaseResponse<HealthzCheckResponse>
     *
     * @throws APIException
     */
    public function check(
        RequestOptions|array|null $requestOptions = null
    ): BaseResponse;
}
