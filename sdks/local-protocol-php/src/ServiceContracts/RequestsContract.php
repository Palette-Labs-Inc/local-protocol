<?php

declare(strict_types=1);

namespace LocalProtocol\ServiceContracts;

use LocalProtocol\Core\Exceptions\APIException;
use LocalProtocol\RequestOptions;
use LocalProtocol\Requests\DeliveryRequest;
use LocalProtocol\Requests\Location;

/**
 * @phpstan-import-type LocationShape from \LocalProtocol\Requests\Location
 * @phpstan-import-type RequestOpts from \LocalProtocol\RequestOptions
 */
interface RequestsContract
{
    /**
     * @api
     *
     * @param string $id unique request identifier
     * @param Location|LocationShape $dropoffLocation A location specified by coordinates and/or postal address. At least one must be provided.
     * @param \DateTimeInterface $dropoffTime requested dropoff time (RFC 3339)
     * @param string $nonce client-generated idempotency key
     * @param Location|LocationShape $pickupLocation A location specified by coordinates and/or postal address. At least one must be provided.
     * @param \DateTimeInterface $pickupTime requested pickup time (RFC 3339)
     * @param string $dropoffInstructions dropoff directions, access codes, or delivery notes
     * @param string $pickupInstructions pickup directions, access codes, or handling notes
     * @param RequestOpts|null $requestOptions
     *
     * @throws APIException
     */
    public function create(
        string $id,
        Location|array $dropoffLocation,
        \DateTimeInterface $dropoffTime,
        string $nonce,
        Location|array $pickupLocation,
        \DateTimeInterface $pickupTime,
        ?string $dropoffInstructions = null,
        ?string $pickupInstructions = null,
        RequestOptions|array|null $requestOptions = null,
    ): DeliveryRequest;

    /**
     * @api
     *
     * @param string $requestID delivery request identifier
     * @param RequestOpts|null $requestOptions
     *
     * @throws APIException
     */
    public function retrieve(
        string $requestID,
        RequestOptions|array|null $requestOptions = null
    ): DeliveryRequest;

    /**
     * @api
     *
     * @param RequestOpts|null $requestOptions
     *
     * @return list<DeliveryRequest>
     *
     * @throws APIException
     */
    public function list(
        RequestOptions|array|null $requestOptions = null
    ): array;
}
