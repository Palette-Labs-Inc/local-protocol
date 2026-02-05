# Menu Item Reference

Presentation-only reference to a canonical item in a menu tree.

## Fields

- `type` (string, required): Node type discriminator. Always `item`.
- `item_id` (string, required): Referenced item identifier.
- `sort_order` (integer, optional): Sort order for display.
- `external_ids` (array, optional): Provider identifiers for this menu node.
- `metadata` (object, optional): Provider-specific or business-defined attributes.

## Example

```json
{
  "type": "item",
  "item_id": "item_1",
  "sort_order": 5
}
```
