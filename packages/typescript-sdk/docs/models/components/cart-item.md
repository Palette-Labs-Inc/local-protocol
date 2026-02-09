# CartItem

An item in a cart.

## Example Usage

```typescript
import { CartItem } from "@localprotocol/sdk/models/components";

let value: CartItem = {
  id: "<id>",
  quantity: 66276,
};
```

## Fields

| Field               | Type                | Required            | Description         |
| ------------------- | ------------------- | ------------------- | ------------------- |
| `id`                | *string*            | :heavy_check_mark:  | Item identifier.    |
| `quantity`          | *number*            | :heavy_check_mark:  | Quantity requested. |