<?php

declare(strict_types=1);

namespace LocalProtocol\Services\Orders;

use LocalProtocol\Client;
use LocalProtocol\Core\Exceptions\APIException;
use LocalProtocol\Core\Util;
use LocalProtocol\Orders\Requests\RequestCreateParams\Item;
use LocalProtocol\Orders\Requests\RequestNewResponse;
use LocalProtocol\RequestOptions;
use LocalProtocol\ServiceContracts\Orders\RequestsContract;
use LocalProtocol\Services\Orders\Requests\QuotesService;

/**
 * Create order requests that can be quoted.
 *
 * @phpstan-import-type ItemShape from \LocalProtocol\Orders\Requests\RequestCreateParams\Item
 * @phpstan-import-type RequestOpts from \LocalProtocol\RequestOptions
 */
final class RequestsService implements RequestsContract
{
    /**
     * @api
     */
    public RequestsRawService $raw;

    /**
     * @api
     */
    public QuotesService $quotes;

    /**
     * @internal
     */
    public function __construct(private Client $client)
    {
        $this->raw = new RequestsRawService($client);
        $this->quotes = new QuotesService($client);
    }

    /**
     * @api
     *
     * Submit a new order request with a cart. The `nonce` field provides idempotency.
     *
     * @param string $id unique cart identifier
     * @param string $intentID shared intent identifier for tracing Request -> Quote -> Order
     * @param list<Item|ItemShape> $items items in the cart
     * @param string $nonce client-generated idempotency key
     * @param RequestOpts|null $requestOptions
     *
     * @throws APIException
     */
    public function create(
        string $id,
        string $intentID,
        array $items,
        string $nonce,
        RequestOptions|array|null $requestOptions = null,
    ): RequestNewResponse {
        $params = Util::removeNulls(
            [
                'id' => $id,
                'intentID' => $intentID,
                'items' => $items,
                'nonce' => $nonce,
            ],
        );

        // @phpstan-ignore-next-line argument.type
        $response = $this->raw->create(params: $params, requestOptions: $requestOptions);

        return $response->parse();
    }
}
