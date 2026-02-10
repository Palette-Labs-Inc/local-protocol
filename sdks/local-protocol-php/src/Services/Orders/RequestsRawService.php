<?php

declare(strict_types=1);

namespace LocalProtocol\Services\Orders;

use LocalProtocol\Client;
use LocalProtocol\Core\Contracts\BaseResponse;
use LocalProtocol\Core\Exceptions\APIException;
use LocalProtocol\Orders\Requests\RequestCreateParams;
use LocalProtocol\Orders\Requests\RequestCreateParams\Item;
use LocalProtocol\Orders\Requests\RequestNewResponse;
use LocalProtocol\RequestOptions;
use LocalProtocol\ServiceContracts\Orders\RequestsRawContract;

/**
 * Create order requests that can be quoted.
 *
 * @phpstan-import-type ItemShape from \LocalProtocol\Orders\Requests\RequestCreateParams\Item
 * @phpstan-import-type RequestOpts from \LocalProtocol\RequestOptions
 */
final class RequestsRawService implements RequestsRawContract
{
    // @phpstan-ignore-next-line
    /**
     * @internal
     */
    public function __construct(private Client $client) {}

    /**
     * @api
     *
     * Submit a new order request with a cart. The `nonce` field provides idempotency.
     *
     * @param array{
     *   id: string, intentID: string, items: list<Item|ItemShape>, nonce: string
     * }|RequestCreateParams $params
     * @param RequestOpts|null $requestOptions
     *
     * @return BaseResponse<RequestNewResponse>
     *
     * @throws APIException
     */
    public function create(
        array|RequestCreateParams $params,
        RequestOptions|array|null $requestOptions = null,
    ): BaseResponse {
        [$parsed, $options] = RequestCreateParams::parseRequest(
            $params,
            $requestOptions,
        );

        // @phpstan-ignore-next-line return.type
        return $this->client->request(
            method: 'post',
            path: 'orders/requests',
            body: (object) $parsed,
            options: $options,
            convert: RequestNewResponse::class,
        );
    }
}
