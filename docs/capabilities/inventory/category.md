# Category

Category grouping items in a catalog.

## Fields

- `id` (string, required): Category identifier.
- `name` (string, required): Category display name.
- `description` (string, optional): Category description.
- `categories` (array, optional): Ordered list of child categories for nested categories.
- `items` (array, required): Ordered list of items in this category.
- `availability` (object, optional): Category-level availability schedule. Overrides item availability unless catalog availability is defined.
- `metadata` (object, optional): Provider-specific or business-defined attributes.

Catalogs control top-level category ordering via their `categories` array.
When nested categories are used, parent categories define sibling order via their `categories` array.
Use an empty `items` list for categories that are defined but currently have no items.

## Example

```json
{
  "id": "catg_1",
  "name": "Tacos",
  "description": "Street-style tacos",
  "items": [
    {
      "id": "item_1",
      "name": "Carnitas Taco",
      "description": "Slow-cooked pork with salsa verde.",
      "price": { "value": "450", "currency": { "symbol": "USD" } }
    },
    {
      "id": "item_2",
      "name": "Veggie Taco",
      "description": "Grilled veggies with pico de gallo.",
      "price": { "value": "425", "currency": { "symbol": "USD" } }
    }
  ]
}
```
