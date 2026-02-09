# EvmAuthCaptureEscrowConfig

Handler configuration for auth/capture escrow on EVM chains.


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `chainId`                                                         | *int*                                                             | :heavy_check_mark:                                                | EVM chain id for the escrow contract.                             |
| `contract`                                                        | *string*                                                          | :heavy_check_mark:                                                | Escrow contract address.                                          |
| `operator`                                                        | *string*                                                          | :heavy_check_mark:                                                | Operator address for state transitions.                           |
| `receiver`                                                        | *string*                                                          | :heavy_check_mark:                                                | Default receiver address for captures.                            |
| `acceptedTokens`                                                  | array<[Components\EvmToken](../../Models/Components/EvmToken.md)> | :heavy_check_mark:                                                | Tokens accepted on the escrow contract chain.                     |
| `additionalProperties`                                            | array<string, *mixed*>                                            | :heavy_minus_sign:                                                | N/A                                                               |