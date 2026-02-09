# GetOrderQuoteRequest

## Example Usage

```typescript
import { GetOrderQuoteRequest } from "@localprotocol/sdk/models/operations";

let value: GetOrderQuoteRequest = {
  orderRequestId: "<id>",
  orderQuoteId: "<id>",
};
```

## Fields

| Field                     | Type                      | Required                  | Description               |
| ------------------------- | ------------------------- | ------------------------- | ------------------------- |
| `orderRequestId`          | *string*                  | :heavy_check_mark:        | Order request identifier. |
| `orderQuoteId`            | *string*                  | :heavy_check_mark:        | Order quote identifier.   |