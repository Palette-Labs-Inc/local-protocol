<?php

declare(strict_types=1);

namespace LocalProtocol\ServiceContracts\Orders;

use LocalProtocol\Core\Exceptions\APIException;
use LocalProtocol\Orders\Requests\RequestCreateParams\Item;
use LocalProtocol\Orders\Requests\RequestNewResponse;
use LocalProtocol\RequestOptions;

/**
 * @phpstan-import-type ItemShape from \LocalProtocol\Orders\Requests\RequestCreateParams\Item
 * @phpstan-import-type RequestOpts from \LocalProtocol\RequestOptions
 */
interface RequestsContract
{
    /**
     * @api
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
    ): RequestNewResponse;
}
