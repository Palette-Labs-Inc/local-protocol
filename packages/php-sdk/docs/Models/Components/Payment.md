# Payment

Payment configuration containing instruments.


## Fields

| Field                                                                                               | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `instruments`                                                                                       | array<[Components\SelectedPaymentInstrument](../../Models/Components/SelectedPaymentInstrument.md)> | :heavy_minus_sign:                                                                                  | Payment instruments available. Each instrument is associated with a handler via handler_id.         |