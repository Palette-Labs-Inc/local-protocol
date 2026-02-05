# Modifier Item

Purchasable modifier item used by one or more modifier options.

## Fields

- `id` (string, required): Modifier item identifier.
- `name` (string, required): Modifier item name.
- `description` (string, optional): Modifier item description.
- `price` (object, required): Price in minor units with currency.
- `metadata` (object, optional): Provider-specific or business-defined attributes.

## Example

```json
{
  "id": "mi_1",
  "name": "Salsa Verde",
  "price": { "amount": 0, "currency": "USD" }
}
```
