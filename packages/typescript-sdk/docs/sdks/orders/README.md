# Orders

## Overview

Order lifecycle operations

### Available Operations

* [createOrderRequest](#createorderrequest) - Create order request
* [listOrderQuotes](#listorderquotes) - List order quotes
* [getOrderQuote](#getorderquote) - Get order quote
* [createOrder](#createorder) - Create order
* [getOrder](#getorder) - Get order

## createOrderRequest

Submit a new order request with a cart. The `nonce` field provides idempotency.

### Example Usage

<!-- UsageSnippet language="typescript" operationID="createOrderRequest" method="post" path="/orders/requests" -->
```typescript
import { LocalProtocol } from "@localprotocol/sdk";

const localProtocol = new LocalProtocol();

async function run() {
  const result = await localProtocol.orders.createOrderRequest({
    id: "<id>",
    intentId: "<id>",
    nonce: "<value>",
    items: [
      {
        id: "<id>",
        quantity: 755842,
      },
    ],
  });

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { LocalProtocolCore } from "@localprotocol/sdk/core.js";
import { ordersCreateOrderRequest } from "@localprotocol/sdk/funcs/orders-create-order-request.js";

// Use `LocalProtocolCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const localProtocol = new LocalProtocolCore();

async function run() {
  const res = await ordersCreateOrderRequest(localProtocol, {
    id: "<id>",
    intentId: "<id>",
    nonce: "<value>",
    items: [
      {
        id: "<id>",
        quantity: 755842,
      },
    ],
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("ordersCreateOrderRequest failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [components.Cart](../../models/components/cart.md)                                                                                                                             | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[components.OrderRequest](../../models/components/order-request.md)\>**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.ErrorResponse             | 400, 409                         | application/json                 |
| errors.ValidationErrorResponse   | 422                              | application/json                 |
| errors.LocalProtocolDefaultError | 4XX, 5XX                         | \*/\*                            |

## listOrderQuotes

Returns all quotes for an order request.

### Example Usage

<!-- UsageSnippet language="typescript" operationID="listOrderQuotes" method="get" path="/orders/requests/{order_request_id}/quotes" -->
```typescript
import { LocalProtocol } from "@localprotocol/sdk";

const localProtocol = new LocalProtocol();

async function run() {
  const result = await localProtocol.orders.listOrderQuotes("<id>");

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { LocalProtocolCore } from "@localprotocol/sdk/core.js";
import { ordersListOrderQuotes } from "@localprotocol/sdk/funcs/orders-list-order-quotes.js";

// Use `LocalProtocolCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const localProtocol = new LocalProtocolCore();

async function run() {
  const res = await ordersListOrderQuotes(localProtocol, "<id>");
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("ordersListOrderQuotes failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `orderRequestId`                                                                                                                                                               | *string*                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                             | Order request identifier.                                                                                                                                                      |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[components.OrderQuote[]](../../models/.md)\>**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.ErrorResponse             | 404                              | application/json                 |
| errors.LocalProtocolDefaultError | 4XX, 5XX                         | \*/\*                            |

## getOrderQuote

Returns a single order quote by ID.

### Example Usage

<!-- UsageSnippet language="typescript" operationID="getOrderQuote" method="get" path="/orders/requests/{order_request_id}/quotes/{order_quote_id}" -->
```typescript
import { LocalProtocol } from "@localprotocol/sdk";

const localProtocol = new LocalProtocol();

async function run() {
  const result = await localProtocol.orders.getOrderQuote("<id>", "<id>");

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { LocalProtocolCore } from "@localprotocol/sdk/core.js";
import { ordersGetOrderQuote } from "@localprotocol/sdk/funcs/orders-get-order-quote.js";

// Use `LocalProtocolCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const localProtocol = new LocalProtocolCore();

async function run() {
  const res = await ordersGetOrderQuote(localProtocol, "<id>", "<id>");
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("ordersGetOrderQuote failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `orderRequestId`                                                                                                                                                               | *string*                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                             | Order request identifier.                                                                                                                                                      |
| `orderQuoteId`                                                                                                                                                                 | *string*                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                             | Order quote identifier.                                                                                                                                                        |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[components.OrderQuote](../../models/components/order-quote.md)\>**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.ErrorResponse             | 404                              | application/json                 |
| errors.LocalProtocolDefaultError | 4XX, 5XX                         | \*/\*                            |

## createOrder

Accept a quote and create an order. The `nonce` field provides idempotency.

### Example Usage

<!-- UsageSnippet language="typescript" operationID="createOrder" method="post" path="/orders" -->
```typescript
import { LocalProtocol } from "@localprotocol/sdk";

const localProtocol = new LocalProtocol();

async function run() {
  const result = await localProtocol.orders.createOrder({
    orderRequestId: "<id>",
    orderQuoteId: "<id>",
    nonce: "<value>",
    paymentInstrumentId: "<id>",
  });

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { LocalProtocolCore } from "@localprotocol/sdk/core.js";
import { ordersCreateOrder } from "@localprotocol/sdk/funcs/orders-create-order.js";

// Use `LocalProtocolCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const localProtocol = new LocalProtocolCore();

async function run() {
  const res = await ordersCreateOrder(localProtocol, {
    orderRequestId: "<id>",
    orderQuoteId: "<id>",
    nonce: "<value>",
    paymentInstrumentId: "<id>",
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("ordersCreateOrder failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [components.CreateOrderRequest](../../models/components/create-order-request.md)                                                                                               | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[components.Order](../../models/components/order.md)\>**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.ErrorResponse             | 400, 404, 409                    | application/json                 |
| errors.LocalProtocolDefaultError | 4XX, 5XX                         | \*/\*                            |

## getOrder

Returns a single order by ID.

### Example Usage

<!-- UsageSnippet language="typescript" operationID="getOrder" method="get" path="/orders/{order_id}" -->
```typescript
import { LocalProtocol } from "@localprotocol/sdk";

const localProtocol = new LocalProtocol();

async function run() {
  const result = await localProtocol.orders.getOrder("<id>");

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { LocalProtocolCore } from "@localprotocol/sdk/core.js";
import { ordersGetOrder } from "@localprotocol/sdk/funcs/orders-get-order.js";

// Use `LocalProtocolCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const localProtocol = new LocalProtocolCore();

async function run() {
  const res = await ordersGetOrder(localProtocol, "<id>");
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("ordersGetOrder failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `orderId`                                                                                                                                                                      | *string*                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                             | Order identifier.                                                                                                                                                              |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[components.Order](../../models/components/order.md)\>**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.ErrorResponse             | 404                              | application/json                 |
| errors.LocalProtocolDefaultError | 4XX, 5XX                         | \*/\*                            |