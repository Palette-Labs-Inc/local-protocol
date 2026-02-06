# Cart

Cart representing a collection of items aggregated with intent to order.

## Fields

- `id` (string, required): Unique cart identifier.
- `intent_id` (string, required): Shared intent identifier for tracing Request → Quote → Order.
- `nonce` (string, required): Client-generated idempotency key.
- `items` (array, required): Array of cart items.

## Cart Item Fields

- `id` (string, required): Item identifier.
- `quantity` (integer, required): Quantity requested.

## Example

```json
{
  "id": "cart_123",
  "intent_id": "intent_001",
  "nonce": "cart-nonce-123",
  "items": [
    {
      "id": "item_abc",
      "quantity": 2
    }
  ]
}
```
