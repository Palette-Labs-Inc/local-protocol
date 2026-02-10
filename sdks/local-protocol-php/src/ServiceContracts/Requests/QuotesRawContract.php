<?php

declare(strict_types=1);

namespace LocalProtocol\ServiceContracts\Requests;

use LocalProtocol\Core\Contracts\BaseResponse;
use LocalProtocol\Core\Exceptions\APIException;
use LocalProtocol\RequestOptions;
use LocalProtocol\Requests\Quotes\DeliveryQuote;
use LocalProtocol\Requests\Quotes\QuoteCreateParams;
use LocalProtocol\Requests\Quotes\QuoteRetrieveParams;

/**
 * @phpstan-import-type RequestOpts from \LocalProtocol\RequestOptions
 */
interface QuotesRawContract
{
    /**
     * @api
     *
     * @param string $requestID delivery request identifier
     * @param array<string,mixed>|QuoteCreateParams $params
     * @param RequestOpts|null $requestOptions
     *
     * @return BaseResponse<DeliveryQuote>
     *
     * @throws APIException
     */
    public function create(
        string $requestID,
        array|QuoteCreateParams $params,
        RequestOptions|array|null $requestOptions = null,
    ): BaseResponse;

    /**
     * @api
     *
     * @param string $quoteID quote identifier
     * @param array<string,mixed>|QuoteRetrieveParams $params
     * @param RequestOpts|null $requestOptions
     *
     * @return BaseResponse<DeliveryQuote>
     *
     * @throws APIException
     */
    public function retrieve(
        string $quoteID,
        array|QuoteRetrieveParams $params,
        RequestOptions|array|null $requestOptions = null,
    ): BaseResponse;

    /**
     * @api
     *
     * @param string $requestID delivery request identifier
     * @param RequestOpts|null $requestOptions
     *
     * @return BaseResponse<list<DeliveryQuote>>
     *
     * @throws APIException
     */
    public function list(
        string $requestID,
        RequestOptions|array|null $requestOptions = null
    ): BaseResponse;
}
