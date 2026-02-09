# DeliveryRequest

A delivery request with server-assigned metadata.

## Example Usage

```typescript
import { DeliveryRequest } from "@localprotocol/sdk/models/components";

let value: DeliveryRequest = {
  id: "<id>",
  nonce: "<value>",
  pickupLocation: {
    coordinates: {
      latitude: 1526.08,
      longitude: 5253.35,
    },
  },
  dropoffLocation: {
    coordinates: {
      latitude: 1526.08,
      longitude: 5253.35,
    },
  },
  pickupTime: new Date("2024-03-13T07:23:14.953Z"),
  dropoffTime: new Date("2024-07-19T12:46:18.015Z"),
  createdAt: new Date("2026-06-30T09:04:53.081Z"),
  status: "open",
};
```

## Fields

| Field                                                                                         | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `id`                                                                                          | *string*                                                                                      | :heavy_check_mark:                                                                            | Unique request identifier.                                                                    |
| `nonce`                                                                                       | *string*                                                                                      | :heavy_check_mark:                                                                            | Client-generated idempotency key.                                                             |
| `pickupLocation`                                                                              | *components.LocationUnion*                                                                    | :heavy_check_mark:                                                                            | A location specified by coordinates and/or postal address. At least one must be provided.     |
| `dropoffLocation`                                                                             | *components.LocationUnion*                                                                    | :heavy_check_mark:                                                                            | A location specified by coordinates and/or postal address. At least one must be provided.     |
| `pickupTime`                                                                                  | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_check_mark:                                                                            | Requested pickup time (RFC 3339).                                                             |
| `dropoffTime`                                                                                 | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_check_mark:                                                                            | Requested dropoff time (RFC 3339).                                                            |
| `pickupInstructions`                                                                          | *string*                                                                                      | :heavy_minus_sign:                                                                            | Pickup directions, access codes, or handling notes.                                           |
| `dropoffInstructions`                                                                         | *string*                                                                                      | :heavy_minus_sign:                                                                            | Dropoff directions, access codes, or delivery notes.                                          |
| `createdAt`                                                                                   | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_check_mark:                                                                            | Server-assigned creation timestamp (RFC 3339).                                                |
| `status`                                                                                      | [components.DeliveryRequestStatus](../../models/components/delivery-request-status.md)        | :heavy_check_mark:                                                                            | Request status.                                                                               |