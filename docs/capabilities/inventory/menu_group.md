# Menu Group

Presentation-only grouping within a menu tree.

## Fields

- `type` (string, required): Node type discriminator. Always `group`.
- `id` (string, required): Menu group identifier.
- `name` (string, required): Group display name.
- `description` (string, optional): Group description.
- `children` (array, required): Child menu nodes (groups or item references).
- `sort_order` (integer, optional): Sort order for display.
- `category_id` (string, optional): Optional link to a canonical category.
- `metadata` (object, optional): Provider-specific or business-defined attributes.

## Example

```json
{
  "type": "group",
  "id": "grp_1",
  "name": "Tacos",
  "children": [
    { "type": "item", "item_id": "item_1" },
    { "type": "item", "item_id": "item_2" }
  ]
}
```
