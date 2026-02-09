# Requests

## Overview

Delivery request operations

### Available Operations

* [createRequest](#createrequest) - Create delivery request
* [listRequests](#listrequests) - List delivery requests
* [getRequest](#getrequest) - Get delivery request

## createRequest

Submit a new delivery request. The `nonce` field provides idempotency.

### Example Usage

<!-- UsageSnippet language="typescript" operationID="createRequest" method="post" path="/requests" -->
```typescript
import { LocalProtocol } from "@localprotocol/sdk";

const localProtocol = new LocalProtocol();

async function run() {
  const result = await localProtocol.requests.createRequest({
    id: "<id>",
    nonce: "<value>",
    pickupLocation: {
      coordinates: {
        latitude: 9821.48,
        longitude: 3629.78,
      },
    },
    dropoffLocation: {
      postalAddress: {},
    },
    pickupTime: new Date("2026-06-22T12:35:13.217Z"),
    dropoffTime: new Date("2026-02-21T01:14:18.597Z"),
  });

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { LocalProtocolCore } from "@localprotocol/sdk/core.js";
import { requestsCreateRequest } from "@localprotocol/sdk/funcs/requests-create-request.js";

// Use `LocalProtocolCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const localProtocol = new LocalProtocolCore();

async function run() {
  const res = await requestsCreateRequest(localProtocol, {
    id: "<id>",
    nonce: "<value>",
    pickupLocation: {
      coordinates: {
        latitude: 9821.48,
        longitude: 3629.78,
      },
    },
    dropoffLocation: {
      postalAddress: {},
    },
    pickupTime: new Date("2026-06-22T12:35:13.217Z"),
    dropoffTime: new Date("2026-02-21T01:14:18.597Z"),
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("requestsCreateRequest failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [components.DeliveryRequestCreate](../../models/components/delivery-request-create.md)                                                                                         | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[components.DeliveryRequest](../../models/components/delivery-request.md)\>**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.ErrorResponse             | 400, 409                         | application/json                 |
| errors.ValidationErrorResponse   | 422                              | application/json                 |
| errors.LocalProtocolDefaultError | 4XX, 5XX                         | \*/\*                            |

## listRequests

Returns all delivery requests.

### Example Usage

<!-- UsageSnippet language="typescript" operationID="listRequests" method="get" path="/requests" -->
```typescript
import { LocalProtocol } from "@localprotocol/sdk";

const localProtocol = new LocalProtocol();

async function run() {
  const result = await localProtocol.requests.listRequests();

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { LocalProtocolCore } from "@localprotocol/sdk/core.js";
import { requestsListRequests } from "@localprotocol/sdk/funcs/requests-list-requests.js";

// Use `LocalProtocolCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const localProtocol = new LocalProtocolCore();

async function run() {
  const res = await requestsListRequests(localProtocol);
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("requestsListRequests failed:", res.error);
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

**Promise\<[components.DeliveryRequest[]](../../models/.md)\>**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.ErrorResponse             | 500                              | application/json                 |
| errors.LocalProtocolDefaultError | 4XX, 5XX                         | \*/\*                            |

## getRequest

Returns a single delivery request by ID.

### Example Usage

<!-- UsageSnippet language="typescript" operationID="getRequest" method="get" path="/requests/{request_id}" -->
```typescript
import { LocalProtocol } from "@localprotocol/sdk";

const localProtocol = new LocalProtocol();

async function run() {
  const result = await localProtocol.requests.getRequest("<id>");

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { LocalProtocolCore } from "@localprotocol/sdk/core.js";
import { requestsGetRequest } from "@localprotocol/sdk/funcs/requests-get-request.js";

// Use `LocalProtocolCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const localProtocol = new LocalProtocolCore();

async function run() {
  const res = await requestsGetRequest(localProtocol, "<id>");
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("requestsGetRequest failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `requestId`                                                                                                                                                                    | *string*                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                             | Delivery request identifier.                                                                                                                                                   |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[components.DeliveryRequest](../../models/components/delivery-request.md)\>**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.ErrorResponse             | 404                              | application/json                 |
| errors.LocalProtocolDefaultError | 4XX, 5XX                         | \*/\*                            |