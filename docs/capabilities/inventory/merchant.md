# Merchant

Top-level payload containing canonical catalog objects and catalogs for a merchant.

## Fields

- `id` (string, required): Merchant identifier.
- `name` (string, required): Merchant name.
- `timezone` (string, required): IANA timezone for availability schedules.
- `last_updated` (string, optional): RFC 3339 timestamp of latest catalog update.
- `catalogs` (array, required): Catalog definitions.
- `categories` (array, required): Canonical categories.
- `items` (array, required): Canonical items.
- `modifier_groups` (array, required): Canonical modifier groups.
- `modifier_options` (array, required): Canonical modifier options.
- `modifier_items` (array, required): Canonical modifier items.
- `metadata` (object, optional): Provider-specific or business-defined attributes.

## Example

```json
{
  "id": "merchant_123",
  "name": "Mesa Grill",
  "timezone": "America/Denver",
  "last_updated": "2026-02-05T18:30:00Z",
  "catalogs": [
    {
      "id": "cat_1",
      "name": "Main Menu",
      "category_ids": ["catg_1"]
    }
  ],
  "categories": [
    {
      "id": "catg_1",
      "name": "Tacos",
      "item_ids": ["item_1"]
    }
  ],
  "items": [
    {
      "id": "item_1",
      "name": "Carnitas Taco",
      "description": { "plain": "Slow-cooked pork with salsa verde." },
      "price": { "amount": "450", "currency": "USD", "decimals": 2 },
      "modifier_group_ids": ["mg_1"]
    }
  ],
  "modifier_groups": [
    {
      "id": "mg_1",
      "name": "Choose Salsa",
      "minimum_selections": 1,
      "maximum_selections": 1,
      "modifier_option_ids": ["mo_1", "mo_2"]
    }
  ],
  "modifier_options": [
    { "id": "mo_1", "modifier_item_id": "mi_1" },
    { "id": "mo_2", "modifier_item_id": "mi_2" }
  ],
  "modifier_items": [
    { "id": "mi_1", "name": "Salsa Verde", "price": { "amount": "0", "currency": "USD", "decimals": 2 } },
    { "id": "mi_2", "name": "Salsa Roja", "price": { "amount": "0", "currency": "USD", "decimals": 2 } }
  ]
}
```
