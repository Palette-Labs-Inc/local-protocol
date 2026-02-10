<?php

declare(strict_types=1);

namespace LocalProtocol\ServiceContracts;

use LocalProtocol\Core\Exceptions\APIException;
use LocalProtocol\Merchants\MerchantGetResponse;
use LocalProtocol\RequestOptions;

/**
 * @phpstan-import-type RequestOpts from \LocalProtocol\RequestOptions
 */
interface MerchantsContract
{
    /**
     * @api
     *
     * @param string $merchantID merchant identifier
     * @param RequestOpts|null $requestOptions
     *
     * @throws APIException
     */
    public function retrieve(
        string $merchantID,
        RequestOptions|array|null $requestOptions = null
    ): MerchantGetResponse;
}
