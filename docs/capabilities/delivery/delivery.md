# Delivery

Delivery resource created when a bid is accepted.

## Fields

- `id` (string, required): Unique delivery identifier.
- `ask_id` (string, required): Reference to the original ask.
- `bid_id` (string, required): Reference to the accepted bid.
- `payment_instrument_id` (string, required): Reference to the payment instrument used to create this delivery.
- `created_at` (string, required): Delivery creation timestamp (RFC 3339).

## Example

```json
{
  "id": "del_789",
  "ask_id": "ask_456",
  "bid_id": "bid_123",
  "payment_instrument_id": "instr_001",
  "created_at": "2026-01-30T19:00:00Z"
}
```
