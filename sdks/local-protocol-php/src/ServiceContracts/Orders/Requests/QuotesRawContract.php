<?php

declare(strict_types=1);

namespace LocalProtocol\ServiceContracts\Orders\Requests;

use LocalProtocol\Core\Contracts\BaseResponse;
use LocalProtocol\Core\Exceptions\APIException;
use LocalProtocol\Orders\Requests\Quotes\OrderQuote;
use LocalProtocol\Orders\Requests\Quotes\QuoteRetrieveParams;
use LocalProtocol\RequestOptions;

/**
 * @phpstan-import-type RequestOpts from \LocalProtocol\RequestOptions
 */
interface QuotesRawContract
{
    /**
     * @api
     *
     * @param string $orderQuoteID order quote identifier
     * @param array<string,mixed>|QuoteRetrieveParams $params
     * @param RequestOpts|null $requestOptions
     *
     * @return BaseResponse<OrderQuote>
     *
     * @throws APIException
     */
    public function retrieve(
        string $orderQuoteID,
        array|QuoteRetrieveParams $params,
        RequestOptions|array|null $requestOptions = null,
    ): BaseResponse;

    /**
     * @api
     *
     * @param string $orderRequestID order request identifier
     * @param RequestOpts|null $requestOptions
     *
     * @return BaseResponse<list<OrderQuote>>
     *
     * @throws APIException
     */
    public function list(
        string $orderRequestID,
        RequestOptions|array|null $requestOptions = null
    ): BaseResponse;
}
