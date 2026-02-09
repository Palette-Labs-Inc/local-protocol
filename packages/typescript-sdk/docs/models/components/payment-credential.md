# PaymentCredential

Base definition for any payment credential.

## Example Usage

```typescript
import { PaymentCredential } from "@localprotocol/sdk/models/components";

let value: PaymentCredential = {
  type: "<value>",
};
```

## Fields

| Field                          | Type                           | Required                       | Description                    |
| ------------------------------ | ------------------------------ | ------------------------------ | ------------------------------ |
| `type`                         | *string*                       | :heavy_check_mark:             | Credential type discriminator. |
| `additionalProperties`         | Record<string, *any*>          | :heavy_minus_sign:             | N/A                            |