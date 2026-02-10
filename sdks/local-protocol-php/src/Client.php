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
 * @phpstan-import-type RequestOpts from \LocalProtocol\RequestOptions
 */
class Client extends BaseClient
{
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
        ?string $baseUrl = null,
        RequestOptions|array|null $requestOptions = null
    ) {
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
                'X-Stainless-Package-Version' => '0.1.0',
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
}
