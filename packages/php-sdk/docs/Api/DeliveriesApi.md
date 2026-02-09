# LocalProtocolSdk\DeliveriesApi

Delivery lifecycle operations

All URIs are relative to http://localhost:8000, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**createDelivery()**](DeliveriesApi.md#createDelivery) | **POST** /deliveries | Create delivery |
| [**getDelivery()**](DeliveriesApi.md#getDelivery) | **GET** /deliveries/{delivery_id} | Get delivery |
| [**listDeliveries()**](DeliveriesApi.md#listDeliveries) | **GET** /deliveries | List deliveries |
| [**updateDeliveryEvent()**](DeliveriesApi.md#updateDeliveryEvent) | **PATCH** /deliveries/{delivery_id}/event | Update delivery event |


## `createDelivery()`

```php
createDelivery($create_delivery_request): \LocalProtocolSdk\Model\Delivery
```

Create delivery

Accept a quote and create a delivery. The `nonce` field provides idempotency.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new LocalProtocolSdk\Api\DeliveriesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$create_delivery_request = new \LocalProtocolSdk\Model\CreateDeliveryRequest(); // \LocalProtocolSdk\Model\CreateDeliveryRequest

try {
    $result = $apiInstance->createDelivery($create_delivery_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DeliveriesApi->createDelivery: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **create_delivery_request** | [**\LocalProtocolSdk\Model\CreateDeliveryRequest**](../Model/CreateDeliveryRequest.md)|  | |

### Return type

[**\LocalProtocolSdk\Model\Delivery**](../Model/Delivery.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getDelivery()`

```php
getDelivery($delivery_id): \LocalProtocolSdk\Model\Delivery
```

Get delivery

Returns a single delivery by ID.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new LocalProtocolSdk\Api\DeliveriesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$delivery_id = 'delivery_id_example'; // string | Delivery identifier.

try {
    $result = $apiInstance->getDelivery($delivery_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DeliveriesApi->getDelivery: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **delivery_id** | **string**| Delivery identifier. | |

### Return type

[**\LocalProtocolSdk\Model\Delivery**](../Model/Delivery.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `listDeliveries()`

```php
listDeliveries(): \LocalProtocolSdk\Model\Delivery[]
```

List deliveries

Returns all deliveries.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new LocalProtocolSdk\Api\DeliveriesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);

try {
    $result = $apiInstance->listDeliveries();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DeliveriesApi->listDeliveries: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**\LocalProtocolSdk\Model\Delivery[]**](../Model/Delivery.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `updateDeliveryEvent()`

```php
updateDeliveryEvent($delivery_id, $update_event_request): \LocalProtocolSdk\Model\Delivery
```

Update delivery event

Transition a delivery to a new event state. If a webhook URL was registered, the server pushes an event notification in the background.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new LocalProtocolSdk\Api\DeliveriesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$delivery_id = 'delivery_id_example'; // string | Delivery identifier.
$update_event_request = new \LocalProtocolSdk\Model\UpdateEventRequest(); // \LocalProtocolSdk\Model\UpdateEventRequest

try {
    $result = $apiInstance->updateDeliveryEvent($delivery_id, $update_event_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DeliveriesApi->updateDeliveryEvent: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **delivery_id** | **string**| Delivery identifier. | |
| **update_event_request** | [**\LocalProtocolSdk\Model\UpdateEventRequest**](../Model/UpdateEventRequest.md)|  | |

### Return type

[**\LocalProtocolSdk\Model\Delivery**](../Model/Delivery.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
