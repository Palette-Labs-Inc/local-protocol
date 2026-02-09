# DeliveryQuote

A delivery quote with server-assigned metadata.

## Example Usage

```typescript
import { DeliveryQuote } from "@localprotocol/sdk/models/components";

let value: DeliveryQuote = {
  id: "<id>",
  nonce: "<value>",
  price: 103613,
  currency: "US Dollar",
  pickupLocation: {
    postalAddress: {},
  },
  dropoffLocation: {
    coordinates: {
      latitude: 1526.08,
      longitude: 5253.35,
    },
  },
  pickupEstimate: new Date("2025-04-16T07:08:16.928Z"),
  dropoffEstimate: new Date("2025-12-11T21:27:13.627Z"),
  payment: {},
  requestId: "<id>",
  createdAt: new Date("2026-09-09T08:17:33.069Z"),
  status: "pending",
};
```

## Fields

| Field                                                                                         | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `id`                                                                                          | *string*                                                                                      | :heavy_check_mark:                                                                            | Unique quote identifier.                                                                      |
| `nonce`                                                                                       | *string*                                                                                      | :heavy_check_mark:                                                                            | Client-generated idempotency key.                                                             |
| `price`                                                                                       | *number*                                                                                      | :heavy_check_mark:                                                                            | Price in minor currency units.                                                                |
| `currency`                                                                                    | *string*                                                                                      | :heavy_check_mark:                                                                            | ISO 4217 currency code.                                                                       |
| `pickupLocation`                                                                              | *components.LocationUnion*                                                                    | :heavy_check_mark:                                                                            | A location specified by coordinates and/or postal address. At least one must be provided.     |
| `dropoffLocation`                                                                             | *components.LocationUnion*                                                                    | :heavy_check_mark:                                                                            | A location specified by coordinates and/or postal address. At least one must be provided.     |
| `pickupEstimate`                                                                              | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_check_mark:                                                                            | Estimated pickup time (RFC 3339).                                                             |
| `dropoffEstimate`                                                                             | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_check_mark:                                                                            | Estimated dropoff time (RFC 3339).                                                            |
| `expiresAt`                                                                                   | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_minus_sign:                                                                            | Time when the quote expires (RFC 3339).                                                       |
| `payment`                                                                                     | [components.Payment](../../models/components/payment.md)                                      | :heavy_check_mark:                                                                            | Payment configuration containing instruments.                                                 |
| `requestId`                                                                                   | *string*                                                                                      | :heavy_check_mark:                                                                            | Reference to the parent delivery request.                                                     |
| `createdAt`                                                                                   | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_check_mark:                                                                            | Server-assigned creation timestamp (RFC 3339).                                                |
| `status`                                                                                      | [components.DeliveryQuoteStatus](../../models/components/delivery-quote-status.md)            | :heavy_check_mark:                                                                            | Quote status.                                                                                 |