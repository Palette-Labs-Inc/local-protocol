# Merchant

Top-level payload containing denormalized catalogs for a merchant.

## Fields

- `id` (string, required): Merchant identifier.
- `name` (string, required): Merchant name.
- `timezone` (string, required): IANA timezone for availability schedules.
- `last_updated` (string, optional): RFC 3339 timestamp of latest catalog update.
- `cover_image` (object, optional): Merchant cover image using the shared `Media` schema.
- `logo` (object, optional): Merchant logo image using the shared `Media` schema.
- `coordinates` (object, optional): Merchant latitude/longitude coordinates.
- `postal_address` (object, optional): Merchant postal address using the UCP `postal_address` schema.
- `phone_number` (string, optional): Merchant contact phone number.
- `email` (string, optional): Merchant contact email address.
- `catalogs` (array, required): Catalog definitions with embedded categories/items/modifiers.
- `metadata` (object, optional): Provider-specific or business-defined attributes.

## Example

```json
{
  "id": "merchant_123",
  "name": "Mesa Grill",
  "timezone": "America/Denver",
  "last_updated": "2026-02-05T18:30:00Z",
  "cover_image": {
    "type": "image",
    "url": "https://cdn.example.com/merchants/merchant_123/cover.jpg"
  },
  "logo": {
    "type": "image",
    "url": "https://cdn.example.com/merchants/merchant_123/logo.png"
  },
  "coordinates": {
    "latitude": 40.5853,
    "longitude": -105.0844
  },
  "postal_address": {
    "street_address": "123 Main St",
    "address_locality": "Fort Collins",
    "address_region": "CO",
    "postal_code": "80524",
    "address_country": "US"
  },
  "phone_number": "+1-970-555-0100",
  "email": "hello@mesagrill.example",
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
