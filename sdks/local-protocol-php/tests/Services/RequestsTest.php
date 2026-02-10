<?php

namespace Tests\Services;

use LocalProtocol\Client;
use LocalProtocol\Core\Util;
use LocalProtocol\Requests\DeliveryRequest;
use PHPUnit\Framework\Attributes\CoversNothing;
use PHPUnit\Framework\Attributes\Test;
use PHPUnit\Framework\TestCase;
use Tests\UnsupportedMockTests;

/**
 * @internal
 */
#[CoversNothing]
final class RequestsTest extends TestCase
{
    protected Client $client;

    protected function setUp(): void
    {
        parent::setUp();

        $testUrl = Util::getenv('TEST_API_BASE_URL') ?: 'http://127.0.0.1:4010';
        $client = new Client(baseUrl: $testUrl);

        $this->client = $client;
    }

    #[Test]
    public function testCreate(): void
    {
        if (UnsupportedMockTests::$skip) {
            $this->markTestSkipped('Prism tests are disabled');
        }

        $result = $this->client->requests->create(
            id: 'id',
            dropoffLocation: [],
            dropoffTime: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
            nonce: 'nonce',
            pickupLocation: [],
            pickupTime: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
        );

        // @phpstan-ignore-next-line method.alreadyNarrowedType
        $this->assertInstanceOf(DeliveryRequest::class, $result);
    }

    #[Test]
    public function testCreateWithOptionalParams(): void
    {
        if (UnsupportedMockTests::$skip) {
            $this->markTestSkipped('Prism tests are disabled');
        }

        $result = $this->client->requests->create(
            id: 'id',
            dropoffLocation: [
                'coordinates' => ['latitude' => -90, 'longitude' => -180],
                'postalAddress' => [
                    'addressCountry' => 'address_country',
                    'addressLocality' => 'address_locality',
                    'addressRegion' => 'address_region',
                    'extendedAddress' => 'extended_address',
                    'firstName' => 'first_name',
                    'lastName' => 'last_name',
                    'phoneNumber' => 'phone_number',
                    'postalCode' => 'postal_code',
                    'streetAddress' => 'street_address',
                ],
            ],
            dropoffTime: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
            nonce: 'nonce',
            pickupLocation: [
                'coordinates' => ['latitude' => -90, 'longitude' => -180],
                'postalAddress' => [
                    'addressCountry' => 'address_country',
                    'addressLocality' => 'address_locality',
                    'addressRegion' => 'address_region',
                    'extendedAddress' => 'extended_address',
                    'firstName' => 'first_name',
                    'lastName' => 'last_name',
                    'phoneNumber' => 'phone_number',
                    'postalCode' => 'postal_code',
                    'streetAddress' => 'street_address',
                ],
            ],
            pickupTime: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
            dropoffInstructions: 'dropoff_instructions',
            pickupInstructions: 'pickup_instructions',
        );

        // @phpstan-ignore-next-line method.alreadyNarrowedType
        $this->assertInstanceOf(DeliveryRequest::class, $result);
    }

    #[Test]
    public function testRetrieve(): void
    {
        if (UnsupportedMockTests::$skip) {
            $this->markTestSkipped('Prism tests are disabled');
        }

        $result = $this->client->requests->retrieve('request_id');

        // @phpstan-ignore-next-line method.alreadyNarrowedType
        $this->assertInstanceOf(DeliveryRequest::class, $result);
    }

    #[Test]
    public function testList(): void
    {
        if (UnsupportedMockTests::$skip) {
            $this->markTestSkipped('Prism tests are disabled');
        }

        $result = $this->client->requests->list();

        // @phpstan-ignore-next-line method.alreadyNarrowedType
        $this->assertIsList($result);
    }
}
