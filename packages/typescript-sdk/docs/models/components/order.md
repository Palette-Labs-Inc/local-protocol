# Order

An order.

## Example Usage

```typescript
import { Order } from "@localprotocol/sdk/models/components";

let value: Order = {
  id: "<id>",
  intentId: "<id>",
  nonce: "<value>",
  paymentInstrumentId: "<id>",
};
```

## Fields

| Field                                                           | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `id`                                                            | *string*                                                        | :heavy_check_mark:                                              | Unique order identifier.                                        |
| `intentId`                                                      | *string*                                                        | :heavy_check_mark:                                              | Shared intent identifier for tracing Request -> Quote -> Order. |
| `nonce`                                                         | *string*                                                        | :heavy_check_mark:                                              | Client-generated idempotency key.                               |
| `paymentInstrumentId`                                           | *string*                                                        | :heavy_check_mark:                                              | Reference to the payment instrument used.                       |