<?php

declare(strict_types=1);

namespace LocalProtocol\Services;

use LocalProtocol\Client;
use LocalProtocol\Core\Contracts\BaseResponse;
use LocalProtocol\Core\Conversion\ListOf;
use LocalProtocol\Core\Exceptions\APIException;
use LocalProtocol\RequestOptions;
use LocalProtocol\Requests\DeliveryRequest;
use LocalProtocol\Requests\Location;
use LocalProtocol\Requests\RequestCreateParams;
use LocalProtocol\ServiceContracts\RequestsRawContract;

/**
 * Create and manage delivery requests.
 *
 * @phpstan-import-type LocationShape from \LocalProtocol\Requests\Location
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
     * Submit a new delivery request. The `nonce` field provides idempotency.
     *
     * @param array{
     *   id: string,
     *   dropoffLocation: Location|LocationShape,
     *   dropoffTime: \DateTimeInterface,
     *   nonce: string,
     *   pickupLocation: Location|LocationShape,
     *   pickupTime: \DateTimeInterface,
     *   dropoffInstructions?: string,
     *   pickupInstructions?: string,
     * }|RequestCreateParams $params
     * @param RequestOpts|null $requestOptions
     *
     * @return BaseResponse<DeliveryRequest>
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
            path: 'requests',
            body: (object) $parsed,
            options: $options,
            convert: DeliveryRequest::class,
        );
    }

    /**
     * @api
     *
     * Returns a single delivery request by ID.
     *
     * @param string $requestID delivery request identifier
     * @param RequestOpts|null $requestOptions
     *
     * @return BaseResponse<DeliveryRequest>
     *
     * @throws APIException
     */
    public function retrieve(
        string $requestID,
        RequestOptions|array|null $requestOptions = null
    ): BaseResponse {
        // @phpstan-ignore-next-line return.type
        return $this->client->request(
            method: 'get',
            path: ['requests/%1$s', $requestID],
            options: $requestOptions,
            convert: DeliveryRequest::class,
        );
    }

    /**
     * @api
     *
     * Returns all delivery requests.
     *
     * @param RequestOpts|null $requestOptions
     *
     * @return BaseResponse<list<DeliveryRequest>>
     *
     * @throws APIException
     */
    public function list(
        RequestOptions|array|null $requestOptions = null
    ): BaseResponse {
        // @phpstan-ignore-next-line return.type
        return $this->client->request(
            method: 'get',
            path: 'requests',
            options: $requestOptions,
            convert: new ListOf(DeliveryRequest::class),
        );
    }
}
