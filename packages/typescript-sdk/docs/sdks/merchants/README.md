# Merchants

## Overview

Merchant and catalog operations

### Available Operations

* [getMerchant](#getmerchant) - Get merchant
* [listMerchantPaymentHandlers](#listmerchantpaymenthandlers) - List payment handlers

## getMerchant

Returns a merchant with its full denormalized catalog tree.

### Example Usage

<!-- UsageSnippet language="typescript" operationID="getMerchant" method="get" path="/merchants/{merchant_id}" -->
```typescript
import { LocalProtocol } from "@localprotocol/sdk";

const localProtocol = new LocalProtocol();

async function run() {
  const result = await localProtocol.merchants.getMerchant("<id>");

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { LocalProtocolCore } from "@localprotocol/sdk/core.js";
import { merchantsGetMerchant } from "@localprotocol/sdk/funcs/merchants-get-merchant.js";

// Use `LocalProtocolCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const localProtocol = new LocalProtocolCore();

async function run() {
  const res = await merchantsGetMerchant(localProtocol, "<id>");
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("merchantsGetMerchant failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `merchantId`                                                                                                                                                                   | *string*                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                             | Merchant identifier.                                                                                                                                                           |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[components.Merchant](../../models/components/merchant.md)\>**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.ErrorResponse             | 404                              | application/json                 |
| errors.LocalProtocolDefaultError | 4XX, 5XX                         | \*/\*                            |

## listMerchantPaymentHandlers

Returns payment handler configurations supported by the merchant.

### Example Usage

<!-- UsageSnippet language="typescript" operationID="listMerchantPaymentHandlers" method="get" path="/merchants/{merchant_id}/payment-handlers" -->
```typescript
import { LocalProtocol } from "@localprotocol/sdk";

const localProtocol = new LocalProtocol();

async function run() {
  const result = await localProtocol.merchants.listMerchantPaymentHandlers("<id>");

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { LocalProtocolCore } from "@localprotocol/sdk/core.js";
import { merchantsListMerchantPaymentHandlers } from "@localprotocol/sdk/funcs/merchants-list-merchant-payment-handlers.js";

// Use `LocalProtocolCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const localProtocol = new LocalProtocolCore();

async function run() {
  const res = await merchantsListMerchantPaymentHandlers(localProtocol, "<id>");
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("merchantsListMerchantPaymentHandlers failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `merchantId`                                                                                                                                                                   | *string*                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                             | Merchant identifier.                                                                                                                                                           |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[components.EvmAuthCaptureEscrowConfig[]](../../models/.md)\>**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.ErrorResponse             | 404                              | application/json                 |
| errors.LocalProtocolDefaultError | 4XX, 5XX                         | \*/\*                            |