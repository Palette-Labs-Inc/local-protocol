# Menu View

Presentation-only menu tree for a catalog. Menu view availability takes precedence over item availability.

## Fields

- `id` (string, required): Menu view identifier.
- `name` (string, required): Menu view name.
- `description` (string, optional): Menu view description.
- `catalog_id` (string, required): Catalog identifier this menu view presents.
- `availability` (object, optional): Menu-level availability schedule.
- `tree` (array, required): Root menu nodes (groups or item references).
- `external_ids` (array, optional): Provider identifiers for this menu view.
- `metadata` (object, optional): Provider-specific or business-defined attributes.

## Example

```json
{
  "id": "mv_1",
  "name": "Dinner Menu",
  "catalog_id": "cat_1",
  "availability": {
    "timezone": "America/Denver",
    "intervals": [
      { "day": "Monday", "from_hour": 16, "from_minute": 0, "to_hour": 21, "to_minute": 0 }
    ]
  },
  "tree": [
    {
      "type": "group",
      "id": "grp_1",
      "name": "Entrees",
      "children": [
        { "type": "item", "item_id": "item_1" },
        { "type": "item", "item_id": "item_2" }
      ]
    }
  ]
}
```
