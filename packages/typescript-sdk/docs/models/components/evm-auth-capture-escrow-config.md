# EvmAuthCaptureEscrowConfig

Handler configuration for auth/capture escrow on EVM chains.

## Example Usage

```typescript
import { EvmAuthCaptureEscrowConfig } from "@localprotocol/sdk/models/components";

let value: EvmAuthCaptureEscrowConfig = {
  chainId: 938971,
  contract: "<value>",
  operator: "<value>",
  receiver: "<value>",
  acceptedTokens: [],
};
```

## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `chainId`                                                     | *number*                                                      | :heavy_check_mark:                                            | EVM chain id for the escrow contract.                         |
| `contract`                                                    | *string*                                                      | :heavy_check_mark:                                            | Escrow contract address.                                      |
| `operator`                                                    | *string*                                                      | :heavy_check_mark:                                            | Operator address for state transitions.                       |
| `receiver`                                                    | *string*                                                      | :heavy_check_mark:                                            | Default receiver address for captures.                        |
| `acceptedTokens`                                              | [components.EvmToken](../../models/components/evm-token.md)[] | :heavy_check_mark:                                            | Tokens accepted on the escrow contract chain.                 |
| `additionalProperties`                                        | Record<string, *any*>                                         | :heavy_minus_sign:                                            | N/A                                                           |