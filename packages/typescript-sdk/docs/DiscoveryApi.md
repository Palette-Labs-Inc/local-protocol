# DiscoveryApi

All URIs are relative to *http://localhost:8000*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDiscovery**](DiscoveryApi.md#getdiscovery) | **GET** /.well-known/local-protocol | Service discovery |
| [**getHealth**](DiscoveryApi.md#gethealth) | **GET** /healthz | Health check |



## getDiscovery

> DiscoveryResponse getDiscovery()

Service discovery

Returns server capabilities, supported standards, and endpoint paths.

### Example

```ts
import {
  Configuration,
  DiscoveryApi,
} from '@localprotocol/sdk';
import type { GetDiscoveryRequest } from '@localprotocol/sdk';

async function example() {
  console.log("🚀 Testing @localprotocol/sdk SDK...");
  const api = new DiscoveryApi();

  try {
    const data = await api.getDiscovery();
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

[**DiscoveryResponse**](DiscoveryResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Discovery metadata. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getHealth

> HealthResponse getHealth()

Health check

Returns server health status.

### Example

```ts
import {
  Configuration,
  DiscoveryApi,
} from '@localprotocol/sdk';
import type { GetHealthRequest } from '@localprotocol/sdk';

async function example() {
  console.log("🚀 Testing @localprotocol/sdk SDK...");
  const api = new DiscoveryApi();

  try {
    const data = await api.getHealth();
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

[**HealthResponse**](HealthResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Server is healthy. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

