<?php

namespace Tests\Services;

use LocalProtocol\Client;
use LocalProtocol\Core\Util;
use LocalProtocol\PaymentInstruments\EvmAuthCaptureEscrowInstrument;
use PHPUnit\Framework\Attributes\CoversNothing;
use PHPUnit\Framework\Attributes\Test;
use PHPUnit\Framework\TestCase;
use Tests\UnsupportedMockTests;

/**
 * @internal
 */
#[CoversNothing]
final class PaymentInstrumentsTest extends TestCase
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
    public function testRegister(): void
    {
        if (UnsupportedMockTests::$skip) {
            $this->markTestSkipped('Prism tests are disabled');
        }

        $result = $this->client->paymentInstruments->register(
            id: 'id',
            token: ['decimals' => 0, 'symbol' => 'symbol'],
            amount: [
                'currency' => [
                    'address' => '0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A',
                    'chainID' => 1,
                    'decimals' => 0,
                ],
                'value' => '269125115713',
            ],
            authorizationExpiresAt: new \DateTimeImmutable(
                '2019-12-27T18:11:19.117Z'
            ),
            chainID: 1,
            contract: '0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A',
            handlerID: 'handler_id',
            maxAmount: [
                'currency' => [
                    'address' => '0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A',
                    'chainID' => 1,
                    'decimals' => 0,
                ],
                'value' => '269125115713',
            ],
            nonce: '269125115713',
            operator: '0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A',
            payer: '0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A',
            paymentInfoHash: '0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8ACa3CC53eb6CEAA2eaa0Aa6be',
            preapprovalExpiresAt: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
            receiver: '0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A',
            refundExpiresAt: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
        );

        // @phpstan-ignore-next-line method.alreadyNarrowedType
        $this->assertInstanceOf(EvmAuthCaptureEscrowInstrument::class, $result);
    }

    #[Test]
    public function testRegisterWithOptionalParams(): void
    {
        if (UnsupportedMockTests::$skip) {
            $this->markTestSkipped('Prism tests are disabled');
        }

        $result = $this->client->paymentInstruments->register(
            id: 'id',
            token: [
                'decimals' => 0,
                'symbol' => 'symbol',
                'address' => '0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A',
            ],
            amount: [
                'currency' => [
                    'address' => '0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A',
                    'chainID' => 1,
                    'decimals' => 0,
                ],
                'value' => '269125115713',
            ],
            authorizationExpiresAt: new \DateTimeImmutable(
                '2019-12-27T18:11:19.117Z'
            ),
            chainID: 1,
            contract: '0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A',
            handlerID: 'handler_id',
            maxAmount: [
                'currency' => [
                    'address' => '0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A',
                    'chainID' => 1,
                    'decimals' => 0,
                ],
                'value' => '269125115713',
            ],
            nonce: '269125115713',
            operator: '0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A',
            payer: '0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A',
            paymentInfoHash: '0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8ACa3CC53eb6CEAA2eaa0Aa6be',
            preapprovalExpiresAt: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
            receiver: '0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A',
            refundExpiresAt: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
            type: 'evm_auth_capture_escrow',
            billingAddress: [
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
            credential: ['type' => 'type'],
            display: ['foo' => 'bar'],
        );

        // @phpstan-ignore-next-line method.alreadyNarrowedType
        $this->assertInstanceOf(EvmAuthCaptureEscrowInstrument::class, $result);
    }
}
