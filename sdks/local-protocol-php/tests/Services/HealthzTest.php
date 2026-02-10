<?php

namespace Tests\Services;

use LocalProtocol\Client;
use LocalProtocol\Core\Util;
use LocalProtocol\Healthz\HealthzCheckResponse;
use PHPUnit\Framework\Attributes\CoversNothing;
use PHPUnit\Framework\Attributes\Test;
use PHPUnit\Framework\TestCase;
use Tests\UnsupportedMockTests;

/**
 * @internal
 */
#[CoversNothing]
final class HealthzTest extends TestCase
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
    public function testCheck(): void
    {
        if (UnsupportedMockTests::$skip) {
            $this->markTestSkipped('Prism tests are disabled');
        }

        $result = $this->client->healthz->check();

        // @phpstan-ignore-next-line method.alreadyNarrowedType
        $this->assertInstanceOf(HealthzCheckResponse::class, $result);
    }
}
