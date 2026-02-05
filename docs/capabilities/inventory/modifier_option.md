# Modifier Option

Selectable option within a modifier group that references a modifier item.

## Fields

- `id` (string, required): Modifier option identifier.
- `modifier_item_id` (string, required): Modifier item identifier for this option.
- `child_modifier_group_ids` (array, optional): Nested modifier group identifiers required after selecting this option.
- `is_default` (boolean, optional): Whether this option is selected by default.
- `sort_order` (integer, optional): Sort order for option display.
- `metadata` (object, optional): Provider-specific or business-defined attributes.

## Example

```json
{
  "id": "mo_1",
  "modifier_item_id": "mi_1",
  "is_default": true,
  "sort_order": 10,
  "child_modifier_group_ids": ["mg_2"]
}
```
