# FiatCurrency

Fiat currency descriptor.

## Example Usage

```typescript
import { FiatCurrency } from "@localprotocol/sdk/models/components";

let value: FiatCurrency = {
  symbol: "<value>",
};
```

## Fields

| Field                                               | Type                                                | Required                                            | Description                                         |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| `symbol`                                            | *string*                                            | :heavy_check_mark:                                  | ISO 4217 currency code (e.g., 'USD', 'EUR', 'JPY'). |