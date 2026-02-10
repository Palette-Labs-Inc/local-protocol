<?php

declare(strict_types=1);

namespace LocalProtocol\Services;

use LocalProtocol\Client;
use LocalProtocol\Core\Contracts\BaseResponse;
use LocalProtocol\Core\Exceptions\APIException;
use LocalProtocol\Healthz\HealthzCheckResponse;
use LocalProtocol\RequestOptions;
use LocalProtocol\ServiceContracts\HealthzRawContract;

/**
 * @phpstan-import-type RequestOpts from \LocalProtocol\RequestOptions
 */
final class HealthzRawService implements HealthzRawContract
{
    // @phpstan-ignore-next-line
    /**
     * @internal
     */
    public function __construct(private Client $client) {}

    /**
     * @api
     *
     * Returns server health status.
     *
     * @param RequestOpts|null $requestOptions
     *
     * @return BaseResponse<HealthzCheckResponse>
     *
     * @throws APIException
     */
    public function check(
        RequestOptions|array|null $requestOptions = null
    ): BaseResponse {
        // @phpstan-ignore-next-line return.type
        return $this->client->request(
            method: 'get',
            path: 'healthz',
            options: $requestOptions,
            convert: HealthzCheckResponse::class,
        );
    }
}
