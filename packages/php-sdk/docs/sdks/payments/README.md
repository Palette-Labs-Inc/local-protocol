# Payments

## Overview

Payment instrument operations

### Available Operations

* [createPaymentInstrument](#createpaymentinstrument) - Register payment instrument

## createPaymentInstrument

Register a payment instrument for use in order creation.

### Example Usage

<!-- UsageSnippet language="php" operationID="createPaymentInstrument" method="post" path="/payment-instruments" -->
```php
declare(strict_types=1);

require 'vendor/autoload.php';

use LocalProtocol;
use LocalProtocol\Models\Components;
use LocalProtocol\Utils;

$sdk = LocalProtocol\LocalProtocol::builder()->build();

$request = new Components\EvmAuthCaptureEscrowInstrument(
    id: '<id>',
    handlerId: '<id>',
    paymentInfoHash: '<value>',
    operator: '<value>',
    payer: '<value>',
    chainId: 933627,
    contract: '<value>',
    receiver: '<value>',
    token: new Components\EvmToken(
        symbol: '<value>',
        decimals: 599585,
    ),
    maxAmount: new Components\MaxAmount(
        value: '<value>',
        currency: new Components\EvmCurrency(
            chainId: 534500,
            address: '6814 Ziemann Field',
            decimals: 609251,
        ),
    ),
    preapprovalExpiresAt: Utils\Utils::parseDateTime('2024-07-26T23:36:42.374Z'),
    authorizationExpiresAt: Utils\Utils::parseDateTime('2024-10-07T03:34:24.771Z'),
    refundExpiresAt: Utils\Utils::parseDateTime('2024-05-30T02:15:26.285Z'),
    nonce: '<value>',
    amount: new Components\EvmAuthCaptureEscrowInstrumentAmount(
        value: '<value>',
        currency: new Components\EvmCurrency(
            chainId: 534500,
            address: '6814 Ziemann Field',
            decimals: 609251,
        ),
    ),
);

$response = $sdk->payments->createPaymentInstrument(
    request: $request
);

if ($response->evmAuthCaptureEscrowInstrument !== null) {
    // handle response
}
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `$request`                                                                                             | [Components\EvmAuthCaptureEscrowInstrument](../../Models/Components/EvmAuthCaptureEscrowInstrument.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |

### Response

**[?Operations\CreatePaymentInstrumentResponse](../../Models/Operations/CreatePaymentInstrumentResponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| Errors\ErrorResponse           | 400                            | application/json               |
| Errors\ValidationErrorResponse | 422                            | application/json               |
| Errors\APIException            | 4XX, 5XX                       | \*/\*                          |