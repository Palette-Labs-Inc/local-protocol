# Modifier Option

Selectable option within a modifier group that embeds a modifier item.

## Fields

- `id` (string, required): Modifier option identifier.
- `modifier_item` (object, required): Modifier item for this option.
- `child_modifier_groups` (array, optional): Nested modifier groups required after selecting this option.
- `is_default` (boolean, optional): Whether this option is selected by default.
- `metadata` (object, optional): Provider-specific or business-defined attributes.

## Example

```json
{
  "id": "mo_1",
  "modifier_item": {
    "id": "mi_1",
    "name": "Salsa Verde",
    "price": { "value": "0", "currency": { "symbol": "USD" } }
  },
  "is_default": true,
  "child_modifier_groups": [
    {
      "id": "mg_2",
      "name": "Heat Level",
      "minimum_selections": 1,
      "maximum_selections": 1,
      "modifier_options": [
        {
          "id": "mo_3",
          "modifier_item": {
            "id": "mi_3",
            "name": "Mild",
            "price": { "value": "0", "currency": { "symbol": "USD" } }
          }
        }
      ]
    }
  ]
}
```
