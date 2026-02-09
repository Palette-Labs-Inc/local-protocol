# Quotes

## Overview

Delivery quote operations

### Available Operations

* [create](#create) - Create quote
* [list](#list) - List quotes for request
* [get](#get) - Get quote

## create

Submit a quote for a delivery request. The `nonce` field provides idempotency.

### Example Usage

<!-- UsageSnippet language="php" operationID="createQuote" method="post" path="/requests/{request_id}/quotes" -->
```php
declare(strict_types=1);

require 'vendor/autoload.php';

use LocalProtocol;
use LocalProtocol\Models\Components;
use LocalProtocol\Utils;

$sdk = LocalProtocol\LocalProtocol::builder()->build();

$body = new Components\DeliveryQuote(
    id: '<id>',
    nonce: '<value>',
    price: 887209,
    currency: 'Bhutanese Ngultrum',
    pickupLocation: new Components\Location1(
        coordinates: new Components\Coordinates(
            latitude: 2026.17,
            longitude: 9956.78,
        ),
    ),
    dropoffLocation: new Components\Location1(
        coordinates: new Components\Coordinates(
            latitude: 2026.17,
            longitude: 9956.78,
        ),
    ),
    pickupEstimate: Utils\Utils::parseDateTime('2026-02-24T12:34:27.941Z'),
    dropoffEstimate: Utils\Utils::parseDateTime('2024-10-17T15:58:14.067Z'),
    payment: new Components\Payment(),
);

$response = $sdk->quotes->create(
    requestId: '<id>',
    body: $body

);

if ($response->deliveryQuote !== null) {
    // handle response
}
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `requestId`                                                          | *string*                                                             | :heavy_check_mark:                                                   | Delivery request identifier.                                         |
| `body`                                                               | [Components\DeliveryQuote](../../Models/Components/DeliveryQuote.md) | :heavy_check_mark:                                                   | N/A                                                                  |

### Response

**[?Operations\CreateQuoteResponse](../../Models/Operations/CreateQuoteResponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| Errors\ErrorResponse           | 400, 404, 409                  | application/json               |
| Errors\ValidationErrorResponse | 422                            | application/json               |
| Errors\APIException            | 4XX, 5XX                       | \*/\*                          |

## list

Returns all quotes for a delivery request.

### Example Usage

<!-- UsageSnippet language="php" operationID="listQuotes" method="get" path="/requests/{request_id}/quotes" -->
```php
declare(strict_types=1);

require 'vendor/autoload.php';

use LocalProtocol;

$sdk = LocalProtocol\LocalProtocol::builder()->build();



$response = $sdk->quotes->list(
    requestId: '<id>'
);

if ($response->deliveryQuotes !== null) {
    // handle response
}
```

### Parameters

| Parameter                    | Type                         | Required                     | Description                  |
| ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- |
| `requestId`                  | *string*                     | :heavy_check_mark:           | Delivery request identifier. |

### Response

**[?Operations\ListQuotesResponse](../../Models/Operations/ListQuotesResponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| Errors\ErrorResponse | 404                  | application/json     |
| Errors\APIException  | 4XX, 5XX             | \*/\*                |

## get

Returns a single quote by ID.

### Example Usage

<!-- UsageSnippet language="php" operationID="getQuote" method="get" path="/requests/{request_id}/quotes/{quote_id}" -->
```php
declare(strict_types=1);

require 'vendor/autoload.php';

use LocalProtocol;

$sdk = LocalProtocol\LocalProtocol::builder()->build();



$response = $sdk->quotes->get(
    requestId: '<id>',
    quoteId: '<id>'

);

if ($response->deliveryQuote !== null) {
    // handle response
}
```

### Parameters

| Parameter                    | Type                         | Required                     | Description                  |
| ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- |
| `requestId`                  | *string*                     | :heavy_check_mark:           | Delivery request identifier. |
| `quoteId`                    | *string*                     | :heavy_check_mark:           | Quote identifier.            |

### Response

**[?Operations\GetQuoteResponse](../../Models/Operations/GetQuoteResponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| Errors\ErrorResponse | 404                  | application/json     |
| Errors\APIException  | 4XX, 5XX             | \*/\*                |