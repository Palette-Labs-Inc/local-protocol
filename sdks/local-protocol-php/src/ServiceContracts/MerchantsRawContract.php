<?php

declare(strict_types=1);

namespace LocalProtocol\ServiceContracts;

use LocalProtocol\Core\Contracts\BaseResponse;
use LocalProtocol\Core\Exceptions\APIException;
use LocalProtocol\Merchants\MerchantGetResponse;
use LocalProtocol\RequestOptions;

/**
 * @phpstan-import-type RequestOpts from \LocalProtocol\RequestOptions
 */
interface MerchantsRawContract
{
    /**
     * @api
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
    ): BaseResponse;
}
