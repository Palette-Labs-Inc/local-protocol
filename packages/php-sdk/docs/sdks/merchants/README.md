# Merchants

## Overview

Merchant and catalog operations

### Available Operations

* [getMerchant](#getmerchant) - Get merchant

## getMerchant

Returns a merchant with its full denormalized catalog tree.

### Example Usage

<!-- UsageSnippet language="php" operationID="getMerchant" method="get" path="/merchants/{merchant_id}" -->
```php
declare(strict_types=1);

require 'vendor/autoload.php';

use LocalProtocol;

$sdk = LocalProtocol\LocalProtocol::builder()->build();



$response = $sdk->merchants->getMerchant(
    merchantId: '<id>'
);

if ($response->merchant !== null) {
    // handle response
}
```

### Parameters

| Parameter            | Type                 | Required             | Description          |
| -------------------- | -------------------- | -------------------- | -------------------- |
| `merchantId`         | *string*             | :heavy_check_mark:   | Merchant identifier. |

### Response

**[?Operations\GetMerchantResponse](../../Models/Operations/GetMerchantResponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| Errors\ErrorResponse | 404                  | application/json     |
| Errors\APIException  | 4XX, 5XX             | \*/\*                |