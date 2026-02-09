# OrderQuote

An order quote.

## Example Usage

```typescript
import { OrderQuote } from "@localprotocol/sdk/models/components";

let value: OrderQuote = {
  id: "<id>",
  intentId: "<id>",
  nonce: "<value>",
  price: 545942,
  readyAt: new Date("2024-12-16T18:55:56.382Z"),
  expiresAt: new Date("2026-02-13T15:05:36.476Z"),
};
```

## Fields

| Field                                                                                         | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `id`                                                                                          | *string*                                                                                      | :heavy_check_mark:                                                                            | Unique quote identifier.                                                                      |
| `intentId`                                                                                    | *string*                                                                                      | :heavy_check_mark:                                                                            | Shared intent identifier for tracing Request -> Quote -> Order.                               |
| `nonce`                                                                                       | *string*                                                                                      | :heavy_check_mark:                                                                            | Client-generated idempotency key.                                                             |
| `price`                                                                                       | *number*                                                                                      | :heavy_check_mark:                                                                            | Price in minor currency units.                                                                |
| `readyAt`                                                                                     | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_check_mark:                                                                            | Estimated readiness time (RFC 3339).                                                          |
| `expiresAt`                                                                                   | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_check_mark:                                                                            | Quote expiration time (RFC 3339).                                                             |