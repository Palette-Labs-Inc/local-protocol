<?php

declare(strict_types=1);

namespace LocalProtocol;

use Http\Discovery\Psr17FactoryDiscovery;
use Http\Discovery\Psr18ClientDiscovery;
use LocalProtocol\Core\BaseClient;
use LocalProtocol\Core\Util;
use LocalProtocol\Services\DeliveriesService;
use LocalProtocol\Services\EventVocabulariesService;
use LocalProtocol\Services\HealthzService;
use LocalProtocol\Services\MerchantsService;
use LocalProtocol\Services\OrdersService;
use LocalProtocol\Services\PaymentInstrumentsService;
use LocalProtocol\Services\RequestsService;
use LocalProtocol\Services\WellKnownService;

/**
 * @phpstan-import-type NormalizedRequest from \LocalProtocol\Core\BaseClient
 * @phpstan-import-type RequestOpts from \LocalProtocol\RequestOptions
 */
class Client extends BaseClient
{
    public string $apiKey;

    /**
     * @api
     */
    public WellKnownService $wellKnown;

    /**
     * @api
     */
    public HealthzService $healthz;

    /**
     * @api
     */
    public RequestsService $requests;

    /**
     * @api
     */
    public DeliveriesService $deliveries;

    /**
     * @api
     */
    public MerchantsService $merchants;

    /**
     * @api
     */
    public OrdersService $orders;

    /**
     * @api
     */
    public EventVocabulariesService $eventVocabularies;

    /**
     * @api
     */
    public PaymentInstrumentsService $paymentInstruments;

    /**
     * @param RequestOpts|null $requestOptions
     */
    public function __construct(
        ?string $apiKey = null,
        ?string $baseUrl = null,
        RequestOptions|array|null $requestOptions = null,
    ) {
        $this->apiKey = (string) ($apiKey ?? Util::getenv('LOCAL_PROTOCOL_API_KEY'));

        $baseUrl ??= Util::getenv(
            'LOCAL_PROTOCOL_BASE_URL'
        ) ?: 'http://localhost:8000';

        $options = RequestOptions::parse(
            RequestOptions::with(
                uriFactory: Psr17FactoryDiscovery::findUriFactory(),
                streamFactory: Psr17FactoryDiscovery::findStreamFactory(),
                requestFactory: Psr17FactoryDiscovery::findRequestFactory(),
                transporter: Psr18ClientDiscovery::find(),
            ),
            $requestOptions,
        );

        parent::__construct(
            headers: [
                'Content-Type' => 'application/json',
                'Accept' => 'application/json',
                'User-Agent' => sprintf('local-protocol/PHP %s', VERSION),
                'X-Stainless-Lang' => 'php',
                'X-Stainless-Package-Version' => '0.0.1',
                'X-Stainless-Arch' => Util::machtype(),
                'X-Stainless-OS' => Util::ostype(),
                'X-Stainless-Runtime' => php_sapi_name(),
                'X-Stainless-Runtime-Version' => phpversion(),
            ],
            baseUrl: $baseUrl,
            options: $options
        );

        $this->wellKnown = new WellKnownService($this);
        $this->healthz = new HealthzService($this);
        $this->requests = new RequestsService($this);
        $this->deliveries = new DeliveriesService($this);
        $this->merchants = new MerchantsService($this);
        $this->orders = new OrdersService($this);
        $this->eventVocabularies = new EventVocabulariesService($this);
        $this->paymentInstruments = new PaymentInstrumentsService($this);
    }

    /** @return array<string,string> */
    protected function authHeaders(): array
    {
        return $this->apiKey ? ['Authorization' => "Bearer {$this->apiKey}"] : [];
    }

    /**
     * @internal
     *
     * @param string|list<string> $path
     * @param array<string,mixed> $query
     * @param array<string,string|int|list<string|int>|null> $headers
     * @param RequestOpts|null $opts
     *
     * @return array{NormalizedRequest, RequestOptions}
     */
    protected function buildRequest(
        string $method,
        string|array $path,
        array $query,
        array $headers,
        mixed $body,
        RequestOptions|array|null $opts,
    ): array {
        return parent::buildRequest(
            method: $method,
            path: $path,
            query: $query,
            headers: [...$this->authHeaders(), ...$headers],
            body: $body,
            opts: $opts,
        );
    }
}
