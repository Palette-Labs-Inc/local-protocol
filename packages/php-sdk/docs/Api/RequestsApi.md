# LocalProtocolSdk\RequestsApi

Delivery request operations

All URIs are relative to http://localhost:8000, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**createRequest()**](RequestsApi.md#createRequest) | **POST** /requests | Create delivery request |
| [**getRequest()**](RequestsApi.md#getRequest) | **GET** /requests/{request_id} | Get delivery request |
| [**listRequests()**](RequestsApi.md#listRequests) | **GET** /requests | List delivery requests |


## `createRequest()`

```php
createRequest($delivery_request_create): \LocalProtocolSdk\Model\DeliveryRequest
```

Create delivery request

Submit a new delivery request. The `nonce` field provides idempotency.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new LocalProtocolSdk\Api\RequestsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$delivery_request_create = new \LocalProtocolSdk\Model\DeliveryRequestCreate(); // \LocalProtocolSdk\Model\DeliveryRequestCreate

try {
    $result = $apiInstance->createRequest($delivery_request_create);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RequestsApi->createRequest: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **delivery_request_create** | [**\LocalProtocolSdk\Model\DeliveryRequestCreate**](../Model/DeliveryRequestCreate.md)|  | |

### Return type

[**\LocalProtocolSdk\Model\DeliveryRequest**](../Model/DeliveryRequest.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getRequest()`

```php
getRequest($request_id): \LocalProtocolSdk\Model\DeliveryRequest
```

Get delivery request

Returns a single delivery request by ID.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new LocalProtocolSdk\Api\RequestsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$request_id = 'request_id_example'; // string | Delivery request identifier.

try {
    $result = $apiInstance->getRequest($request_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RequestsApi->getRequest: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **request_id** | **string**| Delivery request identifier. | |

### Return type

[**\LocalProtocolSdk\Model\DeliveryRequest**](../Model/DeliveryRequest.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `listRequests()`

```php
listRequests(): \LocalProtocolSdk\Model\DeliveryRequest[]
```

List delivery requests

Returns all delivery requests.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new LocalProtocolSdk\Api\RequestsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);

try {
    $result = $apiInstance->listRequests();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RequestsApi->listRequests: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**\LocalProtocolSdk\Model\DeliveryRequest[]**](../Model/DeliveryRequest.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
