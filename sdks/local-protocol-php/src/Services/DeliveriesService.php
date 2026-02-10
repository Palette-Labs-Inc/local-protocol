<?php

declare(strict_types=1);

namespace LocalProtocol\Services;

use LocalProtocol\Client;
use LocalProtocol\Core\Exceptions\APIException;
use LocalProtocol\Core\Util;
use LocalProtocol\Deliveries\Delivery;
use LocalProtocol\RequestOptions;
use LocalProtocol\ServiceContracts\DeliveriesContract;

/**
 * Accept quotes and manage delivery lifecycle state.
 *
 * @phpstan-import-type RequestOpts from \LocalProtocol\RequestOptions
 */
final class DeliveriesService implements DeliveriesContract
{
    /**
     * @api
     */
    public DeliveriesRawService $raw;

    /**
     * @internal
     */
    public function __construct(private Client $client)
    {
        $this->raw = new DeliveriesRawService($client);
    }

    /**
     * @api
     *
     * Accept a quote and create a delivery. The `nonce` field provides idempotency.
     *
     * @param string $nonce client-generated idempotency key
     * @param string $quoteID the accepted quote
     * @param string $requestID the delivery request to fulfill
     * @param string $eventVocabulary event vocabulary standard to use
     * @param string|null $webhookURL optional URL to receive delivery event webhook notifications
     * @param RequestOpts|null $requestOptions
     *
     * @throws APIException
     */
    public function create(
        string $nonce,
        string $quoteID,
        string $requestID,
        string $eventVocabulary = 'xyz.localprotocol.delivery.courier@2026-01-30',
        ?string $webhookURL = null,
        RequestOptions|array|null $requestOptions = null,
    ): Delivery {
        $params = Util::removeNulls(
            [
                'nonce' => $nonce,
                'quoteID' => $quoteID,
                'requestID' => $requestID,
                'eventVocabulary' => $eventVocabulary,
                'webhookURL' => $webhookURL,
            ],
        );

        // @phpstan-ignore-next-line argument.type
        $response = $this->raw->create(params: $params, requestOptions: $requestOptions);

        return $response->parse();
    }

    /**
     * @api
     *
     * Returns a single delivery by ID.
     *
     * @param string $deliveryID delivery identifier
     * @param RequestOpts|null $requestOptions
     *
     * @throws APIException
     */
    public function retrieve(
        string $deliveryID,
        RequestOptions|array|null $requestOptions = null
    ): Delivery {
        // @phpstan-ignore-next-line argument.type
        $response = $this->raw->retrieve($deliveryID, requestOptions: $requestOptions);

        return $response->parse();
    }

    /**
     * @api
     *
     * Returns all deliveries.
     *
     * @param RequestOpts|null $requestOptions
     *
     * @return list<Delivery>
     *
     * @throws APIException
     */
    public function list(
        RequestOptions|array|null $requestOptions = null
    ): array {
        // @phpstan-ignore-next-line argument.type
        $response = $this->raw->list(requestOptions: $requestOptions);

        return $response->parse();
    }

    /**
     * @api
     *
     * Transition a delivery to a new event state. If a webhook URL was registered, the server pushes an event notification in the background.
     *
     * @param string $deliveryID delivery identifier
     * @param string $event event identifier from the delivery's event vocabulary
     * @param string $eventDescription human-readable event description
     * @param RequestOpts|null $requestOptions
     *
     * @throws APIException
     */
    public function updateEvent(
        string $deliveryID,
        string $event,
        string $eventDescription,
        RequestOptions|array|null $requestOptions = null,
    ): Delivery {
        $params = Util::removeNulls(
            ['event' => $event, 'eventDescription' => $eventDescription]
        );

        // @phpstan-ignore-next-line argument.type
        $response = $this->raw->updateEvent($deliveryID, params: $params, requestOptions: $requestOptions);

        return $response->parse();
    }
}
