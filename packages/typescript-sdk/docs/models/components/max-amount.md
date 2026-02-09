# MaxAmount

Maximum amount that can be authorized (atomic units). Currency chain_id MUST match the instrument chain_id; currency address and decimals MUST match token address and decimals.

## Example Usage

```typescript
import { MaxAmount } from "@localprotocol/sdk/models/components";

let value: MaxAmount = {
  value: "<value>",
  currency: {
    chainId: 526835,
    address: "25071 Norfolk Road",
    decimals: 47904,
  },
};
```

## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `value`                                                           | *string*                                                          | :heavy_check_mark:                                                | Value in minor currency units as an integer string.               |
| `currency`                                                        | [components.EvmCurrency](../../models/components/evm-currency.md) | :heavy_check_mark:                                                | EVM token currency descriptor.                                    |