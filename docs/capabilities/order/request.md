# Order Request

Order request posted by a requester.

## Fields

- `id` (string, required): Unique request identifier.
- `intent_id` (string, required): Shared intent identifier for tracing Request → Quote → Order.
- `nonce` (string, required): Client-generated idempotency key.

## Example

```json
{
  "id": "request_456",
  "intent_id": "intent_001",
  "nonce": "request-nonce-456"
}
```
