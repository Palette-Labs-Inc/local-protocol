<?php

namespace Tests\Services\Orders;

use LocalProtocol\Client;
use LocalProtocol\Core\Util;
use LocalProtocol\Orders\Requests\RequestNewResponse;
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

        $result = $this->client->orders->requests->create(
            id: 'id',
            intentID: 'intent_id',
            items: [['id' => 'id', 'quantity' => 1]],
            nonce: 'nonce',
        );

        // @phpstan-ignore-next-line method.alreadyNarrowedType
        $this->assertInstanceOf(RequestNewResponse::class, $result);
    }

    #[Test]
    public function testCreateWithOptionalParams(): void
    {
        if (UnsupportedMockTests::$skip) {
            $this->markTestSkipped('Prism tests are disabled');
        }

        $result = $this->client->orders->requests->create(
            id: 'id',
            intentID: 'intent_id',
            items: [['id' => 'id', 'quantity' => 1]],
            nonce: 'nonce',
        );

        // @phpstan-ignore-next-line method.alreadyNarrowedType
        $this->assertInstanceOf(RequestNewResponse::class, $result);
    }
}
