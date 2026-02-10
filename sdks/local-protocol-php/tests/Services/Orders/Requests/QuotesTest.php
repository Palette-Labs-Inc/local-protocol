<?php

namespace Tests\Services\Orders\Requests;

use LocalProtocol\Client;
use LocalProtocol\Core\Util;
use LocalProtocol\Orders\Requests\Quotes\OrderQuote;
use PHPUnit\Framework\Attributes\CoversNothing;
use PHPUnit\Framework\Attributes\Test;
use PHPUnit\Framework\TestCase;

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
        $client = new Client(apiKey: 'My API Key', baseUrl: $testUrl);

        $this->client = $client;
    }

    #[Test]
    public function testRetrieve(): void
    {
        $result = $this->client->orders->requests->quotes->retrieve(
            'order_quote_id',
            orderRequestID: 'order_request_id'
        );

        // @phpstan-ignore-next-line method.alreadyNarrowedType
        $this->assertInstanceOf(OrderQuote::class, $result);
    }

    #[Test]
    public function testRetrieveWithOptionalParams(): void
    {
        $result = $this->client->orders->requests->quotes->retrieve(
            'order_quote_id',
            orderRequestID: 'order_request_id'
        );

        // @phpstan-ignore-next-line method.alreadyNarrowedType
        $this->assertInstanceOf(OrderQuote::class, $result);
    }

    #[Test]
    public function testList(): void
    {
        $result = $this->client->orders->requests->quotes->list('order_request_id');

        // @phpstan-ignore-next-line method.alreadyNarrowedType
        $this->assertIsList($result);
    }
}
