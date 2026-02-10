<?php

declare(strict_types=1);

namespace LocalProtocol\ServiceContracts;

use LocalProtocol\Core\Contracts\BaseResponse;
use LocalProtocol\Core\Exceptions\APIException;
use LocalProtocol\Deliveries\Delivery;
use LocalProtocol\Deliveries\DeliveryCreateParams;
use LocalProtocol\Deliveries\DeliveryUpdateEventParams;
use LocalProtocol\RequestOptions;

/**
 * @phpstan-import-type RequestOpts from \LocalProtocol\RequestOptions
 */
interface DeliveriesRawContract
{
    /**
     * @api
     *
     * @param array<string,mixed>|DeliveryCreateParams $params
     * @param RequestOpts|null $requestOptions
     *
     * @return BaseResponse<Delivery>
     *
     * @throws APIException
     */
    public function create(
        array|DeliveryCreateParams $params,
        RequestOptions|array|null $requestOptions = null,
    ): BaseResponse;

    /**
     * @api
     *
     * @param string $deliveryID delivery identifier
     * @param RequestOpts|null $requestOptions
     *
     * @return BaseResponse<Delivery>
     *
     * @throws APIException
     */
    public function retrieve(
        string $deliveryID,
        RequestOptions|array|null $requestOptions = null
    ): BaseResponse;

    /**
     * @api
     *
     * @param RequestOpts|null $requestOptions
     *
     * @return BaseResponse<list<Delivery>>
     *
     * @throws APIException
     */
    public function list(
        RequestOptions|array|null $requestOptions = null
    ): BaseResponse;

    /**
     * @api
     *
     * @param string $deliveryID delivery identifier
     * @param array<string,mixed>|DeliveryUpdateEventParams $params
     * @param RequestOpts|null $requestOptions
     *
     * @return BaseResponse<Delivery>
     *
     * @throws APIException
     */
    public function updateEvent(
        string $deliveryID,
        array|DeliveryUpdateEventParams $params,
        RequestOptions|array|null $requestOptions = null,
    ): BaseResponse;
}
