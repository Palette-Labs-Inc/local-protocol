# Amount

Amount with explicit currency. Value is always in minor units (e.g., cents for USD).

## Example Usage

```typescript
import { Amount } from "@localprotocol/sdk/models/components";

let value: Amount = {
  value: "<value>",
  currency: {
    chainId: 793765,
    address: "9303 Belmont Road",
    decimals: 989280,
  },
};
```

## Fields

| Field                                               | Type                                                | Required                                            | Description                                         |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| `value`                                             | *string*                                            | :heavy_check_mark:                                  | Value in minor currency units as an integer string. |
| `currency`                                          | *components.Currency*                               | :heavy_check_mark:                                  | Currency descriptor (fiat or EVM token).            |