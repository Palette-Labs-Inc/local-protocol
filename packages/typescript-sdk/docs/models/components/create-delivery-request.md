# CreateDeliveryRequest

Body for creating a delivery from an accepted quote.

## Example Usage

```typescript
import { CreateDeliveryRequest } from "@localprotocol/sdk/models/components";

let value: CreateDeliveryRequest = {
  requestId: "<id>",
  quoteId: "<id>",
  nonce: "<value>",
};
```

## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `requestId`                                                   | *string*                                                      | :heavy_check_mark:                                            | The delivery request to fulfill.                              |
| `quoteId`                                                     | *string*                                                      | :heavy_check_mark:                                            | The accepted quote.                                           |
| `nonce`                                                       | *string*                                                      | :heavy_check_mark:                                            | Client-generated idempotency key.                             |
| `webhookUrl`                                                  | *string*                                                      | :heavy_minus_sign:                                            | Optional URL to receive delivery event webhook notifications. |
| `eventVocabulary`                                             | *string*                                                      | :heavy_minus_sign:                                            | Event vocabulary standard to use.                             |