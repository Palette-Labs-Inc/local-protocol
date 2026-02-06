# Merchant

Top-level payload containing denormalized catalogs for a merchant.

## Fields

- `id` (string, required): Merchant identifier.
- `name` (string, required): Merchant name.
- `timezone` (string, required): IANA timezone for availability schedules.
- `last_updated` (string, optional): RFC 3339 timestamp of latest catalog update.
- `catalogs` (array, required): Catalog definitions with embedded categories/items/modifiers.
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
      "categories": [
        {
          "id": "catg_1",
          "name": "Tacos",
          "items": [
            {
              "id": "item_1",
              "name": "Carnitas Taco",
              "description": "Slow-cooked pork with salsa verde.",
              "price": { "value": "450", "currency": { "symbol": "USD" } },
              "modifier_groups": [
                {
                  "id": "mg_1",
                  "name": "Choose Salsa",
                  "minimum_selections": 1,
                  "maximum_selections": 1,
                  "modifier_options": [
                    {
                      "id": "mo_1",
                      "modifier_item": {
                        "id": "mi_1",
                        "name": "Salsa Verde",
                        "price": { "value": "0", "currency": { "symbol": "USD" } }
                      }
                    },
                    {
                      "id": "mo_2",
                      "modifier_item": {
                        "id": "mi_2",
                        "name": "Salsa Roja",
                        "price": { "value": "0", "currency": { "symbol": "USD" } }
                      }
                    }
                  ]
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}
```
