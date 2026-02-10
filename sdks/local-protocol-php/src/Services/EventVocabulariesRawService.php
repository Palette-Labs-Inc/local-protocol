<?php

declare(strict_types=1);

namespace LocalProtocol\Services;

use LocalProtocol\Client;
use LocalProtocol\Core\Contracts\BaseResponse;
use LocalProtocol\Core\Exceptions\APIException;
use LocalProtocol\EventVocabularies\EventVocabularyGetResponse;
use LocalProtocol\RequestOptions;
use LocalProtocol\ServiceContracts\EventVocabulariesRawContract;

/**
 * @phpstan-import-type RequestOpts from \LocalProtocol\RequestOptions
 */
final class EventVocabulariesRawService implements EventVocabulariesRawContract
{
    // @phpstan-ignore-next-line
    /**
     * @internal
     */
    public function __construct(private Client $client) {}

    /**
     * @api
     *
     * Returns a delivery event vocabulary by name.
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
    ): BaseResponse {
        // @phpstan-ignore-next-line return.type
        return $this->client->request(
            method: 'get',
            path: ['event-vocabularies/%1$s', $name],
            options: $requestOptions,
            convert: EventVocabularyGetResponse::class,
        );
    }
}
