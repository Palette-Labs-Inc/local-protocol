# EvmToken

EVM token identifier used for auth/capture settlement.

## Example Usage

```typescript
import { EvmToken } from "@localprotocol/sdk/models/components";

let value: EvmToken = {
  symbol: "<value>",
  decimals: 576599,
};
```

## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `address`                                            | *string*                                             | :heavy_minus_sign:                                   | ERC-20 contract address. Omit for native gas tokens. |
| `symbol`                                             | *string*                                             | :heavy_check_mark:                                   | Token symbol (e.g., USDC).                           |
| `decimals`                                           | *number*                                             | :heavy_check_mark:                                   | Token decimals.                                      |