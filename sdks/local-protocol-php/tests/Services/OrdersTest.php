<?php

namespace Tests\Services;

use LocalProtocol\Client;
use LocalProtocol\Core\Util;
use LocalProtocol\Orders\Order;
use PHPUnit\Framework\Attributes\CoversNothing;
use PHPUnit\Framework\Attributes\Test;
use PHPUnit\Framework\TestCase;

/**
 * @internal
 */
#[CoversNothing]
final class OrdersTest extends TestCase
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
        $result = $this->client->orders->create(
            nonce: 'nonce',
            orderQuoteID: 'order_quote_id',
            orderRequestID: 'order_request_id',
            paymentInstrumentID: 'payment_instrument_id',
        );

        // @phpstan-ignore-next-line method.alreadyNarrowedType
        $this->assertInstanceOf(Order::class, $result);
    }

    #[Test]
    public function testCreateWithOptionalParams(): void
    {
        $result = $this->client->orders->create(
            nonce: 'nonce',
            orderQuoteID: 'order_quote_id',
            orderRequestID: 'order_request_id',
            paymentInstrumentID: 'payment_instrument_id',
        );

        // @phpstan-ignore-next-line method.alreadyNarrowedType
        $this->assertInstanceOf(Order::class, $result);
    }

    #[Test]
    public function testRetrieve(): void
    {
        $result = $this->client->orders->retrieve('order_id');

        // @phpstan-ignore-next-line method.alreadyNarrowedType
        $this->assertInstanceOf(Order::class, $result);
    }
}
