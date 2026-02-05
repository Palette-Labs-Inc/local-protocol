# Modifier Group Override

Item-specific overrides for a modifier group.

## Fields

- `modifier_group_id` (string, required): Modifier group identifier being overridden.
- `minimum_selections` (integer, optional): Minimum number of selections required for this item.
- `maximum_selections` (integer, optional): Maximum number of selections allowed for this item.
- `allow_quantities` (boolean, optional): Whether quantities greater than 1 are allowed for this item.
- `max_per_modifier` (integer, optional): Maximum quantity allowed per modifier option for this item.
- `modifier_option_ids` (array, optional): Ordered subset of modifier options available for this item.
- `metadata` (object, optional): Provider-specific or business-defined attributes.

## Example

```json
{
  "modifier_group_id": "mg_1",
  "minimum_selections": 1,
  "maximum_selections": 2,
  "allow_quantities": true,
  "max_per_modifier": 3,
  "modifier_option_ids": ["mo_2", "mo_1"]
}
```
