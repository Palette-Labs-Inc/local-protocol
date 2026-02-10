<?php

namespace Tests\Services;

use LocalProtocol\Client;
use LocalProtocol\Core\Util;
use LocalProtocol\Deliveries\Delivery;
use PHPUnit\Framework\Attributes\CoversNothing;
use PHPUnit\Framework\Attributes\Test;
use PHPUnit\Framework\TestCase;

/**
 * @internal
 */
#[CoversNothing]
final class DeliveriesTest extends TestCase
{
    protected Client $client;

    protected function setUp(): void
    {
        parent::setUp();

        $testUrl = Util::getenv('TEST_API_BASE_URL') ?: 'http://127.0.0.1:4010';
        $client = new Client(apiKey: 'My API Key', baseUrl: $testUrl);

        $this->client = $client;
    }

    #[Test]
    public function testCreate(): void
    {
        $result = $this->client->deliveries->create(
            nonce: 'nonce',
            quoteID: 'quote_id',
            requestID: 'request_id'
        );

        // @phpstan-ignore-next-line method.alreadyNarrowedType
        $this->assertInstanceOf(Delivery::class, $result);
    }

    #[Test]
    public function testCreateWithOptionalParams(): void
    {
        $result = $this->client->deliveries->create(
            nonce: 'nonce',
            quoteID: 'quote_id',
            requestID: 'request_id',
            eventVocabulary: 'event_vocabulary',
            webhookURL: 'webhook_url',
        );

        // @phpstan-ignore-next-line method.alreadyNarrowedType
        $this->assertInstanceOf(Delivery::class, $result);
    }

    #[Test]
    public function testRetrieve(): void
    {
        $result = $this->client->deliveries->retrieve('delivery_id');

        // @phpstan-ignore-next-line method.alreadyNarrowedType
        $this->assertInstanceOf(Delivery::class, $result);
    }

    #[Test]
    public function testList(): void
    {
        $result = $this->client->deliveries->list();

        // @phpstan-ignore-next-line method.alreadyNarrowedType
        $this->assertIsList($result);
    }

    #[Test]
    public function testUpdateEvent(): void
    {
        $result = $this->client->deliveries->updateEvent(
            'delivery_id',
            event: 'event',
            eventDescription: 'event_description'
        );

        // @phpstan-ignore-next-line method.alreadyNarrowedType
        $this->assertInstanceOf(Delivery::class, $result);
    }

    #[Test]
    public function testUpdateEventWithOptionalParams(): void
    {
        $result = $this->client->deliveries->updateEvent(
            'delivery_id',
            event: 'event',
            eventDescription: 'event_description'
        );

        // @phpstan-ignore-next-line method.alreadyNarrowedType
        $this->assertInstanceOf(Delivery::class, $result);
    }
}
