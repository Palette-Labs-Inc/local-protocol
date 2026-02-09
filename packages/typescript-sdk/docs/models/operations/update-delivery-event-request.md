# UpdateDeliveryEventRequest

## Example Usage

```typescript
import { UpdateDeliveryEventRequest } from "@localprotocol/sdk/models/operations";

let value: UpdateDeliveryEventRequest = {
  deliveryId: "<id>",
  body: {
    event: "<value>",
    eventDescription: "<value>",
  },
};
```

## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `deliveryId`                                                                     | *string*                                                                         | :heavy_check_mark:                                                               | Delivery identifier.                                                             |
| `body`                                                                           | [components.UpdateEventRequest](../../models/components/update-event-request.md) | :heavy_check_mark:                                                               | N/A                                                                              |