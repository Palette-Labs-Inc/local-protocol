# QuotesApi

All URIs are relative to *http://localhost:8000*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createQuote**](QuotesApi.md#createquote) | **POST** /requests/{request_id}/quotes | Create quote |
| [**getQuote**](QuotesApi.md#getquote) | **GET** /requests/{request_id}/quotes/{quote_id} | Get quote |
| [**listQuotes**](QuotesApi.md#listquotes) | **GET** /requests/{request_id}/quotes | List quotes for request |



## createQuote

> DeliveryQuote createQuote(requestId, deliveryQuoteCreate)

Create quote

Submit a quote for a delivery request. The &#x60;nonce&#x60; field provides idempotency.

### Example

```ts
import {
  Configuration,
  QuotesApi,
} from '@localprotocol/sdk';
import type { CreateQuoteRequest } from '@localprotocol/sdk';

async function example() {
  console.log("🚀 Testing @localprotocol/sdk SDK...");
  const api = new QuotesApi();

  const body = {
    // string | Delivery request identifier.
    requestId: requestId_example,
    // DeliveryQuoteCreate
    deliveryQuoteCreate: ...,
  } satisfies CreateQuoteRequest;

  try {
    const data = await api.createQuote(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **requestId** | `string` | Delivery request identifier. | [Defaults to `undefined`] |
| **deliveryQuoteCreate** | [DeliveryQuoteCreate](DeliveryQuoteCreate.md) |  | |

### Return type

[**DeliveryQuote**](DeliveryQuote.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Quote created. |  -  |
| **400** | Invalid nonce. |  -  |
| **404** | Request not found. |  -  |
| **409** | Duplicate nonce or quote ID. |  -  |
| **422** | Validation errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getQuote

> DeliveryQuote getQuote(requestId, quoteId)

Get quote

Returns a single quote by ID.

### Example

```ts
import {
  Configuration,
  QuotesApi,
} from '@localprotocol/sdk';
import type { GetQuoteRequest } from '@localprotocol/sdk';

async function example() {
  console.log("🚀 Testing @localprotocol/sdk SDK...");
  const api = new QuotesApi();

  const body = {
    // string | Delivery request identifier.
    requestId: requestId_example,
    // string | Quote identifier.
    quoteId: quoteId_example,
  } satisfies GetQuoteRequest;

  try {
    const data = await api.getQuote(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **requestId** | `string` | Delivery request identifier. | [Defaults to `undefined`] |
| **quoteId** | `string` | Quote identifier. | [Defaults to `undefined`] |

### Return type

[**DeliveryQuote**](DeliveryQuote.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The quote. |  -  |
| **404** | Request or quote not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listQuotes

> Array&lt;DeliveryQuote&gt; listQuotes(requestId)

List quotes for request

Returns all quotes for a delivery request.

### Example

```ts
import {
  Configuration,
  QuotesApi,
} from '@localprotocol/sdk';
import type { ListQuotesRequest } from '@localprotocol/sdk';

async function example() {
  console.log("🚀 Testing @localprotocol/sdk SDK...");
  const api = new QuotesApi();

  const body = {
    // string | Delivery request identifier.
    requestId: requestId_example,
  } satisfies ListQuotesRequest;

  try {
    const data = await api.listQuotes(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **requestId** | `string` | Delivery request identifier. | [Defaults to `undefined`] |

### Return type

[**Array&lt;DeliveryQuote&gt;**](DeliveryQuote.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of quotes. |  -  |
| **404** | Request not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

