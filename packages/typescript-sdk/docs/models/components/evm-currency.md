# EvmCurrency

EVM token currency descriptor.

## Example Usage

```typescript
import { EvmCurrency } from "@localprotocol/sdk/models/components";

let value: EvmCurrency = {
  chainId: 944542,
  address: "27056 Mills Wall",
  decimals: 924120,
};
```

## Fields

| Field                         | Type                          | Required                      | Description                   |
| ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| `chainId`                     | *number*                      | :heavy_check_mark:            | EVM chain id.                 |
| `address`                     | *string*                      | :heavy_check_mark:            | Token contract address.       |
| `decimals`                    | *number*                      | :heavy_check_mark:            | Decimal places for the token. |