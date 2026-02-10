<?php

declare(strict_types=1);

namespace LocalProtocol\Services;

use LocalProtocol\Client;
use LocalProtocol\Core\Exceptions\APIException;
use LocalProtocol\Merchants\MerchantGetResponse;
use LocalProtocol\RequestOptions;
use LocalProtocol\ServiceContracts\MerchantsContract;

/**
 * Read merchant profile and denormalized catalog data.
 *
 * @phpstan-import-type RequestOpts from \LocalProtocol\RequestOptions
 */
final class MerchantsService implements MerchantsContract
{
    /**
     * @api
     */
    public MerchantsRawService $raw;

    /**
     * @internal
     */
    public function __construct(private Client $client)
    {
        $this->raw = new MerchantsRawService($client);
    }

    /**
     * @api
     *
     * Returns a merchant with its full denormalized catalog tree.
     *
     * @param string $merchantID merchant identifier
     * @param RequestOpts|null $requestOptions
     *
     * @throws APIException
     */
    public function retrieve(
        string $merchantID,
        RequestOptions|array|null $requestOptions = null
    ): MerchantGetResponse {
        // @phpstan-ignore-next-line argument.type
        $response = $this->raw->retrieve($merchantID, requestOptions: $requestOptions);

        return $response->parse();
    }
}
