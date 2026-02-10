<?php

declare(strict_types=1);

namespace LocalProtocol\Services\Requests;

use LocalProtocol\Client;
use LocalProtocol\Core\Exceptions\APIException;
use LocalProtocol\Core\Util;
use LocalProtocol\PaymentInstruments\Payment;
use LocalProtocol\RequestOptions;
use LocalProtocol\Requests\Location;
use LocalProtocol\Requests\Quotes\DeliveryQuote;
use LocalProtocol\ServiceContracts\Requests\QuotesContract;

/**
 * @phpstan-import-type PaymentShape from \LocalProtocol\PaymentInstruments\Payment
 * @phpstan-import-type LocationShape from \LocalProtocol\Requests\Location
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
     * Submit a quote for a delivery request. The `nonce` field provides idempotency.
     *
     * @param string $requestID delivery request identifier
     * @param string $id unique quote identifier
     * @param string $currency ISO 4217 currency code
     * @param \DateTimeInterface $dropoffEstimate estimated dropoff time (RFC 3339)
     * @param Location|LocationShape $dropoffLocation A location specified by coordinates and/or postal address. At least one must be provided.
     * @param string $nonce client-generated idempotency key
     * @param Payment|PaymentShape $payment payment handlers available for accepting this quote
     * @param \DateTimeInterface $pickupEstimate estimated pickup time (RFC 3339)
     * @param Location|LocationShape $pickupLocation A location specified by coordinates and/or postal address. At least one must be provided.
     * @param int $price price in minor currency units
     * @param \DateTimeInterface $expiresAt time when the quote expires (RFC 3339)
     * @param RequestOpts|null $requestOptions
     *
     * @throws APIException
     */
    public function create(
        string $requestID,
        string $id,
        string $currency,
        \DateTimeInterface $dropoffEstimate,
        Location|array $dropoffLocation,
        string $nonce,
        Payment|array $payment,
        \DateTimeInterface $pickupEstimate,
        Location|array $pickupLocation,
        int $price,
        ?\DateTimeInterface $expiresAt = null,
        RequestOptions|array|null $requestOptions = null,
    ): DeliveryQuote {
        $params = Util::removeNulls(
            [
                'id' => $id,
                'currency' => $currency,
                'dropoffEstimate' => $dropoffEstimate,
                'dropoffLocation' => $dropoffLocation,
                'nonce' => $nonce,
                'payment' => $payment,
                'pickupEstimate' => $pickupEstimate,
                'pickupLocation' => $pickupLocation,
                'price' => $price,
                'expiresAt' => $expiresAt,
            ],
        );

        // @phpstan-ignore-next-line argument.type
        $response = $this->raw->create($requestID, params: $params, requestOptions: $requestOptions);

        return $response->parse();
    }

    /**
     * @api
     *
     * Returns a single quote by ID.
     *
     * @param string $quoteID quote identifier
     * @param string $requestID delivery request identifier
     * @param RequestOpts|null $requestOptions
     *
     * @throws APIException
     */
    public function retrieve(
        string $quoteID,
        string $requestID,
        RequestOptions|array|null $requestOptions = null,
    ): DeliveryQuote {
        $params = Util::removeNulls(['requestID' => $requestID]);

        // @phpstan-ignore-next-line argument.type
        $response = $this->raw->retrieve($quoteID, params: $params, requestOptions: $requestOptions);

        return $response->parse();
    }

    /**
     * @api
     *
     * Returns all quotes for a delivery request.
     *
     * @param string $requestID delivery request identifier
     * @param RequestOpts|null $requestOptions
     *
     * @return list<DeliveryQuote>
     *
     * @throws APIException
     */
    public function list(
        string $requestID,
        RequestOptions|array|null $requestOptions = null
    ): array {
        // @phpstan-ignore-next-line argument.type
        $response = $this->raw->list($requestID, requestOptions: $requestOptions);

        return $response->parse();
    }
}
