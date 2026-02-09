# OrderRequest

An order request.

## Example Usage

```typescript
import { OrderRequest } from "@localprotocol/sdk/models/components";

let value: OrderRequest = {
  id: "<id>",
  intentId: "<id>",
  nonce: "<value>",
};
```

## Fields

| Field                                                           | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `id`                                                            | *string*                                                        | :heavy_check_mark:                                              | Unique request identifier.                                      |
| `intentId`                                                      | *string*                                                        | :heavy_check_mark:                                              | Shared intent identifier for tracing Request -> Quote -> Order. |
| `nonce`                                                         | *string*                                                        | :heavy_check_mark:                                              | Client-generated idempotency key.                               |