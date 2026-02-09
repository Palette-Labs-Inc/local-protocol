# Events

## Overview

Event vocabulary operations

### Available Operations

* [getEventVocabulary](#geteventvocabulary) - Get event vocabulary

## getEventVocabulary

Returns a delivery event vocabulary by name.

### Example Usage

<!-- UsageSnippet language="php" operationID="getEventVocabulary" method="get" path="/event-vocabularies/{name}" -->
```php
declare(strict_types=1);

require 'vendor/autoload.php';

use LocalProtocol;

$sdk = LocalProtocol\LocalProtocol::builder()->build();



$response = $sdk->events->getEventVocabulary(
    name: '<value>'
);

if ($response->deliveryEventVocabulary !== null) {
    // handle response
}
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `name`                                                                                       | *string*                                                                                     | :heavy_check_mark:                                                                           | Event vocabulary name in reverse-domain notation (e.g., xyz.localprotocol.delivery.courier). |

### Response

**[?Operations\GetEventVocabularyResponse](../../Models/Operations/GetEventVocabularyResponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| Errors\ErrorResponse | 404                  | application/json     |
| Errors\APIException  | 4XX, 5XX             | \*/\*                |