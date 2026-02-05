# Category

Canonical category grouping items in a catalog.

## Fields

- `id` (string, required): Category identifier.
- `name` (string, required): Category display name.
- `description` (string, optional): Category description.
- `parent_category_id` (string, optional): Parent category identifier for nested categories.
- `item_ids` (array, required): Ordered list of item identifiers in this category.
- `metadata` (object, optional): Provider-specific or business-defined attributes.

Catalogs control category ordering via their `category_ids` list.
Use an empty `item_ids` list for categories that are defined but currently have no items.

## Example

```json
{
  "id": "catg_1",
  "name": "Tacos",
  "description": "Street-style tacos",
  "item_ids": ["item_1", "item_2"]
}
```
