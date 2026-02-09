# Catalog

A catalog containing embedded categories, items, availability, and fulfillment configuration.

## Example Usage

```typescript
import { Catalog } from "@localprotocol/sdk/models/components";

let value: Catalog = {
  id: "<id>",
  name: "<value>",
  categories: [],
};
```

## Fields

| Field                                                                       | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `id`                                                                        | *string*                                                                    | :heavy_check_mark:                                                          | Catalog identifier.                                                         |
| `name`                                                                      | *string*                                                                    | :heavy_check_mark:                                                          | Catalog name.                                                               |
| `description`                                                               | *string*                                                                    | :heavy_minus_sign:                                                          | Catalog description.                                                        |
| `categories`                                                                | [components.CatalogCategory](../../models/components/catalog-category.md)[] | :heavy_check_mark:                                                          | Ordered top-level categories.                                               |
| `items`                                                                     | [components.CatalogItem](../../models/components/catalog-item.md)[]         | :heavy_minus_sign:                                                          | Items not assigned to a category.                                           |
| `availability`                                                              | [components.Availability](../../models/components/availability.md)          | :heavy_minus_sign:                                                          | Availability schedule for a catalog, category, or item.                     |
| `metadata`                                                                  | Record<string, *any*>                                                       | :heavy_minus_sign:                                                          | Business-defined custom data.                                               |