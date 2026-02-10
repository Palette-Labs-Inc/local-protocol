# Local Protocol PHP API library

The Local Protocol PHP library provides convenient access to the Local Protocol REST API from any PHP 8.1.0+ application.

It is generated with [Stainless](https://www.stainless.com/).

## Documentation

The REST API documentation can be found on [localprotocol.xyz](https://localprotocol.xyz).

## Installation

To use this package, install via Composer by adding the following to your application's `composer.json`:

<!-- x-release-please-start-version -->

```json
{
  "repositories": [
    {
      "type": "vcs",
      "url": "git@github.com:Palette-Labs-Inc/local-protocol-php.git"
    }
  ],
  "require": {
    "local-protocol/local-protocol": "dev-main"
  }
}
```

<!-- x-release-please-end -->

## Usage

This library uses named parameters to specify optional arguments.
Parameters with a default value must be set by name.

```php
<?php

use LocalProtocol\Client;

$client = new Client();

$deliveryRequest = $client->requests->create(
  id: 'req_demo_123',
  dropoffLocation: [
    'coordinates' => ['latitude' => 37.7875, 'longitude' => -122.4073]
  ],
  dropoffTime: new \DateTimeImmutable('2026-02-10T17:30:00Z'),
  nonce: 'nonce_demo_123',
  pickupLocation: [
    'coordinates' => ['latitude' => 37.7751, 'longitude' => -122.4193]
  ],
  pickupTime: new \DateTimeImmutable('2026-02-10T17:00:00Z'),
);

var_dump($deliveryRequest->id);
```

### Value Objects

It is recommended to use the static `with` constructor `Coordinates::with(latitude: -90, ...)`
and named parameters to initialize value objects.

However, builders are also provided `(new Coordinates)->withLatitude(-90)`.

### Handling errors

When the library is unable to connect to the API, or if the API returns a non-success status code (i.e., 4xx or 5xx response), a subclass of `LocalProtocol\Core\Exceptions\APIException` will be thrown:

```php
<?php

use LocalProtocol\Core\Exceptions\APIConnectionException;
use LocalProtocol\Core\Exceptions\RateLimitException;
use LocalProtocol\Core\Exceptions\APIStatusException;

try {
  $wellKnown = $client->wellKnown->retrieve();
} catch (APIConnectionException $e) {
  echo "The server could not be reached", PHP_EOL;
  var_dump($e->getPrevious());
} catch (RateLimitException $e) {
  echo "A 429 status code was received; we should back off a bit.", PHP_EOL;
} catch (APIStatusException $e) {
  echo "Another non-200-range status code was received", PHP_EOL;
  echo $e->getMessage();
}
```

Error codes are as follows:

| Cause            | Error Type                     |
| ---------------- | ------------------------------ |
| HTTP 400         | `BadRequestException`          |
| HTTP 401         | `AuthenticationException`      |
| HTTP 403         | `PermissionDeniedException`    |
| HTTP 404         | `NotFoundException`            |
| HTTP 409         | `ConflictException`            |
| HTTP 422         | `UnprocessableEntityException` |
| HTTP 429         | `RateLimitException`           |
| HTTP >= 500      | `InternalServerException`      |
| Other HTTP error | `APIStatusException`           |
| Timeout          | `APITimeoutException`          |
| Network error    | `APIConnectionException`       |

### Retries

Certain errors will be automatically retried 2 times by default, with a short exponential backoff.

Connection errors (for example, due to a network connectivity problem), 408 Request Timeout, 409 Conflict, 429 Rate Limit, >=500 Internal errors, and timeouts will all be retried by default.

You can use the `maxRetries` option to configure or disable this:

```php
<?php

use LocalProtocol\Client;

// Configure the default for all requests:
$client = new Client(requestOptions: ['maxRetries' => 0]);

// Or, configure per-request:
$result = $client->wellKnown->retrieve(requestOptions: ['maxRetries' => 5]);
```

## Advanced concepts

### Making custom or undocumented requests

#### Undocumented properties

You can send undocumented parameters to any endpoint, and read undocumented response properties, like so:

Note: the `extra*` parameters of the same name overrides the documented parameters.

```php
<?php

$wellKnown = $client->wellKnown->retrieve(
  requestOptions: [
    'extraQueryParams' => ['my_query_parameter' => 'value'],
    'extraBodyParams' => ['my_body_parameter' => 'value'],
    'extraHeaders' => ['my-header' => 'value'],
  ],
);
```

#### Undocumented request params

If you want to explicitly send an extra param, you can do so with the `extra_query`, `extra_body`, and `extra_headers` under the `request_options:` parameter when making a request, as seen in the examples above.

#### Undocumented endpoints

To make requests to undocumented endpoints while retaining the benefit of auth, retries, and so on, you can make requests using `client.request`, like so:

```php
<?php

$response = $client->request(
  method: "post",
  path: '/undocumented/endpoint',
  query: ['dog' => 'woof'],
  headers: ['useful-header' => 'interesting-value'],
  body: ['hello' => 'world']
);
```

## Versioning

This package follows [SemVer](https://semver.org/spec/v2.0.0.html) conventions. As the library is in initial development and has a major version of `0`, APIs may change at any time.

This package considers improvements to the (non-runtime) PHPDoc type definitions to be non-breaking changes.

## Requirements

PHP 8.1.0 or higher.

## Contributing

See [the contributing documentation](https://github.com/Palette-Labs-Inc/local-protocol-php/tree/main/CONTRIBUTING.md).
