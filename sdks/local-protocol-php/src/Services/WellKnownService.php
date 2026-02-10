<?php

declare(strict_types=1);

namespace LocalProtocol\Services;

use LocalProtocol\Client;
use LocalProtocol\Core\Exceptions\APIException;
use LocalProtocol\RequestOptions;
use LocalProtocol\ServiceContracts\WellKnownContract;
use LocalProtocol\WellKnown\WellKnownGetResponse;

/**
 * Discover server capabilities, standards, and endpoints.
 *
 * @phpstan-import-type RequestOpts from \LocalProtocol\RequestOptions
 */
final class WellKnownService implements WellKnownContract
{
    /**
     * @api
     */
    public WellKnownRawService $raw;

    /**
     * @internal
     */
    public function __construct(private Client $client)
    {
        $this->raw = new WellKnownRawService($client);
    }

    /**
     * @api
     *
     * Returns server capabilities, supported standards, and endpoint paths.
     *
     * @param RequestOpts|null $requestOptions
     *
     * @throws APIException
     */
    public function retrieve(
        RequestOptions|array|null $requestOptions = null
    ): WellKnownGetResponse {
        // @phpstan-ignore-next-line argument.type
        $response = $this->raw->retrieve(requestOptions: $requestOptions);

        return $response->parse();
    }
}
