# Item

Menu item with embedded modifier groups.

## Fields

- `id` (string, required): Item identifier.
- `name` (string, required): Item name.
- `description` (string, required): Item description.
- `price` (object, required): Base price in minor units with currency (see [Amount](../../shared/amount.md)).
- `media` (array, optional): Optional array of Media objects (see [Media](../../shared/media.md); schema: `schemas/shared/media.json`).
- `modifier_groups` (array, optional): Modifier groups available for this item.
- `availability` (object, optional): Item-level availability schedule; if a catalog or category defines availability, the item-level availability is ignored.
- `metadata` (object, optional): Provider-specific or business-defined attributes.

## Example

```json
{
  "id": "item_1",
  "name": "Carnitas Taco",
  "description": "Slow-cooked pork with salsa verde.",
  "price": { "value": "450", "currency": { "symbol": "USD" } },
  "modifier_groups": [
    {
      "id": "mg_1",
      "name": "Choose Salsa",
      "minimum_selections": 1,
      "maximum_selections": 2,
      "modifier_options": [
        {
          "id": "mo_1",
          "modifier_item": {
            "id": "mi_1",
            "name": "Salsa Verde",
            "price": { "value": "0", "currency": { "symbol": "USD" } }
          }
        },
        {
          "id": "mo_2",
          "modifier_item": {
            "id": "mi_2",
            "name": "Salsa Roja",
            "price": { "value": "0", "currency": { "symbol": "USD" } }
          }
        }
      ]
    }
  ],
  "availability": {
    "intervals": [
      { "day": "Friday", "from_hour": 11, "from_minute": 0, "to_hour": 22, "to_minute": 0 }
    ]
  }
}
```
