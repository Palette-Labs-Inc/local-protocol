# Modifier Option

Selectable option within a modifier group that references a modifier item.

Modifier options are separated from modifier items so that:
- The same purchasable modifier item (price/name/media) can be reused across multiple groups or contexts.
- Groups can control option ordering, defaults, and nested follow-on groups without duplicating the item data.
- POS models (e.g., Square) map cleanly: option nodes reference modifier items rather than embedding them.

## Fields

- `id` (string, required): Modifier option identifier.
- `modifier_item_id` (string, required): Modifier item identifier for this option.
- `child_modifier_group_ids` (array, optional): Nested modifier group identifiers required after selecting this option.
- `is_default` (boolean, optional): Whether this option is selected by default.
- `metadata` (object, optional): Provider-specific or business-defined attributes.

## Example

```json
{
  "id": "mo_1",
  "modifier_item_id": "mi_1",
  "is_default": true,
  "child_modifier_group_ids": ["mg_2"]
}
```
