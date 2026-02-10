<?php

declare(strict_types=1);

namespace LocalProtocol\Services;

use LocalProtocol\Client;
use LocalProtocol\Core\Contracts\BaseResponse;
use LocalProtocol\Core\Conversion\ListOf;
use LocalProtocol\Core\Exceptions\APIException;
use LocalProtocol\Deliveries\Delivery;
use LocalProtocol\Deliveries\DeliveryCreateParams;
use LocalProtocol\Deliveries\DeliveryUpdateEventParams;
use LocalProtocol\RequestOptions;
use LocalProtocol\ServiceContracts\DeliveriesRawContract;

/**
 * Accept quotes and manage delivery lifecycle state.
 *
 * @phpstan-import-type RequestOpts from \LocalProtocol\RequestOptions
 */
final class DeliveriesRawService implements DeliveriesRawContract
{
    // @phpstan-ignore-next-line
    /**
     * @internal
     */
    public function __construct(private Client $client) {}

    /**
     * @api
     *
     * Accept a quote and create a delivery. The `nonce` field provides idempotency.
     *
     * @param array{
     *   nonce: string,
     *   quoteID: string,
     *   requestID: string,
     *   eventVocabulary?: string,
     *   webhookURL?: string|null,
     * }|DeliveryCreateParams $params
     * @param RequestOpts|null $requestOptions
     *
     * @return BaseResponse<Delivery>
     *
     * @throws APIException
     */
    public function create(
        array|DeliveryCreateParams $params,
        RequestOptions|array|null $requestOptions = null,
    ): BaseResponse {
        [$parsed, $options] = DeliveryCreateParams::parseRequest(
            $params,
            $requestOptions,
        );

        // @phpstan-ignore-next-line return.type
        return $this->client->request(
            method: 'post',
            path: 'deliveries',
            body: (object) $parsed,
            options: $options,
            convert: Delivery::class,
        );
    }

    /**
     * @api
     *
     * Returns a single delivery by ID.
     *
     * @param string $deliveryID delivery identifier
     * @param RequestOpts|null $requestOptions
     *
     * @return BaseResponse<Delivery>
     *
     * @throws APIException
     */
    public function retrieve(
        string $deliveryID,
        RequestOptions|array|null $requestOptions = null
    ): BaseResponse {
        // @phpstan-ignore-next-line return.type
        return $this->client->request(
            method: 'get',
            path: ['deliveries/%1$s', $deliveryID],
            options: $requestOptions,
            convert: Delivery::class,
        );
    }

    /**
     * @api
     *
     * Returns all deliveries.
     *
     * @param RequestOpts|null $requestOptions
     *
     * @return BaseResponse<list<Delivery>>
     *
     * @throws APIException
     */
    public function list(
        RequestOptions|array|null $requestOptions = null
    ): BaseResponse {
        // @phpstan-ignore-next-line return.type
        return $this->client->request(
            method: 'get',
            path: 'deliveries',
            options: $requestOptions,
            convert: new ListOf(Delivery::class),
        );
    }

    /**
     * @api
     *
     * Transition a delivery to a new event state. If a webhook URL was registered, the server pushes an event notification in the background.
     *
     * @param string $deliveryID delivery identifier
     * @param array{
     *   event: string, eventDescription: string
     * }|DeliveryUpdateEventParams $params
     * @param RequestOpts|null $requestOptions
     *
     * @return BaseResponse<Delivery>
     *
     * @throws APIException
     */
    public function updateEvent(
        string $deliveryID,
        array|DeliveryUpdateEventParams $params,
        RequestOptions|array|null $requestOptions = null,
    ): BaseResponse {
        [$parsed, $options] = DeliveryUpdateEventParams::parseRequest(
            $params,
            $requestOptions,
        );

        // @phpstan-ignore-next-line return.type
        return $this->client->request(
            method: 'patch',
            path: ['deliveries/%1$s/event', $deliveryID],
            body: (object) $parsed,
            options: $options,
            convert: Delivery::class,
        );
    }
}
