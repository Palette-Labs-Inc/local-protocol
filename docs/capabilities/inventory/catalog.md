# Catalog

Catalog grouping categories, items, and availability.

## Fields

- `id` (string, required): Catalog identifier.
- `name` (string, required): Catalog name.
- `description` (string, optional): Catalog description.
- `categories` (array, required): Ordered top-level categories included in this catalog. Nested categories live under each category's `categories` array.
- `items` (array, optional): Ordered items included directly in the catalog (not assigned to a category).
- `availability` (object, optional): Catalog-level availability schedule. Overrides category and item availability.
- `fulfillment_modes` (array, optional): Fulfillment modes supported by this catalog. Canonical values: `DELIVERY`, `PICKUP`, `DINE_IN`. Custom values are allowed.
- `metadata` (object, optional): Provider-specific or business-defined attributes.

Category ordering is defined by the `categories` array, nested category ordering is defined by each category's `categories` array, and item ordering is defined by each category's `items` array (or `items` on the catalog for uncategorized items).
When rendering or storing uncategorized items, clients should group `items` under a synthetic category (for example, "Items" or "Uncategorized") if a UI or storage layer requires category membership.

## Example

```json
{
  "id": "cat_1",
  "name": "Breakfast",
  "description": "Morning menu",
  "categories": [
    {
      "id": "catg_1",
      "name": "Tacos",
      "items": [
        {
          "id": "item_1",
          "name": "Carnitas Taco",
          "description": "Slow-cooked pork with salsa verde.",
          "price": { "value": "450", "currency": { "symbol": "USD" } }
        }
      ]
    }
  ],
  "items": [
    {
      "id": "item_9",
      "name": "Fresh OJ",
      "description": "House-pressed orange juice.",
      "price": { "value": "300", "currency": { "symbol": "USD" } }
    }
  ],
  "availability": {
    "intervals": [
      { "day": "Saturday", "from_hour": 8, "from_minute": 0, "to_hour": 14, "to_minute": 0 }
    ]
  },
  "fulfillment_modes": ["PICKUP", "DELIVERY"],
  "metadata": { "source": "pos" }
}
```
