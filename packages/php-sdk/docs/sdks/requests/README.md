# Requests

## Overview

Delivery request operations

### Available Operations

* [create](#create) - Create delivery request
* [list](#list) - List delivery requests
* [get](#get) - Get delivery request

## create

Submit a new delivery request. The `nonce` field provides idempotency.

### Example Usage

<!-- UsageSnippet language="php" operationID="createRequest" method="post" path="/requests" -->
```php
declare(strict_types=1);

require 'vendor/autoload.php';

use LocalProtocol;
use LocalProtocol\Models\Components;
use LocalProtocol\Utils;

$sdk = LocalProtocol\LocalProtocol::builder()->build();

$request = new Components\DeliveryRequestCreate(
    id: '<id>',
    nonce: '<value>',
    pickupLocation: new Components\Location1(
        coordinates: new Components\Coordinates(
            latitude: 9821.48,
            longitude: 3629.78,
        ),
    ),
    dropoffLocation: new Components\Location2(
        postalAddress: new Components\PostalAddress(),
    ),
    pickupTime: Utils\Utils::parseDateTime('2026-06-22T12:35:13.217Z'),
    dropoffTime: Utils\Utils::parseDateTime('2026-02-21T01:14:18.597Z'),
);

$response = $sdk->requests->create(
    request: $request
);

if ($response->deliveryRequest !== null) {
    // handle response
}
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `$request`                                                                           | [Components\DeliveryRequestCreate](../../Models/Components/DeliveryRequestCreate.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |

### Response

**[?Operations\CreateRequestResponse](../../Models/Operations/CreateRequestResponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| Errors\ErrorResponse           | 400, 409                       | application/json               |
| Errors\ValidationErrorResponse | 422                            | application/json               |
| Errors\APIException            | 4XX, 5XX                       | \*/\*                          |

## list

Returns all delivery requests.

### Example Usage

<!-- UsageSnippet language="php" operationID="listRequests" method="get" path="/requests" -->
```php
declare(strict_types=1);

require 'vendor/autoload.php';

use LocalProtocol;

$sdk = LocalProtocol\LocalProtocol::builder()->build();



$response = $sdk->requests->list(

);

if ($response->deliveryRequests !== null) {
    // handle response
}
```

### Response

**[?Operations\ListRequestsResponse](../../Models/Operations/ListRequestsResponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| Errors\ErrorResponse | 500                  | application/json     |
| Errors\APIException  | 4XX, 5XX             | \*/\*                |

## get

Returns a single delivery request by ID.

### Example Usage

<!-- UsageSnippet language="php" operationID="getRequest" method="get" path="/requests/{request_id}" -->
```php
declare(strict_types=1);

require 'vendor/autoload.php';

use LocalProtocol;

$sdk = LocalProtocol\LocalProtocol::builder()->build();



$response = $sdk->requests->get(
    requestId: '<id>'
);

if ($response->deliveryRequest !== null) {
    // handle response
}
```

### Parameters

| Parameter                    | Type                         | Required                     | Description                  |
| ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- |
| `requestId`                  | *string*                     | :heavy_check_mark:           | Delivery request identifier. |

### Response

**[?Operations\GetRequestResponse](../../Models/Operations/GetRequestResponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| Errors\ErrorResponse | 404                  | application/json     |
| Errors\APIException  | 4XX, 5XX             | \*/\*                |