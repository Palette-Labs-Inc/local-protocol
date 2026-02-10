<?php

declare(strict_types=1);

namespace LocalProtocol\ServiceContracts;

use LocalProtocol\Core\Exceptions\APIException;
use LocalProtocol\EventVocabularies\EventVocabularyGetResponse;
use LocalProtocol\RequestOptions;

/**
 * @phpstan-import-type RequestOpts from \LocalProtocol\RequestOptions
 */
interface EventVocabulariesContract
{
    /**
     * @api
     *
     * @param string $name Event vocabulary name in reverse-domain notation (e.g., xyz.localprotocol.delivery.courier).
     * @param RequestOpts|null $requestOptions
     *
     * @throws APIException
     */
    public function retrieve(
        string $name,
        RequestOptions|array|null $requestOptions = null
    ): EventVocabularyGetResponse;
}
