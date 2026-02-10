<?php

declare(strict_types=1);

namespace LocalProtocol\ServiceContracts;

use LocalProtocol\Core\Contracts\BaseResponse;
use LocalProtocol\Core\Exceptions\APIException;
use LocalProtocol\PaymentInstruments\EvmAuthCaptureEscrowInstrument;
use LocalProtocol\PaymentInstruments\PaymentInstrumentRegisterParams;
use LocalProtocol\RequestOptions;

/**
 * @phpstan-import-type RequestOpts from \LocalProtocol\RequestOptions
 */
interface PaymentInstrumentsRawContract
{
    /**
     * @api
     *
     * @param array<string,mixed>|PaymentInstrumentRegisterParams $params
     * @param RequestOpts|null $requestOptions
     *
     * @return BaseResponse<EvmAuthCaptureEscrowInstrument>
     *
     * @throws APIException
     */
    public function register(
        array|PaymentInstrumentRegisterParams $params,
        RequestOptions|array|null $requestOptions = null,
    ): BaseResponse;
}
