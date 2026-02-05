# Modifier Group

Group of modifier options with selection constraints.

## Fields

- `id` (string, required): Modifier group identifier.
- `name` (string, required): Display name for the modifier group.
- `description` (string, optional): Modifier group description.
- `minimum_selections` (integer, optional): Minimum number of selections required.
- `maximum_selections` (integer, optional): Maximum number of selections allowed.
- `allow_quantities` (boolean, optional): Whether quantities greater than 1 are allowed for modifier options.
- `max_per_modifier` (integer, optional): Maximum quantity allowed per modifier option.
- `modifier_option_ids` (array, required): Ordered modifier option identifiers in this group. Order should be used for display.
- `type` (string, optional): Modifier group type classification.
- `metadata` (object, optional): Provider-specific or business-defined attributes.

## Example

```json
{
  "id": "mg_1",
  "name": "Choose Salsa",
  "minimum_selections": 1,
  "maximum_selections": 1,
  "allow_quantities": false,
  "max_per_modifier": 1,
  "modifier_option_ids": ["mo_1", "mo_2"]
}
```
