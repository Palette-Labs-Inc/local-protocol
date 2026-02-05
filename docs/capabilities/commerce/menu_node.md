# Menu Node

Union type for nodes in a menu tree. A node is either a `menu_group` or a `menu_item_ref`.

## Example

```json
{ "type": "group", "id": "grp_1", "name": "Tacos", "children": [{ "type": "item", "item_id": "item_1" }] }
```

```json
{ "type": "item", "item_id": "item_1" }
```
