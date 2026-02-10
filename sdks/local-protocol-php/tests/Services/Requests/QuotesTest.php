<?php

namespace Tests\Services\Requests;

use LocalProtocol\Client;
use LocalProtocol\Core\Util;
use LocalProtocol\Requests\Quotes\DeliveryQuote;
use PHPUnit\Framework\Attributes\CoversNothing;
use PHPUnit\Framework\Attributes\Test;
use PHPUnit\Framework\TestCase;
use Tests\UnsupportedMockTests;

/**
 * @internal
 */
#[CoversNothing]
final class QuotesTest extends TestCase
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

        $result = $this->client->requests->quotes->create(
            'request_id',
            id: 'id',
            currency: 'SEW',
            dropoffEstimate: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
            dropoffLocation: [],
            nonce: 'nonce',
            payment: [],
            pickupEstimate: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
            pickupLocation: [],
            price: 0,
        );

        // @phpstan-ignore-next-line method.alreadyNarrowedType
        $this->assertInstanceOf(DeliveryQuote::class, $result);
    }

    #[Test]
    public function testCreateWithOptionalParams(): void
    {
        if (UnsupportedMockTests::$skip) {
            $this->markTestSkipped('Prism tests are disabled');
        }

        $result = $this->client->requests->quotes->create(
            'request_id',
            id: 'id',
            currency: 'SEW',
            dropoffEstimate: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
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
            nonce: 'nonce',
            payment: [
                'instruments' => [
                    [
                        'id' => 'id',
                        'handlerID' => 'handler_id',
                        'type' => 'type',
                        'billingAddress' => [
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
                        'credential' => ['type' => 'type'],
                        'display' => ['foo' => 'bar'],
                        'selected' => true,
                    ],
                ],
            ],
            pickupEstimate: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
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
            price: 0,
            expiresAt: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
        );

        // @phpstan-ignore-next-line method.alreadyNarrowedType
        $this->assertInstanceOf(DeliveryQuote::class, $result);
    }

    #[Test]
    public function testRetrieve(): void
    {
        if (UnsupportedMockTests::$skip) {
            $this->markTestSkipped('Prism tests are disabled');
        }

        $result = $this->client->requests->quotes->retrieve(
            'quote_id',
            requestID: 'request_id'
        );

        // @phpstan-ignore-next-line method.alreadyNarrowedType
        $this->assertInstanceOf(DeliveryQuote::class, $result);
    }

    #[Test]
    public function testRetrieveWithOptionalParams(): void
    {
        if (UnsupportedMockTests::$skip) {
            $this->markTestSkipped('Prism tests are disabled');
        }

        $result = $this->client->requests->quotes->retrieve(
            'quote_id',
            requestID: 'request_id'
        );

        // @phpstan-ignore-next-line method.alreadyNarrowedType
        $this->assertInstanceOf(DeliveryQuote::class, $result);
    }

    #[Test]
    public function testList(): void
    {
        if (UnsupportedMockTests::$skip) {
            $this->markTestSkipped('Prism tests are disabled');
        }

        $result = $this->client->requests->quotes->list('request_id');

        // @phpstan-ignore-next-line method.alreadyNarrowedType
        $this->assertIsList($result);
    }
}
