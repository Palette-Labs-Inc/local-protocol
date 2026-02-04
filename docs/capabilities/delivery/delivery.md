# Delivery

Delivery resource created when a quote is accepted.

## Fields

- `id` (string, required): Unique delivery identifier.
- `request_id` (string, required): Reference to the original request.
- `quote_id` (string, required): Reference to the accepted quote.
- `payment_instrument_id` (string, required): Reference to the payment instrument used to create this delivery.
- `created_at` (string, required): Delivery creation timestamp (RFC 3339).

## Example

```json
{
  "id": "del_789",
  "request_id": "request_456",
  "quote_id": "quote_123",
  "payment_instrument_id": "instr_001",
  "created_at": "2026-01-30T19:00:00Z"
}
```
