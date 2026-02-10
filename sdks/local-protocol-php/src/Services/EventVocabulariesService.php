<?php

declare(strict_types=1);

namespace LocalProtocol\Services;

use LocalProtocol\Client;
use LocalProtocol\Core\Exceptions\APIException;
use LocalProtocol\EventVocabularies\EventVocabularyGetResponse;
use LocalProtocol\RequestOptions;
use LocalProtocol\ServiceContracts\EventVocabulariesContract;

/**
 * @phpstan-import-type RequestOpts from \LocalProtocol\RequestOptions
 */
final class EventVocabulariesService implements EventVocabulariesContract
{
    /**
     * @api
     */
    public EventVocabulariesRawService $raw;

    /**
     * @internal
     */
    public function __construct(private Client $client)
    {
        $this->raw = new EventVocabulariesRawService($client);
    }

    /**
     * @api
     *
     * Returns a delivery event vocabulary by name.
     *
     * @param string $name Event vocabulary name in reverse-domain notation (e.g., xyz.localprotocol.delivery.courier).
     * @param RequestOpts|null $requestOptions
     *
     * @throws APIException
     */
    public function retrieve(
        string $name,
        RequestOptions|array|null $requestOptions = null
    ): EventVocabularyGetResponse {
        // @phpstan-ignore-next-line argument.type
        $response = $this->raw->retrieve($name, requestOptions: $requestOptions);

        return $response->parse();
    }
}
