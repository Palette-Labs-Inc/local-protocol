<?php
/**
 * Request validation integration tests.
 *
 * Mirrors packages/conformance/validation_test.py.
 * Run against a live server:
 *   SERVER_URL=http://localhost:8000 vendor/bin/phpunit test/Integration/
 */

namespace LocalProtocolSdk\Test\Integration;

use GuzzleHttp\Client;
use PHPUnit\Framework\TestCase;

class ValidationTest extends TestCase
{
    private Client $client;
    private string $baseUrl;

    protected function setUp(): void
    {
        $this->baseUrl = getenv('SERVER_URL') ?: 'http://localhost:8000';
        $this->client = new Client([
            'base_uri' => $this->baseUrl,
            'http_errors' => false,
            'headers' => ['Content-Type' => 'application/json'],
        ]);
    }

    // -- helpers --

    private function createRequestPayload(): array
    {
        return [
            'id' => self::uuid(),
            'nonce' => self::uuid(),
            'pickup_location' => [
                'coordinates' => ['latitude' => 37.7749, 'longitude' => -122.4194],
            ],
            'dropoff_location' => [
                'coordinates' => ['latitude' => 37.7849, 'longitude' => -122.4094],
            ],
            'pickup_time' => gmdate('Y-m-d\TH:i:s\Z', time() + 1800),
            'dropoff_time' => gmdate('Y-m-d\TH:i:s\Z', time() + 3600),
        ];
    }

    private static function uuid(): string
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

    // -- request validation tests --

    public function testRequestRequiresPickupLocation(): void
    {
        $payload = $this->createRequestPayload();
        unset($payload['pickup_location']);

        $response = $this->client->post('/requests', ['json' => $payload]);
        $this->assertContains($response->getStatusCode(), [400, 422]);
    }

    public function testRequestRequiresDropoffLocation(): void
    {
        $payload = $this->createRequestPayload();
        unset($payload['dropoff_location']);

        $response = $this->client->post('/requests', ['json' => $payload]);
        $this->assertContains($response->getStatusCode(), [400, 422]);
    }

    public function testRequestRequiresPickupTime(): void
    {
        $payload = $this->createRequestPayload();
        unset($payload['pickup_time']);

        $response = $this->client->post('/requests', ['json' => $payload]);
        $this->assertContains($response->getStatusCode(), [400, 422]);
    }

    public function testRequestRequiresDropoffTime(): void
    {
        $payload = $this->createRequestPayload();
        unset($payload['dropoff_time']);

        $response = $this->client->post('/requests', ['json' => $payload]);
        $this->assertContains($response->getStatusCode(), [400, 422]);
    }

    public function testRequestInvalidTimeFormatRejected(): void
    {
        $payload = $this->createRequestPayload();
        $payload['pickup_time'] = 'not-a-valid-datetime';

        $response = $this->client->post('/requests', ['json' => $payload]);
        $this->assertContains($response->getStatusCode(), [400, 422]);
    }
}
