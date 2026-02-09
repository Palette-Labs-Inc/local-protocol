# Delivery

A delivery resource.

## Example Usage

```typescript
import { Delivery } from "@localprotocol/sdk/models/components";

let value: Delivery = {
  id: "<id>",
  requestId: "<id>",
  quoteId: "<id>",
  paymentInstrumentId: "<id>",
  event: "<value>",
  eventDescription: "<value>",
  eventVocabulary: "<value>",
  createdAt: new Date("2024-12-07T15:03:04.400Z"),
  updatedAt: new Date("2024-09-27T23:16:34.680Z"),
};
```

## Fields

| Field                                                                                         | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `id`                                                                                          | *string*                                                                                      | :heavy_check_mark:                                                                            | Unique delivery identifier.                                                                   |
| `requestId`                                                                                   | *string*                                                                                      | :heavy_check_mark:                                                                            | Reference to the delivery request.                                                            |
| `quoteId`                                                                                     | *string*                                                                                      | :heavy_check_mark:                                                                            | Reference to the accepted quote.                                                              |
| `paymentInstrumentId`                                                                         | *string*                                                                                      | :heavy_check_mark:                                                                            | Reference to the payment instrument used to create this delivery.                             |
| `event`                                                                                       | *string*                                                                                      | :heavy_check_mark:                                                                            | Current event identifier.                                                                     |
| `eventDescription`                                                                            | *string*                                                                                      | :heavy_check_mark:                                                                            | Human-readable description of the current event.                                              |
| `eventVocabulary`                                                                             | *string*                                                                                      | :heavy_check_mark:                                                                            | Event vocabulary standard in use.                                                             |
| `webhookUrl`                                                                                  | *string*                                                                                      | :heavy_minus_sign:                                                                            | Registered webhook URL, if any.                                                               |
| `createdAt`                                                                                   | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_check_mark:                                                                            | Creation timestamp (RFC 3339).                                                                |
| `updatedAt`                                                                                   | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | :heavy_check_mark:                                                                            | Last update timestamp (RFC 3339).                                                             |