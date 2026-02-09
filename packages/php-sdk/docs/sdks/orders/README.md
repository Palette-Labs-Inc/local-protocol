# Orders

## Overview

Order lifecycle operations

### Available Operations

* [createOrderRequest](#createorderrequest) - Create order request
* [listOrderQuotes](#listorderquotes) - List order quotes
* [getOrderQuote](#getorderquote) - Get order quote
* [createOrder](#createorder) - Create order
* [getOrder](#getorder) - Get order

## createOrderRequest

Submit a new order request with a cart. The `nonce` field provides idempotency.

### Example Usage

<!-- UsageSnippet language="php" operationID="createOrderRequest" method="post" path="/orders/requests" -->
```php
declare(strict_types=1);

require 'vendor/autoload.php';

use LocalProtocol;
use LocalProtocol\Models\Components;

$sdk = LocalProtocol\LocalProtocol::builder()->build();

$request = new Components\Cart(
    id: '<id>',
    intentId: '<id>',
    nonce: '<value>',
    items: [
        new Components\CartItem(
            id: '<id>',
            quantity: 755842,
        ),
    ],
);

$response = $sdk->orders->createOrderRequest(
    request: $request
);

if ($response->orderRequest !== null) {
    // handle response
}
```

### Parameters

| Parameter                                          | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `$request`                                         | [Components\Cart](../../Models/Components/Cart.md) | :heavy_check_mark:                                 | The request object to use for the request.         |

### Response

**[?Operations\CreateOrderRequestResponse](../../Models/Operations/CreateOrderRequestResponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| Errors\ErrorResponse           | 400, 409                       | application/json               |
| Errors\ValidationErrorResponse | 422                            | application/json               |
| Errors\APIException            | 4XX, 5XX                       | \*/\*                          |

## listOrderQuotes

Returns all quotes for an order request.

### Example Usage

<!-- UsageSnippet language="php" operationID="listOrderQuotes" method="get" path="/orders/requests/{order_request_id}/quotes" -->
```php
declare(strict_types=1);

require 'vendor/autoload.php';

use LocalProtocol;

$sdk = LocalProtocol\LocalProtocol::builder()->build();



$response = $sdk->orders->listOrderQuotes(
    orderRequestId: '<id>'
);

if ($response->orderQuotes !== null) {
    // handle response
}
```

### Parameters

| Parameter                 | Type                      | Required                  | Description               |
| ------------------------- | ------------------------- | ------------------------- | ------------------------- |
| `orderRequestId`          | *string*                  | :heavy_check_mark:        | Order request identifier. |

### Response

**[?Operations\ListOrderQuotesResponse](../../Models/Operations/ListOrderQuotesResponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| Errors\ErrorResponse | 404                  | application/json     |
| Errors\APIException  | 4XX, 5XX             | \*/\*                |

## getOrderQuote

Returns a single order quote by ID.

### Example Usage

<!-- UsageSnippet language="php" operationID="getOrderQuote" method="get" path="/orders/requests/{order_request_id}/quotes/{order_quote_id}" -->
```php
declare(strict_types=1);

require 'vendor/autoload.php';

use LocalProtocol;

$sdk = LocalProtocol\LocalProtocol::builder()->build();



$response = $sdk->orders->getOrderQuote(
    orderRequestId: '<id>',
    orderQuoteId: '<id>'

);

if ($response->orderQuote !== null) {
    // handle response
}
```

### Parameters

| Parameter                 | Type                      | Required                  | Description               |
| ------------------------- | ------------------------- | ------------------------- | ------------------------- |
| `orderRequestId`          | *string*                  | :heavy_check_mark:        | Order request identifier. |
| `orderQuoteId`            | *string*                  | :heavy_check_mark:        | Order quote identifier.   |

### Response

**[?Operations\GetOrderQuoteResponse](../../Models/Operations/GetOrderQuoteResponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| Errors\ErrorResponse | 404                  | application/json     |
| Errors\APIException  | 4XX, 5XX             | \*/\*                |

## createOrder

Accept a quote and create an order. The `nonce` field provides idempotency.

### Example Usage

<!-- UsageSnippet language="php" operationID="createOrder" method="post" path="/orders" -->
```php
declare(strict_types=1);

require 'vendor/autoload.php';

use LocalProtocol;
use LocalProtocol\Models\Components;

$sdk = LocalProtocol\LocalProtocol::builder()->build();

$request = new Components\CreateOrderRequest(
    orderRequestId: '<id>',
    orderQuoteId: '<id>',
    nonce: '<value>',
    paymentInstrumentId: '<id>',
);

$response = $sdk->orders->createOrder(
    request: $request
);

if ($response->order !== null) {
    // handle response
}
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `$request`                                                                     | [Components\CreateOrderRequest](../../Models/Components/CreateOrderRequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |

### Response

**[?Operations\CreateOrderResponse](../../Models/Operations/CreateOrderResponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| Errors\ErrorResponse | 400, 404, 409        | application/json     |
| Errors\APIException  | 4XX, 5XX             | \*/\*                |

## getOrder

Returns a single order by ID.

### Example Usage

<!-- UsageSnippet language="php" operationID="getOrder" method="get" path="/orders/{order_id}" -->
```php
declare(strict_types=1);

require 'vendor/autoload.php';

use LocalProtocol;

$sdk = LocalProtocol\LocalProtocol::builder()->build();



$response = $sdk->orders->getOrder(
    orderId: '<id>'
);

if ($response->order !== null) {
    // handle response
}
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `orderId`          | *string*           | :heavy_check_mark: | Order identifier.  |

### Response

**[?Operations\GetOrderResponse](../../Models/Operations/GetOrderResponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| Errors\ErrorResponse | 404                  | application/json     |
| Errors\APIException  | 4XX, 5XX             | \*/\*                |