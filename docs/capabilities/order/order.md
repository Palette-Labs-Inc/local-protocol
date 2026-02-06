# Order

Order resource created when a quote is accepted and payment is provided.

## Fields

- `id` (string, required): Unique order identifier.
- `intent_id` (string, required): Shared intent identifier for tracing Request → Quote → Order.
- `nonce` (string, required): Client-generated idempotency key.
- `payment_instrument_id` (string, required): Reference to the payment instrument used to create this order.

## Example

```json
{
  "id": "order_789",
  "intent_id": "intent_001",
  "nonce": "order-nonce-789",
  "payment_instrument_id": "instr_001"
}
```
