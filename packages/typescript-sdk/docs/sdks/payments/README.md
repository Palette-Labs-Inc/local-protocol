# Payments

## Overview

Payment instrument operations

### Available Operations

* [createPaymentInstrument](#createpaymentinstrument) - Register payment instrument

## createPaymentInstrument

Register a payment instrument for use in order creation.

### Example Usage

<!-- UsageSnippet language="typescript" operationID="createPaymentInstrument" method="post" path="/payment-instruments" -->
```typescript
import { LocalProtocol } from "@localprotocol/sdk";

const localProtocol = new LocalProtocol();

async function run() {
  const result = await localProtocol.payments.createPaymentInstrument({
    id: "<id>",
    handlerId: "<id>",
    type: "evm_auth_capture_escrow",
    paymentInfoHash: "<value>",
    operator: "<value>",
    payer: "<value>",
    chainId: 933627,
    contract: "<value>",
    receiver: "<value>",
    token: {
      symbol: "<value>",
      decimals: 599585,
    },
    maxAmount: {
      value: "<value>",
      currency: {
        chainId: 534500,
        address: "6814 Ziemann Field",
        decimals: 609251,
      },
    },
    preapprovalExpiresAt: new Date("2024-07-26T23:36:42.374Z"),
    authorizationExpiresAt: new Date("2024-10-07T03:34:24.771Z"),
    refundExpiresAt: new Date("2024-05-30T02:15:26.285Z"),
    nonce: "<value>",
    amount: {
      value: "<value>",
      currency: {
        chainId: 534500,
        address: "6814 Ziemann Field",
        decimals: 609251,
      },
    },
  });

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:

```typescript
import { LocalProtocolCore } from "@localprotocol/sdk/core.js";
import { paymentsCreatePaymentInstrument } from "@localprotocol/sdk/funcs/payments-create-payment-instrument.js";

// Use `LocalProtocolCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const localProtocol = new LocalProtocolCore();

async function run() {
  const res = await paymentsCreatePaymentInstrument(localProtocol, {
    id: "<id>",
    handlerId: "<id>",
    type: "evm_auth_capture_escrow",
    paymentInfoHash: "<value>",
    operator: "<value>",
    payer: "<value>",
    chainId: 933627,
    contract: "<value>",
    receiver: "<value>",
    token: {
      symbol: "<value>",
      decimals: 599585,
    },
    maxAmount: {
      value: "<value>",
      currency: {
        chainId: 534500,
        address: "6814 Ziemann Field",
        decimals: 609251,
      },
    },
    preapprovalExpiresAt: new Date("2024-07-26T23:36:42.374Z"),
    authorizationExpiresAt: new Date("2024-10-07T03:34:24.771Z"),
    refundExpiresAt: new Date("2024-05-30T02:15:26.285Z"),
    nonce: "<value>",
    amount: {
      value: "<value>",
      currency: {
        chainId: 534500,
        address: "6814 Ziemann Field",
        decimals: 609251,
      },
    },
  });
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("paymentsCreatePaymentInstrument failed:", res.error);
  }
}

run();
```

### Parameters

| Parameter                                                                                                                                                                      | Type                                                                                                                                                                           | Required                                                                                                                                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                      | [components.EvmAuthCaptureEscrowInstrument](../../models/components/evm-auth-capture-escrow-instrument.md)                                                                     | :heavy_check_mark:                                                                                                                                                             | The request object to use for the request.                                                                                                                                     |
| `options`                                                                                                                                                                      | RequestOptions                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                             | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions`                                                                                                                                                         | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options)                                                                                        | :heavy_minus_sign:                                                                                                                                                             | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`                                                                                                                                                              | [RetryConfig](../../lib/utils/retryconfig.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                             | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[components.EvmAuthCaptureEscrowInstrument](../../models/components/evm-auth-capture-escrow-instrument.md)\>**

### Errors

| Error Type                       | Status Code                      | Content Type                     |
| -------------------------------- | -------------------------------- | -------------------------------- |
| errors.ErrorResponse             | 400                              | application/json                 |
| errors.ValidationErrorResponse   | 422                              | application/json                 |
| errors.LocalProtocolDefaultError | 4XX, 5XX                         | \*/\*                            |