# RequestsApi

All URIs are relative to *http://localhost:8000*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createRequest**](RequestsApi.md#createrequest) | **POST** /requests | Create delivery request |
| [**getRequest**](RequestsApi.md#getrequest) | **GET** /requests/{request_id} | Get delivery request |
| [**listRequests**](RequestsApi.md#listrequests) | **GET** /requests | List delivery requests |



## createRequest

> DeliveryRequest createRequest(deliveryRequestCreate)

Create delivery request

Submit a new delivery request. The &#x60;nonce&#x60; field provides idempotency.

### Example

```ts
import {
  Configuration,
  RequestsApi,
} from '@localprotocol/sdk';
import type { CreateRequestRequest } from '@localprotocol/sdk';

async function example() {
  console.log("🚀 Testing @localprotocol/sdk SDK...");
  const api = new RequestsApi();

  const body = {
    // DeliveryRequestCreate
    deliveryRequestCreate: ...,
  } satisfies CreateRequestRequest;

  try {
    const data = await api.createRequest(body);
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
| **deliveryRequestCreate** | [DeliveryRequestCreate](DeliveryRequestCreate.md) |  | |

### Return type

[**DeliveryRequest**](DeliveryRequest.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Request created. |  -  |
| **400** | Invalid nonce. |  -  |
| **409** | Duplicate nonce or request ID. |  -  |
| **422** | Validation errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getRequest

> DeliveryRequest getRequest(requestId)

Get delivery request

Returns a single delivery request by ID.

### Example

```ts
import {
  Configuration,
  RequestsApi,
} from '@localprotocol/sdk';
import type { GetRequestRequest } from '@localprotocol/sdk';

async function example() {
  console.log("🚀 Testing @localprotocol/sdk SDK...");
  const api = new RequestsApi();

  const body = {
    // string | Delivery request identifier.
    requestId: requestId_example,
  } satisfies GetRequestRequest;

  try {
    const data = await api.getRequest(body);
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

[**DeliveryRequest**](DeliveryRequest.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request. |  -  |
| **404** | Request not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listRequests

> Array&lt;DeliveryRequest&gt; listRequests()

List delivery requests

Returns all delivery requests.

### Example

```ts
import {
  Configuration,
  RequestsApi,
} from '@localprotocol/sdk';
import type { ListRequestsRequest } from '@localprotocol/sdk';

async function example() {
  console.log("🚀 Testing @localprotocol/sdk SDK...");
  const api = new RequestsApi();

  try {
    const data = await api.listRequests();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**Array&lt;DeliveryRequest&gt;**](DeliveryRequest.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of requests. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

