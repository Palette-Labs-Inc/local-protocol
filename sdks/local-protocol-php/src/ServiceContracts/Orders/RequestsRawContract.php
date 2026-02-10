<?php

declare(strict_types=1);

namespace LocalProtocol\ServiceContracts\Orders;

use LocalProtocol\Core\Contracts\BaseResponse;
use LocalProtocol\Core\Exceptions\APIException;
use LocalProtocol\Orders\Requests\RequestCreateParams;
use LocalProtocol\Orders\Requests\RequestNewResponse;
use LocalProtocol\RequestOptions;

/**
 * @phpstan-import-type RequestOpts from \LocalProtocol\RequestOptions
 */
interface RequestsRawContract
{
    /**
     * @api
     *
     * @param array<string,mixed>|RequestCreateParams $params
     * @param RequestOpts|null $requestOptions
     *
     * @return BaseResponse<RequestNewResponse>
     *
     * @throws APIException
     */
    public function create(
        array|RequestCreateParams $params,
        RequestOptions|array|null $requestOptions = null,
    ): BaseResponse;
}
