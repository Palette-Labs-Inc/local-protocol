# EvmAuthCaptureEscrowInstrumentAmount

Amount in atomic units. Currency chain_id MUST match the instrument chain_id; currency address and decimals MUST match token address and decimals.


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `value`                                                          | *string*                                                         | :heavy_check_mark:                                               | Value in minor currency units as an integer string.              |
| `currency`                                                       | [Components\EvmCurrency](../../Models/Components/EvmCurrency.md) | :heavy_check_mark:                                               | EVM token currency descriptor.                                   |