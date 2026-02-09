# DeliveryQuoteCreate

Body for creating a delivery quote.

## Example Usage

```typescript
import { DeliveryQuoteCreate } from "@localprotocol/sdk/models/components";

let value: DeliveryQuoteCreate = {
  id: "<id>",
  nonce: "<value>",
  price: 579880,
  currency: "Gibraltar Pound",
  pickupLocation: {
    coordinates: {
      latitude: 1526.08,
      longitude: 5253.35,
    },
  },
  dropoffLocation: {
    postalAddress: {},
  },
  pickupEstimate: new Date("2026-10-03T21:48:02.753Z"),
  dropoffEstimate: new Date("2025-01-15T21:06:30.676Z"),
  payment: {},
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