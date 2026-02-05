# Catalog

Canonical catalog grouping categories, items, and availability.

## Fields

- `id` (string, required): Catalog identifier.
- `name` (string, required): Catalog name.
- `description` (string, optional): Catalog description.
- `category_ids` (array, required): Ordered top-level category identifiers included in this catalog (empty if uncategorized). Nested categories are referenced by parent categories via `child_category_ids`.
- `item_ids` (array, optional): Ordered item identifiers included directly in the catalog (not assigned to a category).
- `availability` (object, optional): Catalog-level availability schedule. Overrides category and item availability.
- `fulfillment_modes` (array, optional): Fulfillment modes supported by this catalog.
- `metadata` (object, optional): Provider-specific or business-defined attributes.

Category ordering is defined by `category_ids`, nested category ordering is defined by parent `child_category_ids`, and item ordering is defined by each category's `item_ids` (or `item_ids` on the catalog for uncategorized items).
When rendering or storing uncategorized items, clients should group `item_ids` under a synthetic category (for example, "Items" or "Uncategorized") if a UI or storage layer requires category membership.

## Example

```json
{
  "id": "cat_1",
  "name": "Breakfast",
  "description": "Morning menu",
  "category_ids": ["catg_1", "catg_2"],
  "item_ids": ["item_9"],
  "availability": {
    "intervals": [
      { "day": "Saturday", "from_hour": 8, "from_minute": 0, "to_hour": 14, "to_minute": 0 }
    ]
  },
  "fulfillment_modes": ["PICKUP", "DELIVERY"],
  "metadata": { "source": "pos" }
}
```
