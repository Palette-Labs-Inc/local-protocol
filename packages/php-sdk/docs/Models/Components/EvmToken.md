# EvmToken

EVM token identifier used for auth/capture settlement.


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `address`                                            | *?string*                                            | :heavy_minus_sign:                                   | ERC-20 contract address. Omit for native gas tokens. |
| `symbol`                                             | *string*                                             | :heavy_check_mark:                                   | Token symbol (e.g., USDC).                           |
| `decimals`                                           | *int*                                                | :heavy_check_mark:                                   | Token decimals.                                      |