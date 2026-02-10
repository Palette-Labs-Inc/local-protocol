<?php

declare(strict_types=1);

namespace LocalProtocol\Services;

use LocalProtocol\Client;
use LocalProtocol\Core\Exceptions\APIException;
use LocalProtocol\Core\Util;
use LocalProtocol\Orders\Order;
use LocalProtocol\RequestOptions;
use LocalProtocol\ServiceContracts\OrdersContract;
use LocalProtocol\Services\Orders\RequestsService;

/**
 * Create and retrieve orders and order-level requests.
 *
 * @phpstan-import-type RequestOpts from \LocalProtocol\RequestOptions
 */
final class OrdersService implements OrdersContract
{
    /**
     * @api
     */
    public OrdersRawService $raw;

    /**
     * @api
     */
    public RequestsService $requests;

    /**
     * @internal
     */
    public function __construct(private Client $client)
    {
        $this->raw = new OrdersRawService($client);
        $this->requests = new RequestsService($client);
    }

    /**
     * @api
     *
     * Accept a quote and create an order. The `nonce` field provides idempotency.
     *
     * @param string $nonce client-generated idempotency key
     * @param string $orderQuoteID the accepted quote
     * @param string $orderRequestID the order request to fulfill
     * @param string $paymentInstrumentID reference to the registered payment instrument
     * @param RequestOpts|null $requestOptions
     *
     * @throws APIException
     */
    public function create(
        string $nonce,
        string $orderQuoteID,
        string $orderRequestID,
        string $paymentInstrumentID,
        RequestOptions|array|null $requestOptions = null,
    ): Order {
        $params = Util::removeNulls(
            [
                'nonce' => $nonce,
                'orderQuoteID' => $orderQuoteID,
                'orderRequestID' => $orderRequestID,
                'paymentInstrumentID' => $paymentInstrumentID,
            ],
        );

        // @phpstan-ignore-next-line argument.type
        $response = $this->raw->create(params: $params, requestOptions: $requestOptions);

        return $response->parse();
    }

    /**
     * @api
     *
     * Returns a single order by ID.
     *
     * @param string $orderID order identifier
     * @param RequestOpts|null $requestOptions
     *
     * @throws APIException
     */
    public function retrieve(
        string $orderID,
        RequestOptions|array|null $requestOptions = null
    ): Order {
        // @phpstan-ignore-next-line argument.type
        $response = $this->raw->retrieve($orderID, requestOptions: $requestOptions);

        return $response->parse();
    }
}
