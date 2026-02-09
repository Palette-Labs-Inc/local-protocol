# Deliveries

## Overview

Delivery lifecycle operations

### Available Operations

* [create](#create) - Create delivery
* [list](#list) - List deliveries
* [get](#get) - Get delivery
* [updateEvent](#updateevent) - Update delivery event

## create

Accept a quote and create a delivery. The `nonce` field provides idempotency.

### Example Usage

<!-- UsageSnippet language="php" operationID="createDelivery" method="post" path="/deliveries" -->
```php
declare(strict_types=1);

require 'vendor/autoload.php';

use LocalProtocol;
use LocalProtocol\Models\Components;

$sdk = LocalProtocol\LocalProtocol::builder()->build();

$request = new Components\CreateDeliveryRequest(
    requestId: '<id>',
    quoteId: '<id>',
    nonce: '<value>',
);

$response = $sdk->deliveries->create(
    request: $request
);

if ($response->delivery !== null) {
    // handle response
}
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `$request`                                                                           | [Components\CreateDeliveryRequest](../../Models/Components/CreateDeliveryRequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |

### Response

**[?Operations\CreateDeliveryResponse](../../Models/Operations/CreateDeliveryResponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| Errors\ErrorResponse | 400, 404, 409        | application/json     |
| Errors\APIException  | 4XX, 5XX             | \*/\*                |

## list

Returns all deliveries.

### Example Usage

<!-- UsageSnippet language="php" operationID="listDeliveries" method="get" path="/deliveries" -->
```php
declare(strict_types=1);

require 'vendor/autoload.php';

use LocalProtocol;

$sdk = LocalProtocol\LocalProtocol::builder()->build();



$response = $sdk->deliveries->list(

);

if ($response->deliveries !== null) {
    // handle response
}
```

### Response

**[?Operations\ListDeliveriesResponse](../../Models/Operations/ListDeliveriesResponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| Errors\ErrorResponse | 500                  | application/json     |
| Errors\APIException  | 4XX, 5XX             | \*/\*                |

## get

Returns a single delivery by ID.

### Example Usage

<!-- UsageSnippet language="php" operationID="getDelivery" method="get" path="/deliveries/{delivery_id}" -->
```php
declare(strict_types=1);

require 'vendor/autoload.php';

use LocalProtocol;

$sdk = LocalProtocol\LocalProtocol::builder()->build();



$response = $sdk->deliveries->get(
    deliveryId: '<id>'
);

if ($response->delivery !== null) {
    // handle response
}
```

### Parameters

| Parameter            | Type                 | Required             | Description          |
| -------------------- | -------------------- | -------------------- | -------------------- |
| `deliveryId`         | *string*             | :heavy_check_mark:   | Delivery identifier. |

### Response

**[?Operations\GetDeliveryResponse](../../Models/Operations/GetDeliveryResponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| Errors\ErrorResponse | 404                  | application/json     |
| Errors\APIException  | 4XX, 5XX             | \*/\*                |

## updateEvent

Transition a delivery to a new event state. If a webhook URL was registered, the server pushes an event notification in the background.

### Example Usage

<!-- UsageSnippet language="php" operationID="updateDeliveryEvent" method="patch" path="/deliveries/{delivery_id}/event" -->
```php
declare(strict_types=1);

require 'vendor/autoload.php';

use LocalProtocol;
use LocalProtocol\Models\Components;

$sdk = LocalProtocol\LocalProtocol::builder()->build();

$body = new Components\UpdateEventRequest(
    event: '<value>',
    eventDescription: '<value>',
);

$response = $sdk->deliveries->updateEvent(
    deliveryId: '<id>',
    body: $body

);

if ($response->delivery !== null) {
    // handle response
}
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `deliveryId`                                                                   | *string*                                                                       | :heavy_check_mark:                                                             | Delivery identifier.                                                           |
| `body`                                                                         | [Components\UpdateEventRequest](../../Models/Components/UpdateEventRequest.md) | :heavy_check_mark:                                                             | N/A                                                                            |

### Response

**[?Operations\UpdateDeliveryEventResponse](../../Models/Operations/UpdateDeliveryEventResponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| Errors\ErrorResponse | 404                  | application/json     |
| Errors\APIException  | 4XX, 5XX             | \*/\*                |