<?php

declare(strict_types=1);

namespace LocalProtocol\ServiceContracts;

use LocalProtocol\Core\Exceptions\APIException;
use LocalProtocol\Orders\Order;
use LocalProtocol\RequestOptions;

/**
 * @phpstan-import-type RequestOpts from \LocalProtocol\RequestOptions
 */
interface OrdersContract
{
    /**
     * @api
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
    ): Order;

    /**
     * @api
     *
     * @param string $orderID order identifier
     * @param RequestOpts|null $requestOptions
     *
     * @throws APIException
     */
    public function retrieve(
        string $orderID,
        RequestOptions|array|null $requestOptions = null
    ): Order;
}
