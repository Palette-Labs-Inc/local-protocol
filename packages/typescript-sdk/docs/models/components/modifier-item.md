# ModifierItem

A purchasable modifier item within a modifier group.

## Example Usage

```typescript
import { ModifierItem } from "@localprotocol/sdk/models/components";

let value: ModifierItem = {
  id: "<id>",
  name: "<value>",
  price: {
    value: "<value>",
    currency: {
      chainId: 793765,
      address: "9303 Belmont Road",
      decimals: 989280,
    },
  },
};
```

## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `id`                                                                                 | *string*                                                                             | :heavy_check_mark:                                                                   | Modifier item identifier.                                                            |
| `name`                                                                               | *string*                                                                             | :heavy_check_mark:                                                                   | Modifier item name.                                                                  |
| `description`                                                                        | *string*                                                                             | :heavy_minus_sign:                                                                   | Optional modifier item description.                                                  |
| `price`                                                                              | [components.Amount](../../models/components/amount.md)                               | :heavy_check_mark:                                                                   | Amount with explicit currency. Value is always in minor units (e.g., cents for USD). |
| `metadata`                                                                           | Record<string, *any*>                                                                | :heavy_minus_sign:                                                                   | Business-defined custom data.                                                        |