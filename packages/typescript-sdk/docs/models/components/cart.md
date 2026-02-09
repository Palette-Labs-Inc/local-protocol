# Cart

A shopping cart.

## Example Usage

```typescript
import { Cart } from "@localprotocol/sdk/models/components";

let value: Cart = {
  id: "<id>",
  intentId: "<id>",
  nonce: "<value>",
  items: [
    {
      id: "<id>",
      quantity: 834295,
    },
  ],
};
```

## Fields

| Field                                                           | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `id`                                                            | *string*                                                        | :heavy_check_mark:                                              | Unique cart identifier.                                         |
| `intentId`                                                      | *string*                                                        | :heavy_check_mark:                                              | Shared intent identifier for tracing Request -> Quote -> Order. |
| `nonce`                                                         | *string*                                                        | :heavy_check_mark:                                              | Client-generated idempotency key.                               |
| `items`                                                         | [components.CartItem](../../models/components/cart-item.md)[]   | :heavy_check_mark:                                              | Items in the cart.                                              |