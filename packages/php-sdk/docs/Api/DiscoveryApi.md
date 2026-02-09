# LocalProtocolSdk\DiscoveryApi

Service discovery and health

All URIs are relative to http://localhost:8000, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getDiscovery()**](DiscoveryApi.md#getDiscovery) | **GET** /.well-known/local-protocol | Service discovery |
| [**getHealth()**](DiscoveryApi.md#getHealth) | **GET** /healthz | Health check |


## `getDiscovery()`

```php
getDiscovery(): \LocalProtocolSdk\Model\DiscoveryResponse
```

Service discovery

Returns server capabilities, supported standards, and endpoint paths.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new LocalProtocolSdk\Api\DiscoveryApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);

try {
    $result = $apiInstance->getDiscovery();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DiscoveryApi->getDiscovery: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**\LocalProtocolSdk\Model\DiscoveryResponse**](../Model/DiscoveryResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getHealth()`

```php
getHealth(): \LocalProtocolSdk\Model\HealthResponse
```

Health check

Returns server health status.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new LocalProtocolSdk\Api\DiscoveryApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);

try {
    $result = $apiInstance->getHealth();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DiscoveryApi->getHealth: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**\LocalProtocolSdk\Model\HealthResponse**](../Model/HealthResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
