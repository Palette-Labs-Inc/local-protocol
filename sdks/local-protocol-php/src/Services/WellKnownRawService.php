<?php

declare(strict_types=1);

namespace LocalProtocol\Services;

use LocalProtocol\Client;
use LocalProtocol\Core\Contracts\BaseResponse;
use LocalProtocol\Core\Exceptions\APIException;
use LocalProtocol\RequestOptions;
use LocalProtocol\ServiceContracts\WellKnownRawContract;
use LocalProtocol\WellKnown\WellKnownGetResponse;

/**
 * @phpstan-import-type RequestOpts from \LocalProtocol\RequestOptions
 */
final class WellKnownRawService implements WellKnownRawContract
{
    // @phpstan-ignore-next-line
    /**
     * @internal
     */
    public function __construct(private Client $client) {}

    /**
     * @api
     *
     * Returns server capabilities, supported standards, and endpoint paths.
     *
     * @param RequestOpts|null $requestOptions
     *
     * @return BaseResponse<WellKnownGetResponse>
     *
     * @throws APIException
     */
    public function retrieve(
        RequestOptions|array|null $requestOptions = null
    ): BaseResponse {
        // @phpstan-ignore-next-line return.type
        return $this->client->request(
            method: 'get',
            path: '.well-known/local-protocol',
            options: $requestOptions,
            convert: WellKnownGetResponse::class,
        );
    }
}
