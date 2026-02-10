<?php

declare(strict_types=1);

namespace LocalProtocol\ServiceContracts\Orders\Requests;

use LocalProtocol\Core\Exceptions\APIException;
use LocalProtocol\Orders\Requests\Quotes\OrderQuote;
use LocalProtocol\RequestOptions;

/**
 * @phpstan-import-type RequestOpts from \LocalProtocol\RequestOptions
 */
interface QuotesContract
{
    /**
     * @api
     *
     * @param string $orderQuoteID order quote identifier
     * @param string $orderRequestID order request identifier
     * @param RequestOpts|null $requestOptions
     *
     * @throws APIException
     */
    public function retrieve(
        string $orderQuoteID,
        string $orderRequestID,
        RequestOptions|array|null $requestOptions = null,
    ): OrderQuote;

    /**
     * @api
     *
     * @param string $orderRequestID order request identifier
     * @param RequestOpts|null $requestOptions
     *
     * @return list<OrderQuote>
     *
     * @throws APIException
     */
    public function list(
        string $orderRequestID,
        RequestOptions|array|null $requestOptions = null
    ): array;
}
