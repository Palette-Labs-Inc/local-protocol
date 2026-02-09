# CatalogCategory

A category grouping items in a catalog.

## Example Usage

```typescript
import { CatalogCategory } from "@localprotocol/sdk/models/components";

let value: CatalogCategory = {
  id: "<id>",
  name: "<value>",
  items: [
    {
      id: "<id>",
      name: "<value>",
      description: "willing reproachfully brr yippee outside phooey",
      price: {
        value: "<value>",
        currency: {
          chainId: 793765,
          address: "9303 Belmont Road",
          decimals: 989280,
        },
      },
    },
  ],
};
```

## Fields

| Field                                                                       | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `id`                                                                        | *string*                                                                    | :heavy_check_mark:                                                          | Category identifier.                                                        |
| `name`                                                                      | *string*                                                                    | :heavy_check_mark:                                                          | Category display name.                                                      |
| `description`                                                               | *string*                                                                    | :heavy_minus_sign:                                                          | Optional category description.                                              |
| `categories`                                                                | [components.CatalogCategory](../../models/components/catalog-category.md)[] | :heavy_minus_sign:                                                          | Ordered child categories for nested category trees.                         |
| `items`                                                                     | [components.CatalogItem](../../models/components/catalog-item.md)[]         | :heavy_check_mark:                                                          | Ordered items in this category.                                             |
| `availability`                                                              | [components.Availability](../../models/components/availability.md)          | :heavy_minus_sign:                                                          | Availability schedule for a catalog, category, or item.                     |
| `metadata`                                                                  | Record<string, *any*>                                                       | :heavy_minus_sign:                                                          | Business-defined custom data.                                               |