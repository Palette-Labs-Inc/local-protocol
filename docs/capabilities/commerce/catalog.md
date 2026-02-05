# Catalog

Canonical catalog grouping categories, items, and associated menu views.

## Fields

- `id` (string, required): Catalog identifier.
- `name` (string, required): Catalog name.
- `description` (string, optional): Catalog description.
- `category_ids` (array, required): Category identifiers included in this catalog.
- `item_ids` (array, optional): Item identifiers included directly in the catalog (not assigned to a category).
- `fulfillment_modes` (array, optional): Fulfillment modes supported by this catalog.
- `menu_view_ids` (array, optional): Menu view identifiers associated with this catalog.
- `external_ids` (array, optional): Provider identifiers for this catalog.
- `metadata` (object, optional): Provider-specific or business-defined attributes.

## Example

```json
{
  "id": "cat_1",
  "name": "Breakfast",
  "description": "Morning menu",
  "category_ids": ["catg_1", "catg_2"],
  "item_ids": ["item_9"],
  "fulfillment_modes": ["PICKUP", "DELIVERY"],
  "menu_view_ids": ["mv_breakfast"]
}
```
