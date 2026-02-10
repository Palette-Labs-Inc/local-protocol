<?php

declare(strict_types=1);

namespace LocalProtocol\Services;

use LocalProtocol\Client;
use LocalProtocol\Core\Contracts\BaseResponse;
use LocalProtocol\Core\Exceptions\APIException;
use LocalProtocol\Merchants\MerchantGetResponse;
use LocalProtocol\RequestOptions;
use LocalProtocol\ServiceContracts\MerchantsRawContract;

/**
 * @phpstan-import-type RequestOpts from \LocalProtocol\RequestOptions
 */
final class MerchantsRawService implements MerchantsRawContract
{
    // @phpstan-ignore-next-line
    /**
     * @internal
     */
    public function __construct(private Client $client) {}

    /**
     * @api
     *
     * Returns a merchant with its full denormalized catalog tree.
     *
     * @param string $merchantID merchant identifier
     * @param RequestOpts|null $requestOptions
     *
     * @return BaseResponse<MerchantGetResponse>
     *
     * @throws APIException
     */
    public function retrieve(
        string $merchantID,
        RequestOptions|array|null $requestOptions = null
    ): BaseResponse {
        // @phpstan-ignore-next-line return.type
        return $this->client->request(
            method: 'get',
            path: ['merchants/%1$s', $merchantID],
            options: $requestOptions,
            convert: MerchantGetResponse::class,
        );
    }
}
