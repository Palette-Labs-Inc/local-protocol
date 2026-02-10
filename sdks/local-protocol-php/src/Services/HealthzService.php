<?php

declare(strict_types=1);

namespace LocalProtocol\Services;

use LocalProtocol\Client;
use LocalProtocol\Core\Exceptions\APIException;
use LocalProtocol\Healthz\HealthzCheckResponse;
use LocalProtocol\RequestOptions;
use LocalProtocol\ServiceContracts\HealthzContract;

/**
 * @phpstan-import-type RequestOpts from \LocalProtocol\RequestOptions
 */
final class HealthzService implements HealthzContract
{
    /**
     * @api
     */
    public HealthzRawService $raw;

    /**
     * @internal
     */
    public function __construct(private Client $client)
    {
        $this->raw = new HealthzRawService($client);
    }

    /**
     * @api
     *
     * Returns server health status.
     *
     * @param RequestOpts|null $requestOptions
     *
     * @throws APIException
     */
    public function check(
        RequestOptions|array|null $requestOptions = null
    ): HealthzCheckResponse {
        // @phpstan-ignore-next-line argument.type
        $response = $this->raw->check(requestOptions: $requestOptions);

        return $response->parse();
    }
}
