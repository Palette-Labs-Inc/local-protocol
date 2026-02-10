<?php

declare(strict_types=1);

namespace LocalProtocol\Services\Requests;

use LocalProtocol\Client;
use LocalProtocol\Core\Contracts\BaseResponse;
use LocalProtocol\Core\Conversion\ListOf;
use LocalProtocol\Core\Exceptions\APIException;
use LocalProtocol\RequestOptions;
use LocalProtocol\Requests\Location;
use LocalProtocol\Requests\Quotes\DeliveryQuote;
use LocalProtocol\Requests\Quotes\QuoteCreateParams;
use LocalProtocol\Requests\Quotes\QuoteCreateParams\Payment;
use LocalProtocol\Requests\Quotes\QuoteRetrieveParams;
use LocalProtocol\ServiceContracts\Requests\QuotesRawContract;

/**
 * @phpstan-import-type PaymentShape from \LocalProtocol\Requests\Quotes\QuoteCreateParams\Payment
 * @phpstan-import-type LocationShape from \LocalProtocol\Requests\Location
 * @phpstan-import-type RequestOpts from \LocalProtocol\RequestOptions
 */
final class QuotesRawService implements QuotesRawContract
{
    // @phpstan-ignore-next-line
    /**
     * @internal
     */
    public function __construct(private Client $client) {}

    /**
     * @api
     *
     * Submit a quote for a delivery request. The `nonce` field provides idempotency.
     *
     * @param string $requestID delivery request identifier
     * @param array{
     *   id: string,
     *   currency: string,
     *   dropoffEstimate: \DateTimeInterface,
     *   dropoffLocation: Location|LocationShape,
     *   nonce: string,
     *   payment: Payment|PaymentShape,
     *   pickupEstimate: \DateTimeInterface,
     *   pickupLocation: Location|LocationShape,
     *   price: int,
     *   expiresAt?: \DateTimeInterface,
     * }|QuoteCreateParams $params
     * @param RequestOpts|null $requestOptions
     *
     * @return BaseResponse<DeliveryQuote>
     *
     * @throws APIException
     */
    public function create(
        string $requestID,
        array|QuoteCreateParams $params,
        RequestOptions|array|null $requestOptions = null,
    ): BaseResponse {
        [$parsed, $options] = QuoteCreateParams::parseRequest(
            $params,
            $requestOptions,
        );

        // @phpstan-ignore-next-line return.type
        return $this->client->request(
            method: 'post',
            path: ['requests/%1$s/quotes', $requestID],
            body: (object) $parsed,
            options: $options,
            convert: DeliveryQuote::class,
        );
    }

    /**
     * @api
     *
     * Returns a single quote by ID.
     *
     * @param string $quoteID quote identifier
     * @param array{requestID: string}|QuoteRetrieveParams $params
     * @param RequestOpts|null $requestOptions
     *
     * @return BaseResponse<DeliveryQuote>
     *
     * @throws APIException
     */
    public function retrieve(
        string $quoteID,
        array|QuoteRetrieveParams $params,
        RequestOptions|array|null $requestOptions = null,
    ): BaseResponse {
        [$parsed, $options] = QuoteRetrieveParams::parseRequest(
            $params,
            $requestOptions,
        );
        $requestID = $parsed['requestID'];
        unset($parsed['requestID']);

        // @phpstan-ignore-next-line return.type
        return $this->client->request(
            method: 'get',
            path: ['requests/%1$s/quotes/%2$s', $requestID, $quoteID],
            options: $options,
            convert: DeliveryQuote::class,
        );
    }

    /**
     * @api
     *
     * Returns all quotes for a delivery request.
     *
     * @param string $requestID delivery request identifier
     * @param RequestOpts|null $requestOptions
     *
     * @return BaseResponse<list<DeliveryQuote>>
     *
     * @throws APIException
     */
    public function list(
        string $requestID,
        RequestOptions|array|null $requestOptions = null
    ): BaseResponse {
        // @phpstan-ignore-next-line return.type
        return $this->client->request(
            method: 'get',
            path: ['requests/%1$s/quotes', $requestID],
            options: $requestOptions,
            convert: new ListOf(DeliveryQuote::class),
        );
    }
}
