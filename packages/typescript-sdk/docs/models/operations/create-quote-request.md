# CreateQuoteRequest

## Example Usage

```typescript
import { CreateQuoteRequest } from "@localprotocol/sdk/models/operations";

let value: CreateQuoteRequest = {
  requestId: "<id>",
  body: {
    id: "<id>",
    nonce: "<value>",
    price: 35096,
    currency: "Brazilian Real",
    pickupLocation: {
      postalAddress: {},
    },
    dropoffLocation: {
      postalAddress: {},
    },
    pickupEstimate: new Date("2025-02-19T23:42:47.679Z"),
    dropoffEstimate: new Date("2025-07-01T19:01:21.228Z"),
    payment: {},
  },
};
```

## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `requestId`                                                                        | *string*                                                                           | :heavy_check_mark:                                                                 | Delivery request identifier.                                                       |
| `body`                                                                             | [components.DeliveryQuoteCreate](../../models/components/delivery-quote-create.md) | :heavy_check_mark:                                                                 | N/A                                                                                |