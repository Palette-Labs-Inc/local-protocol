<?php

declare(strict_types=1);

namespace Tests;

use DateInterval;
use DateTimeImmutable;
use LocalProtocol\Client;
use LocalProtocol\Deliveries\Delivery;
use LocalProtocol\Requests\DeliveryRequest;
use LocalProtocol\Requests\Quotes\DeliveryQuote;
use PHPUnit\Framework\TestCase;

abstract class IntegrationTestBase extends TestCase
{
    protected Client $sdk;
    protected string $baseUrl;

    protected function setUp(): void
    {
        parent::setUp();
        $this->baseUrl = getenv('TEST_API_BASE_URL') ?: 'http://localhost:8000';
        $this->sdk = new Client(
            apiKey: 'test',
            baseUrl: $this->baseUrl,
        );
    }

    protected function createRequest(
        ?string $requestId = null,
        float $pickupLat = 37.7749,
        float $pickupLng = -122.4194,
        float $dropoffLat = 37.7849,
        float $dropoffLng = -122.4094,
    ): DeliveryRequest {
        $now = new DateTimeImmutable('now', new \DateTimeZone('UTC'));

        return $this->sdk->requests->create(
            id: $requestId ?? self::uuid(),
            dropoffLocation: [
                'coordinates' => ['latitude' => $dropoffLat, 'longitude' => $dropoffLng],
            ],
            dropoffTime: $now->add(new DateInterval('PT1H')),
            nonce: self::uuid(),
            pickupLocation: [
                'coordinates' => ['latitude' => $pickupLat, 'longitude' => $pickupLng],
            ],
            pickupTime: $now->add(new DateInterval('PT30M')),
        );
    }

    protected function createQuote(
        string $requestId,
        ?string $quoteId = null,
        int $price = 1500,
        string $currency = 'USD',
    ): DeliveryQuote {
        $now = new DateTimeImmutable('now', new \DateTimeZone('UTC'));

        return $this->sdk->requests->quotes->create(
            requestID: $requestId,
            id: $quoteId ?? self::uuid(),
            currency: $currency,
            dropoffEstimate: $now->add(new DateInterval('PT55M')),
            dropoffLocation: [
                'coordinates' => ['latitude' => 37.7849, 'longitude' => -122.4094],
            ],
            nonce: self::uuid(),
            payment: [],
            pickupEstimate: $now->add(new DateInterval('PT25M')),
            pickupLocation: [
                'coordinates' => ['latitude' => 37.7749, 'longitude' => -122.4194],
            ],
            price: $price,
        );
    }

    protected function createDelivery(
        ?string $webhookUrl = null,
    ): Delivery {
        $req = $this->createRequest();
        $quote = $this->createQuote($req->id);

        return $this->sdk->deliveries->create(
            nonce: self::uuid(),
            quoteID: $quote->id,
            requestID: $req->id,
            webhookURL: $webhookUrl,
        );
    }

    protected static function uuid(): string
    {
        return sprintf(
            '%04x%04x-%04x-%04x-%04x-%04x%04x%04x',
            mt_rand(0, 0xffff), mt_rand(0, 0xffff),
            mt_rand(0, 0xffff),
            mt_rand(0, 0x0fff) | 0x4000,
            mt_rand(0, 0x3fff) | 0x8000,
            mt_rand(0, 0xffff), mt_rand(0, 0xffff), mt_rand(0, 0xffff)
        );
    }
}
