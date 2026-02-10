<?php

declare(strict_types=1);

namespace Tests;

use Symfony\Component\HttpClient\HttpClient;
use Symfony\Contracts\HttpClient\HttpClientInterface;

/**
 * Negative/validation tests for error paths.
 *
 * These use a raw HTTP client rather than the SDK to send invalid payloads
 * and verify the server returns appropriate error codes.
 */
class ValidationTest extends IntegrationTestBase
{
    private HttpClientInterface $httpClient;

    protected function setUp(): void
    {
        parent::setUp();
        $this->httpClient = HttpClient::create(['base_uri' => $this->baseUrl]);
    }

    // --- Request validation ---

    public function testCreateRequestMissingRequiredFieldReturns4xx(): void
    {
        $response = $this->httpClient->request('POST', '/requests', [
            'json' => ['id' => 'test-invalid'],
            'headers' => ['Content-Type' => 'application/json'],
        ]);
        $this->assertContains($response->getStatusCode(), [400, 422]);
    }

    public function testGetNonexistentRequestReturns404(): void
    {
        $response = $this->httpClient->request('GET', '/requests/nonexistent-request-id');
        $this->assertSame(404, $response->getStatusCode());
    }

    // --- Quote validation ---

    public function testCreateQuoteForNonexistentRequestReturns404(): void
    {
        $now = new \DateTimeImmutable('now', new \DateTimeZone('UTC'));

        $response = $this->httpClient->request('POST', '/requests/nonexistent-request-id/quotes', [
            'json' => [
                'id' => self::uuid(),
                'nonce' => self::uuid(),
                'price' => 1500,
                'currency' => 'USD',
                'payment' => new \stdClass(),
                'pickup_location' => ['coordinates' => ['latitude' => 37.7749, 'longitude' => -122.4194]],
                'dropoff_location' => ['coordinates' => ['latitude' => 37.7849, 'longitude' => -122.4094]],
                'pickup_estimate' => $now->add(new \DateInterval('PT25M'))->format('c'),
                'dropoff_estimate' => $now->add(new \DateInterval('PT55M'))->format('c'),
            ],
            'headers' => ['Content-Type' => 'application/json'],
        ]);
        $this->assertSame(404, $response->getStatusCode());
    }

    // --- Delivery validation ---

    public function testGetNonexistentDeliveryReturns404(): void
    {
        $response = $this->httpClient->request('GET', '/deliveries/nonexistent-delivery-id');
        $this->assertSame(404, $response->getStatusCode());
    }

    public function testUpdateEventOnNonexistentDeliveryReturns404(): void
    {
        $response = $this->httpClient->request('PATCH', '/deliveries/nonexistent-delivery-id/event', [
            'json' => ['event' => 'assigned', 'event_description' => 'test'],
            'headers' => ['Content-Type' => 'application/json'],
        ]);
        $this->assertSame(404, $response->getStatusCode());
    }

    // --- Idempotency ---

    public function testDuplicateRequestWithSameNonce(): void
    {
        $now = new \DateTimeImmutable('now', new \DateTimeZone('UTC'));
        $nonce = 'test-nonce-' . self::uuid();
        $payload = [
            'id' => self::uuid(),
            'nonce' => $nonce,
            'pickup_location' => ['coordinates' => ['latitude' => 37.7749, 'longitude' => -122.4194]],
            'dropoff_location' => ['coordinates' => ['latitude' => 37.7849, 'longitude' => -122.4094]],
            'pickup_time' => $now->add(new \DateInterval('PT30M'))->format('c'),
            'dropoff_time' => $now->add(new \DateInterval('PT1H'))->format('c'),
        ];

        $response1 = $this->httpClient->request('POST', '/requests', [
            'json' => $payload,
            'headers' => ['Content-Type' => 'application/json'],
        ]);
        $this->assertContains($response1->getStatusCode(), [200, 201]);

        $response2 = $this->httpClient->request('POST', '/requests', [
            'json' => $payload,
            'headers' => ['Content-Type' => 'application/json'],
        ]);
        $this->assertContains($response2->getStatusCode(), [200, 201]);

        $data1 = json_decode($response1->getContent(), true);
        $data2 = json_decode($response2->getContent(), true);
        $this->assertSame($data1['id'], $data2['id']);
    }
}
