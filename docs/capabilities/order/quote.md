# Order Quote

Order quote offered by a provider, including price and readiness timing.

## Fields

- `id` (string, required): Unique quote identifier.
- `intent_id` (string, required): Shared intent identifier for tracing Request → Quote → Order.
- `nonce` (string, required): Client-generated idempotency key.
- `price` (integer, required): Price in minor currency units.
- `ready_at` (string, required): Estimated readiness time (RFC 3339).
- `expires_at` (string, required): Quote expiration time (RFC 3339).

## Example

```json
{
  "id": "quote_123",
  "intent_id": "intent_001",
  "nonce": "quote-nonce-123",
  "price": 1299,
  "ready_at": "2026-02-05T19:15:00Z",
  "expires_at": "2026-02-05T19:30:00Z"
}
```
