# localprotocol/local-protocol-sdk

Developer-friendly & type-safe Php SDK specifically catered to leverage *localprotocol/local-protocol-sdk* API.

[![Built by Speakeasy](https://img.shields.io/badge/Built_by-SPEAKEASY-374151?style=for-the-badge&labelColor=f3f4f6)](https://www.speakeasy.com/?utm_source=localprotocol/local-protocol-sdk&utm_campaign=php)
[![License: MIT](https://img.shields.io/badge/LICENSE_//_MIT-3b5bdb?style=for-the-badge&labelColor=eff6ff)](https://opensource.org/licenses/MIT)


<br /><br />
> [!IMPORTANT]
> This SDK is not yet ready for production use. To complete setup please follow the steps outlined in your [workspace](https://app.speakeasy.com/org/palette-labs/local-protocol). Delete this section before > publishing to a package manager.

<!-- Start Summary [summary] -->
## Summary

Local Protocol: Local Protocol delivery API. Covers service discovery, delivery requests, quotes, and deliveries.
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [localprotocol/local-protocol-sdk](#localprotocollocal-protocol-sdk)
  * [SDK Installation](#sdk-installation)
  * [SDK Example Usage](#sdk-example-usage)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
* [Development](#development)
  * [Maturity](#maturity)
  * [Contributions](#contributions)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!TIP]
> To finish publishing your SDK you must [run your first generation action](https://www.speakeasy.com/docs/github-setup#step-by-step-guide).


The SDK relies on [Composer](https://getcomposer.org/) to manage its dependencies.

To install the SDK first add the below to your `composer.json` file:

```json
{
    "repositories": [
        {
            "type": "github",
            "url": "<UNSET>.git"
        }
    ],
    "require": {
        "localprotocol/local-protocol-sdk": "*"
    }
}
```

Then run the following command:

```bash
composer update
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

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
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [Deliveries](docs/sdks/deliveries/README.md)

* [create](docs/sdks/deliveries/README.md#create) - Create delivery
* [list](docs/sdks/deliveries/README.md#list) - List deliveries
* [get](docs/sdks/deliveries/README.md#get) - Get delivery
* [updateEvent](docs/sdks/deliveries/README.md#updateevent) - Update delivery event

### [Discovery](docs/sdks/discovery/README.md)

* [get](docs/sdks/discovery/README.md#get) - Service discovery
* [getHealth](docs/sdks/discovery/README.md#gethealth) - Health check

### [Quotes](docs/sdks/quotes/README.md)

* [create](docs/sdks/quotes/README.md#create) - Create quote
* [list](docs/sdks/quotes/README.md#list) - List quotes for request
* [get](docs/sdks/quotes/README.md#get) - Get quote

### [Requests](docs/sdks/requests/README.md)

* [create](docs/sdks/requests/README.md#create) - Create delivery request
* [list](docs/sdks/requests/README.md#list) - List delivery requests
* [get](docs/sdks/requests/README.md#get) - Get delivery request

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations. All operations return a response object or throw an exception.

By default an API error will raise a `Errors\APIException` exception, which has the following properties:

| Property       | Type                                    | Description           |
|----------------|-----------------------------------------|-----------------------|
| `$message`     | *string*                                | The error message     |
| `$statusCode`  | *int*                                   | The HTTP status code  |
| `$rawResponse` | *?\Psr\Http\Message\ResponseInterface*  | The raw HTTP response |
| `$body`        | *string*                                | The response content  |

When custom error responses are specified for an operation, the SDK may also throw their associated exception. You can refer to respective *Errors* tables in SDK docs for more details on possible exception types for each operation. For example, the `get` method throws the following exceptions:

| Error Type           | Status Code | Content Type     |
| -------------------- | ----------- | ---------------- |
| Errors\ErrorResponse | 500         | application/json |
| Errors\APIException  | 4XX, 5XX    | \*/\*            |

### Example

```php
declare(strict_types=1);

require 'vendor/autoload.php';

use LocalProtocol;
use LocalProtocol\Models\Errors;

$sdk = LocalProtocol\LocalProtocol::builder()->build();

try {
    $response = $sdk->discovery->get(

    );

    if ($response->discoveryResponse !== null) {
        // handle response
    }
} catch (Errors\ErrorResponseThrowable $e) {
    // handle $e->$container data
    throw $e;
} catch (Errors\APIException $e) {
    // handle default exception
    throw $e;
}
```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Override Server URL Per-Client

The default server can be overridden globally using the `setServerUrl(string $serverUrl)` builder method when initializing the SDK client instance. For example:
```php
declare(strict_types=1);

require 'vendor/autoload.php';

use LocalProtocol;

$sdk = LocalProtocol\LocalProtocol::builder()
    ->setServerURL('http://localhost:8000')
    ->build();



$response = $sdk->discovery->get(

);

if ($response->discoveryResponse !== null) {
    // handle response
}
```
<!-- End Server Selection [server] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=localprotocol/local-protocol-sdk&utm_campaign=php)
