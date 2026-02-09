# Discovery

## Overview

Service discovery and health

### Available Operations

* [getDiscovery](#getdiscovery) - Service discovery
* [getHealth](#gethealth) - Health check

## getDiscovery

Returns server capabilities, supported standards, and endpoint paths.

### Example Usage

<!-- UsageSnippet language="typescript" operationID="getDiscovery" method="get" path="/.well-known/local-protocol" -->
```typescript
import { LocalProtocol } from "@localprotocol/sdk";

const localProtocol = new LocalProtocol();

async function run() {
  const result = await localProtocol.discovery.getDiscovery();

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { LocalProtocolCore } from "@localprotocol/sdk/core.js";
import { discoveryGetDiscovery } from "@localprotocol/sdk/funcs/discovery-get-discovery.js";

// Use `LocalProtocolCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const localProtocol = new LocalProtocolCore();

async function run() {
  const res = await discoveryGetDiscovery(localProtocol);
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("discoveryGetDiscovery failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[components.DiscoveryResponse](../../models/components/discovery-response.md)\>**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.ErrorResponse             | 500                              | application/json                 |
| errors.LocalProtocolDefaultError | 4XX, 5XX                         | \*/\*                            |

## getHealth

Returns server health status.

### Example Usage

<!-- UsageSnippet language="typescript" operationID="getHealth" method="get" path="/healthz" -->
```typescript
import { LocalProtocol } from "@localprotocol/sdk";

const localProtocol = new LocalProtocol();

async function run() {
  const result = await localProtocol.discovery.getHealth();

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { LocalProtocolCore } from "@localprotocol/sdk/core.js";
import { discoveryGetHealth } from "@localprotocol/sdk/funcs/discovery-get-health.js";

// Use `LocalProtocolCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const localProtocol = new LocalProtocolCore();

async function run() {
  const res = await discoveryGetHealth(localProtocol);
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("discoveryGetHealth failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[components.HealthResponse](../../models/components/health-response.md)\>**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.ErrorResponse             | 503                              | application/json                 |
| errors.LocalProtocolDefaultError | 4XX, 5XX                         | \*/\*                            |