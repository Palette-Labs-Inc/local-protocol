# Item

Canonical menu item with modifier group references.

## Fields

- `id` (string, required): Item identifier.
- `name` (string, required): Item name.
- `description` (object, required): Item description in one or more formats.
- `price` (object, required): Base price in minor units with currency.
- `media` (array, optional): Item media.
- `modifier_group_ids` (array, optional): Modifier group identifiers available for this item.
- `modifier_group_overrides` (array, optional): Item-level overrides for modifier groups (selection constraints, quantities, and option ordering/availability).
- `availability` (object, optional): Item-level availability schedule. Overrides are ignored when the catalog or category defines availability.
- `metadata` (object, optional): Provider-specific or business-defined attributes.

## Example

```json
{
  "id": "item_1",
  "name": "Carnitas Taco",
  "description": { "plain": "Slow-cooked pork with salsa verde." },
  "price": { "amount": 450, "currency": "USD" },
  "modifier_group_ids": ["mg_1"],
  "availability": {
    "intervals": [
      { "day": "Friday", "from_hour": 11, "from_minute": 0, "to_hour": 22, "to_minute": 0 }
    ]
  }
}
```
