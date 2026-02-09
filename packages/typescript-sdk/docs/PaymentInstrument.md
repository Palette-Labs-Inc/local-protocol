
# PaymentInstrument

Base definition for any payment instrument.

## Properties

Name | Type
------------ | -------------
`id` | string
`handlerId` | string
`type` | string
`billingAddress` | [PostalAddress](PostalAddress.md)
`credential` | [PaymentCredential](PaymentCredential.md)
`display` | object

## Example

```typescript
import type { PaymentInstrument } from '@localprotocol/sdk'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "handlerId": null,
  "type": null,
  "billingAddress": null,
  "credential": null,
  "display": null,
} satisfies PaymentInstrument

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as PaymentInstrument
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


