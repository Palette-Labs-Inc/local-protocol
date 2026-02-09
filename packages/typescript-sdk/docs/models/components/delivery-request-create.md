# DeliveryRequestCreate

Body for creating a delivery request.

## Example Usage

```typescript
import { DeliveryRequestCreate } from "@localprotocol/sdk/models/components";

let value: DeliveryRequestCreate = {
  id: "<id>",
  nonce: "<value>",
  pickupLocation: {
    coordinates: {
      latitude: 1526.08,
      longitude: 5253.35,
    },
  },
  dropoffLocation: {
    postalAddress: {},
  },
  pickupTime: new Date("2025-10-03T13:17:04.168Z"),
  dropoffTime: new Date("2025-07-03T18:38:15.767Z"),
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