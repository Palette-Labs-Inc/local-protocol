# Category

Canonical category grouping items in a catalog.

## Fields

- `id` (string, required): Category identifier.
- `name` (string, required): Category display name.
- `description` (string, optional): Category description.
- `item_ids` (array, required): Ordered list of item identifiers in this category.
- `sort_order` (integer, optional): Sort order for category display.
- `metadata` (object, optional): Provider-specific or business-defined attributes.

## Example

```json
{
  "id": "catg_1",
  "name": "Tacos",
  "description": "Street-style tacos",
  "item_ids": ["item_1", "item_2"],
  "sort_order": 10
}
```
