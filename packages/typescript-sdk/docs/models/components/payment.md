# Payment

Payment configuration containing instruments.

## Example Usage

```typescript
import { Payment } from "@localprotocol/sdk/models/components";

let value: Payment = {};
```

## Fields

| Field                                                                                            | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `instruments`                                                                                    | [components.SelectedPaymentInstrument](../../models/components/selected-payment-instrument.md)[] | :heavy_minus_sign:                                                                               | Payment instruments available. Each instrument is associated with a handler via handler_id.      |