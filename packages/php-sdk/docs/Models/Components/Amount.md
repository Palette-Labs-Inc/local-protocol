# Amount

Amount with explicit currency. Value is always in minor units (e.g., cents for USD).


## Fields

| Field                                                                                 | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `value`                                                                               | *string*                                                                              | :heavy_check_mark:                                                                    | Value in minor currency units as an integer string.                                   |
| `currency`                                                                            | [Components\FiatCurrency\|Components\EvmCurrency](../../Models/Components/Currency.md) | :heavy_check_mark:                                                                    | Currency descriptor (fiat or EVM token).                                              |