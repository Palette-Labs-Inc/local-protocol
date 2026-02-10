<?php

declare(strict_types=1);

namespace LocalProtocol\Services\Orders\Requests;

use LocalProtocol\Client;
use LocalProtocol\Core\Contracts\BaseResponse;
use LocalProtocol\Core\Conversion\ListOf;
use LocalProtocol\Core\Exceptions\APIException;
use LocalProtocol\Orders\Requests\Quotes\OrderQuote;
use LocalProtocol\Orders\Requests\Quotes\QuoteRetrieveParams;
use LocalProtocol\RequestOptions;
use LocalProtocol\ServiceContracts\Orders\Requests\QuotesRawContract;

/**
 * List and retrieve order request quotes.
 *
 * @phpstan-import-type RequestOpts from \LocalProtocol\RequestOptions
 */
final class QuotesRawService implements QuotesRawContract
{
    // @phpstan-ignore-next-line
    /**
     * @internal
     */
    public function __construct(private Client $client) {}

    /**
     * @api
     *
     * Returns a single order quote by ID.
     *
     * @param string $orderQuoteID order quote identifier
     * @param array{orderRequestID: string}|QuoteRetrieveParams $params
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
    ): BaseResponse {
        [$parsed, $options] = QuoteRetrieveParams::parseRequest(
            $params,
            $requestOptions,
        );
        $orderRequestID = $parsed['orderRequestID'];
        unset($parsed['orderRequestID']);

        // @phpstan-ignore-next-line return.type
        return $this->client->request(
            method: 'get',
            path: [
                'orders/requests/%1$s/quotes/%2$s', $orderRequestID, $orderQuoteID,
            ],
            options: $options,
            convert: OrderQuote::class,
        );
    }

    /**
     * @api
     *
     * Returns all quotes for an order request.
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
    ): BaseResponse {
        // @phpstan-ignore-next-line return.type
        return $this->client->request(
            method: 'get',
            path: ['orders/requests/%1$s/quotes', $orderRequestID],
            options: $requestOptions,
            convert: new ListOf(OrderQuote::class),
        );
    }
}
