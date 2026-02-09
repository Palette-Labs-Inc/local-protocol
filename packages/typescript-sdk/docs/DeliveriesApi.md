# DeliveriesApi

All URIs are relative to *http://localhost:8000*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createDelivery**](DeliveriesApi.md#createdeliveryoperation) | **POST** /deliveries | Create delivery |
| [**getDelivery**](DeliveriesApi.md#getdelivery) | **GET** /deliveries/{delivery_id} | Get delivery |
| [**listDeliveries**](DeliveriesApi.md#listdeliveries) | **GET** /deliveries | List deliveries |
| [**updateDeliveryEvent**](DeliveriesApi.md#updatedeliveryevent) | **PATCH** /deliveries/{delivery_id}/event | Update delivery event |



## createDelivery

> Delivery createDelivery(createDeliveryRequest)

Create delivery

Accept a quote and create a delivery. The &#x60;nonce&#x60; field provides idempotency.

### Example

```ts
import {
  Configuration,
  DeliveriesApi,
} from '@localprotocol/sdk';
import type { CreateDeliveryOperationRequest } from '@localprotocol/sdk';

async function example() {
  console.log("🚀 Testing @localprotocol/sdk SDK...");
  const api = new DeliveriesApi();

  const body = {
    // CreateDeliveryRequest
    createDeliveryRequest: ...,
  } satisfies CreateDeliveryOperationRequest;

  try {
    const data = await api.createDelivery(body);
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
| **createDeliveryRequest** | [CreateDeliveryRequest](CreateDeliveryRequest.md) |  | |

### Return type

[**Delivery**](Delivery.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Delivery created. |  -  |
| **400** | Invalid nonce or quote does not belong to request. |  -  |
| **404** | Request or quote not found. |  -  |
| **409** | Duplicate nonce or nonce reuse with different payload. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getDelivery

> Delivery getDelivery(deliveryId)

Get delivery

Returns a single delivery by ID.

### Example

```ts
import {
  Configuration,
  DeliveriesApi,
} from '@localprotocol/sdk';
import type { GetDeliveryRequest } from '@localprotocol/sdk';

async function example() {
  console.log("🚀 Testing @localprotocol/sdk SDK...");
  const api = new DeliveriesApi();

  const body = {
    // string | Delivery identifier.
    deliveryId: deliveryId_example,
  } satisfies GetDeliveryRequest;

  try {
    const data = await api.getDelivery(body);
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
| **deliveryId** | `string` | Delivery identifier. | [Defaults to `undefined`] |

### Return type

[**Delivery**](Delivery.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The delivery. |  -  |
| **404** | Delivery not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listDeliveries

> Array&lt;Delivery&gt; listDeliveries()

List deliveries

Returns all deliveries.

### Example

```ts
import {
  Configuration,
  DeliveriesApi,
} from '@localprotocol/sdk';
import type { ListDeliveriesRequest } from '@localprotocol/sdk';

async function example() {
  console.log("🚀 Testing @localprotocol/sdk SDK...");
  const api = new DeliveriesApi();

  try {
    const data = await api.listDeliveries();
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

[**Array&lt;Delivery&gt;**](Delivery.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of deliveries. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## updateDeliveryEvent

> Delivery updateDeliveryEvent(deliveryId, updateEventRequest)

Update delivery event

Transition a delivery to a new event state. If a webhook URL was registered, the server pushes an event notification in the background.

### Example

```ts
import {
  Configuration,
  DeliveriesApi,
} from '@localprotocol/sdk';
import type { UpdateDeliveryEventRequest } from '@localprotocol/sdk';

async function example() {
  console.log("🚀 Testing @localprotocol/sdk SDK...");
  const api = new DeliveriesApi();

  const body = {
    // string | Delivery identifier.
    deliveryId: deliveryId_example,
    // UpdateEventRequest
    updateEventRequest: ...,
  } satisfies UpdateDeliveryEventRequest;

  try {
    const data = await api.updateDeliveryEvent(body);
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
| **deliveryId** | `string` | Delivery identifier. | [Defaults to `undefined`] |
| **updateEventRequest** | [UpdateEventRequest](UpdateEventRequest.md) |  | |

### Return type

[**Delivery**](Delivery.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Delivery event updated. |  -  |
| **404** | Delivery not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

