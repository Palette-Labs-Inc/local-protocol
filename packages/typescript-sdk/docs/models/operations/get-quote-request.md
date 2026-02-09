# GetQuoteRequest

## Example Usage

```typescript
import { GetQuoteRequest } from "@localprotocol/sdk/models/operations";

let value: GetQuoteRequest = {
  requestId: "<id>",
  quoteId: "<id>",
};
```

## Fields

| Field                        | Type                         | Required                     | Description                  |
| ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- |
| `requestId`                  | *string*                     | :heavy_check_mark:           | Delivery request identifier. |
| `quoteId`                    | *string*                     | :heavy_check_mark:           | Quote identifier.            |