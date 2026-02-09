# CreateOrderRequest

Body for creating an order from an accepted quote.

## Example Usage

```typescript
import { CreateOrderRequest } from "@localprotocol/sdk/models/components";

let value: CreateOrderRequest = {
  orderRequestId: "<id>",
  orderQuoteId: "<id>",
  nonce: "<value>",
  paymentInstrumentId: "<id>",
};
```

## Fields

| Field                                           | Type                                            | Required                                        | Description                                     |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| `orderRequestId`                                | *string*                                        | :heavy_check_mark:                              | The order request to fulfill.                   |
| `orderQuoteId`                                  | *string*                                        | :heavy_check_mark:                              | The accepted quote.                             |
| `nonce`                                         | *string*                                        | :heavy_check_mark:                              | Client-generated idempotency key.               |
| `paymentInstrumentId`                           | *string*                                        | :heavy_check_mark:                              | Reference to the registered payment instrument. |