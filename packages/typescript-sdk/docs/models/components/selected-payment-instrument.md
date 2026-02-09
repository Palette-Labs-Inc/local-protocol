# SelectedPaymentInstrument

A payment instrument with selection state.

## Example Usage

```typescript
import { SelectedPaymentInstrument } from "@localprotocol/sdk/models/components";

let value: SelectedPaymentInstrument = {
  id: "<id>",
  handlerId: "<id>",
  type: "<value>",
};
```

## Fields

| Field                                                                                                         | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                          | *string*                                                                                                      | :heavy_check_mark:                                                                                            | Unique instrument identifier.                                                                                 |
| `handlerId`                                                                                                   | *string*                                                                                                      | :heavy_check_mark:                                                                                            | Handler instance identifier.                                                                                  |
| `type`                                                                                                        | *string*                                                                                                      | :heavy_check_mark:                                                                                            | Instrument category (e.g., 'card', 'tokenized_card').                                                         |
| `billingAddress`                                                                                              | [components.PostalAddress](../../models/components/postal-address.md)                                         | :heavy_minus_sign:                                                                                            | N/A                                                                                                           |
| `credential`                                                                                                  | [components.PaymentCredential](../../models/components/payment-credential.md)                                 | :heavy_minus_sign:                                                                                            | Base definition for any payment credential.                                                                   |
| `display`                                                                                                     | [components.SelectedPaymentInstrumentDisplay](../../models/components/selected-payment-instrument-display.md) | :heavy_minus_sign:                                                                                            | Display information for the instrument.                                                                       |
| `selected`                                                                                                    | *boolean*                                                                                                     | :heavy_minus_sign:                                                                                            | Whether this instrument is selected by the user.                                                              |
| `additionalProperties`                                                                                        | Record<string, *any*>                                                                                         | :heavy_minus_sign:                                                                                            | N/A                                                                                                           |