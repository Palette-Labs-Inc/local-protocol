<?php

declare(strict_types=1);

namespace LocalProtocol\ServiceContracts;

use LocalProtocol\Core\Contracts\BaseResponse;
use LocalProtocol\Core\Exceptions\APIException;
use LocalProtocol\RequestOptions;
use LocalProtocol\Requests\DeliveryRequest;
use LocalProtocol\Requests\RequestCreateParams;

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
     * @return BaseResponse<DeliveryRequest>
     *
     * @throws APIException
     */
    public function create(
        array|RequestCreateParams $params,
        RequestOptions|array|null $requestOptions = null,
    ): BaseResponse;

    /**
     * @api
     *
     * @param string $requestID delivery request identifier
     * @param RequestOpts|null $requestOptions
     *
     * @return BaseResponse<DeliveryRequest>
     *
     * @throws APIException
     */
    public function retrieve(
        string $requestID,
        RequestOptions|array|null $requestOptions = null
    ): BaseResponse;

    /**
     * @api
     *
     * @param RequestOpts|null $requestOptions
     *
     * @return BaseResponse<list<DeliveryRequest>>
     *
     * @throws APIException
     */
    public function list(
        RequestOptions|array|null $requestOptions = null
    ): BaseResponse;
}
