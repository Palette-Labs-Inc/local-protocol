# CatalogItem

A menu item with embedded modifier groups.

## Example Usage

```typescript
import { CatalogItem } from "@localprotocol/sdk/models/components";

let value: CatalogItem = {
  id: "<id>",
  name: "<value>",
  description: "on nor terrorise meanwhile fervently",
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
| `id`                                                                                 | *string*                                                                             | :heavy_check_mark:                                                                   | Item identifier.                                                                     |
| `name`                                                                               | *string*                                                                             | :heavy_check_mark:                                                                   | Item name.                                                                           |
| `description`                                                                        | *string*                                                                             | :heavy_check_mark:                                                                   | Item description.                                                                    |
| `price`                                                                              | [components.Amount](../../models/components/amount.md)                               | :heavy_check_mark:                                                                   | Amount with explicit currency. Value is always in minor units (e.g., cents for USD). |
| `media`                                                                              | [components.Media](../../models/components/media.md)[]                               | :heavy_minus_sign:                                                                   | Item media (images, videos, 3D models).                                              |
| `modifierGroups`                                                                     | [components.ModifierGroup](../../models/components/modifier-group.md)[]              | :heavy_minus_sign:                                                                   | Modifier groups available for this item.                                             |
| `availability`                                                                       | [components.Availability](../../models/components/availability.md)                   | :heavy_minus_sign:                                                                   | Availability schedule for a catalog, category, or item.                              |
| `metadata`                                                                           | Record<string, *any*>                                                                | :heavy_minus_sign:                                                                   | Business-defined custom data.                                                        |