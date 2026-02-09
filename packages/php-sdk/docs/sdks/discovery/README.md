# Discovery

## Overview

Service discovery and health

### Available Operations

* [get](#get) - Service discovery
* [getHealth](#gethealth) - Health check

## get

Returns server capabilities, supported standards, and endpoint paths.

### Example Usage

<!-- UsageSnippet language="php" operationID="getDiscovery" method="get" path="/.well-known/local-protocol" -->
```php
declare(strict_types=1);

require 'vendor/autoload.php';

use LocalProtocol;

$sdk = LocalProtocol\LocalProtocol::builder()->build();



$response = $sdk->discovery->get(

);

if ($response->discoveryResponse !== null) {
    // handle response
}
```

### Response

**[?Operations\GetDiscoveryResponse](../../Models/Operations/GetDiscoveryResponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| Errors\ErrorResponse | 500                  | application/json     |
| Errors\APIException  | 4XX, 5XX             | \*/\*                |

## getHealth

Returns server health status.

### Example Usage

<!-- UsageSnippet language="php" operationID="getHealth" method="get" path="/healthz" -->
```php
declare(strict_types=1);

require 'vendor/autoload.php';

use LocalProtocol;

$sdk = LocalProtocol\LocalProtocol::builder()->build();



$response = $sdk->discovery->getHealth(

);

if ($response->healthResponse !== null) {
    // handle response
}
```

### Response

**[?Operations\GetHealthResponse](../../Models/Operations/GetHealthResponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| Errors\ErrorResponse | 503                  | application/json     |
| Errors\APIException  | 4XX, 5XX             | \*/\*                |