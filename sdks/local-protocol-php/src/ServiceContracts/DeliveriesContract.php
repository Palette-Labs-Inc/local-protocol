<?php

declare(strict_types=1);

namespace LocalProtocol\ServiceContracts;

use LocalProtocol\Core\Exceptions\APIException;
use LocalProtocol\Deliveries\Delivery;
use LocalProtocol\RequestOptions;

/**
 * @phpstan-import-type RequestOpts from \LocalProtocol\RequestOptions
 */
interface DeliveriesContract
{
    /**
     * @api
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
    ): Delivery;

    /**
     * @api
     *
     * @param string $deliveryID delivery identifier
     * @param RequestOpts|null $requestOptions
     *
     * @throws APIException
     */
    public function retrieve(
        string $deliveryID,
        RequestOptions|array|null $requestOptions = null
    ): Delivery;

    /**
     * @api
     *
     * @param RequestOpts|null $requestOptions
     *
     * @return list<Delivery>
     *
     * @throws APIException
     */
    public function list(
        RequestOptions|array|null $requestOptions = null
    ): array;

    /**
     * @api
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
    ): Delivery;
}
