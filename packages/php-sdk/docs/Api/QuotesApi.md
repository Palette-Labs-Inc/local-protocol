# LocalProtocolSdk\QuotesApi

Delivery quote operations

All URIs are relative to http://localhost:8000, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**createQuote()**](QuotesApi.md#createQuote) | **POST** /requests/{request_id}/quotes | Create quote |
| [**getQuote()**](QuotesApi.md#getQuote) | **GET** /requests/{request_id}/quotes/{quote_id} | Get quote |
| [**listQuotes()**](QuotesApi.md#listQuotes) | **GET** /requests/{request_id}/quotes | List quotes for request |


## `createQuote()`

```php
createQuote($request_id, $delivery_quote_create): \LocalProtocolSdk\Model\DeliveryQuote
```

Create quote

Submit a quote for a delivery request. The `nonce` field provides idempotency.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new LocalProtocolSdk\Api\QuotesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$request_id = 'request_id_example'; // string | Delivery request identifier.
$delivery_quote_create = new \LocalProtocolSdk\Model\DeliveryQuoteCreate(); // \LocalProtocolSdk\Model\DeliveryQuoteCreate

try {
    $result = $apiInstance->createQuote($request_id, $delivery_quote_create);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling QuotesApi->createQuote: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **request_id** | **string**| Delivery request identifier. | |
| **delivery_quote_create** | [**\LocalProtocolSdk\Model\DeliveryQuoteCreate**](../Model/DeliveryQuoteCreate.md)|  | |

### Return type

[**\LocalProtocolSdk\Model\DeliveryQuote**](../Model/DeliveryQuote.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getQuote()`

```php
getQuote($request_id, $quote_id): \LocalProtocolSdk\Model\DeliveryQuote
```

Get quote

Returns a single quote by ID.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new LocalProtocolSdk\Api\QuotesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$request_id = 'request_id_example'; // string | Delivery request identifier.
$quote_id = 'quote_id_example'; // string | Quote identifier.

try {
    $result = $apiInstance->getQuote($request_id, $quote_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling QuotesApi->getQuote: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **request_id** | **string**| Delivery request identifier. | |
| **quote_id** | **string**| Quote identifier. | |

### Return type

[**\LocalProtocolSdk\Model\DeliveryQuote**](../Model/DeliveryQuote.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `listQuotes()`

```php
listQuotes($request_id): \LocalProtocolSdk\Model\DeliveryQuote[]
```

List quotes for request

Returns all quotes for a delivery request.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new LocalProtocolSdk\Api\QuotesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$request_id = 'request_id_example'; // string | Delivery request identifier.

try {
    $result = $apiInstance->listQuotes($request_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling QuotesApi->listQuotes: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **request_id** | **string**| Delivery request identifier. | |

### Return type

[**\LocalProtocolSdk\Model\DeliveryQuote[]**](../Model/DeliveryQuote.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
