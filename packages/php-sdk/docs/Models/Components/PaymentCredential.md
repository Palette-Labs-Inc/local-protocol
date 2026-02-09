# PaymentCredential

Base definition for any payment credential.


## Fields

| Field                          | Type                           | Required                       | Description                    |
| ------------------------------ | ------------------------------ | ------------------------------ | ------------------------------ |
| `type`                         | *string*                       | :heavy_check_mark:             | Credential type discriminator. |
| `additionalProperties`         | array<string, *mixed*>         | :heavy_minus_sign:             | N/A                            |