<?php

declare(strict_types=1);

namespace LocalProtocol\ServiceContracts;

use LocalProtocol\Core\Contracts\BaseResponse;
use LocalProtocol\Core\Exceptions\APIException;
use LocalProtocol\EventVocabularies\EventVocabularyGetResponse;
use LocalProtocol\RequestOptions;

/**
 * @phpstan-import-type RequestOpts from \LocalProtocol\RequestOptions
 */
interface EventVocabulariesRawContract
{
    /**
     * @api
     *
     * @param string $name Event vocabulary name in reverse-domain notation (e.g., xyz.localprotocol.delivery.courier).
     * @param RequestOpts|null $requestOptions
     *
     * @return BaseResponse<EventVocabularyGetResponse>
     *
     * @throws APIException
     */
    public function retrieve(
        string $name,
        RequestOptions|array|null $requestOptions = null
    ): BaseResponse;
}
