<?php

declare(strict_types=1);

namespace LocalProtocol\Services;

use LocalProtocol\Client;
use LocalProtocol\Core\Contracts\BaseResponse;
use LocalProtocol\Core\Exceptions\APIException;
use LocalProtocol\Orders\Order;
use LocalProtocol\Orders\OrderCreateParams;
use LocalProtocol\RequestOptions;
use LocalProtocol\ServiceContracts\OrdersRawContract;

/**
 * @phpstan-import-type RequestOpts from \LocalProtocol\RequestOptions
 */
final class OrdersRawService implements OrdersRawContract
{
    // @phpstan-ignore-next-line
    /**
     * @internal
     */
    public function __construct(private Client $client) {}

    /**
     * @api
     *
     * Accept a quote and create an order. The `nonce` field provides idempotency.
     *
     * @param array{
     *   nonce: string,
     *   orderQuoteID: string,
     *   orderRequestID: string,
     *   paymentInstrumentID: string,
     * }|OrderCreateParams $params
     * @param RequestOpts|null $requestOptions
     *
     * @return BaseResponse<Order>
     *
     * @throws APIException
     */
    public function create(
        array|OrderCreateParams $params,
        RequestOptions|array|null $requestOptions = null,
    ): BaseResponse {
        [$parsed, $options] = OrderCreateParams::parseRequest(
            $params,
            $requestOptions,
        );

        // @phpstan-ignore-next-line return.type
        return $this->client->request(
            method: 'post',
            path: 'orders',
            body: (object) $parsed,
            options: $options,
            convert: Order::class,
        );
    }

    /**
     * @api
     *
     * Returns a single order by ID.
     *
     * @param string $orderID order identifier
     * @param RequestOpts|null $requestOptions
     *
     * @return BaseResponse<Order>
     *
     * @throws APIException
     */
    public function retrieve(
        string $orderID,
        RequestOptions|array|null $requestOptions = null
    ): BaseResponse {
        // @phpstan-ignore-next-line return.type
        return $this->client->request(
            method: 'get',
            path: ['orders/%1$s', $orderID],
            options: $requestOptions,
            convert: Order::class,
        );
    }
}
