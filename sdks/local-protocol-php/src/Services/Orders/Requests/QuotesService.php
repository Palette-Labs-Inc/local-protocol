<?php

declare(strict_types=1);

namespace LocalProtocol\Services\Orders\Requests;

use LocalProtocol\Client;
use LocalProtocol\Core\Exceptions\APIException;
use LocalProtocol\Core\Util;
use LocalProtocol\Orders\Requests\Quotes\OrderQuote;
use LocalProtocol\RequestOptions;
use LocalProtocol\ServiceContracts\Orders\Requests\QuotesContract;

/**
 * List and retrieve order request quotes.
 *
 * @phpstan-import-type RequestOpts from \LocalProtocol\RequestOptions
 */
final class QuotesService implements QuotesContract
{
    /**
     * @api
     */
    public QuotesRawService $raw;

    /**
     * @internal
     */
    public function __construct(private Client $client)
    {
        $this->raw = new QuotesRawService($client);
    }

    /**
     * @api
     *
     * Returns a single order quote by ID.
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
    ): OrderQuote {
        $params = Util::removeNulls(['orderRequestID' => $orderRequestID]);

        // @phpstan-ignore-next-line argument.type
        $response = $this->raw->retrieve($orderQuoteID, params: $params, requestOptions: $requestOptions);

        return $response->parse();
    }

    /**
     * @api
     *
     * Returns all quotes for an order request.
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
    ): array {
        // @phpstan-ignore-next-line argument.type
        $response = $this->raw->list($orderRequestID, requestOptions: $requestOptions);

        return $response->parse();
    }
}
