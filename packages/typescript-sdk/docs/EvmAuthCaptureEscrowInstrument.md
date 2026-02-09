
# EvmAuthCaptureEscrowInstrument

Payment instrument for auth/capture escrow on EVM chains.

## Properties

Name | Type
------------ | -------------
`id` | string
`handlerId` | string
`type` | string
`billingAddress` | [PostalAddress](PostalAddress.md)
`credential` | [PaymentCredential](PaymentCredential.md)
`display` | object
`paymentInfoHash` | string
`operator` | string
`payer` | string
`chainId` | number
`contract` | string
`receiver` | string
`token` | [EvmToken](EvmToken.md)
`maxAmount` | [Amount](Amount.md)
`preapprovalExpiresAt` | Date
`authorizationExpiresAt` | Date
`refundExpiresAt` | Date
`nonce` | string
`amount` | [Amount](Amount.md)

## Example

```typescript
import type { EvmAuthCaptureEscrowInstrument } from '@localprotocol/sdk'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "handlerId": null,
  "type": null,
  "billingAddress": null,
  "credential": null,
  "display": null,
  "paymentInfoHash": null,
  "operator": null,
  "payer": null,
  "chainId": null,
  "contract": null,
  "receiver": null,
  "token": null,
  "maxAmount": null,
  "preapprovalExpiresAt": null,
  "authorizationExpiresAt": null,
  "refundExpiresAt": null,
  "nonce": null,
  "amount": null,
} satisfies EvmAuthCaptureEscrowInstrument

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as EvmAuthCaptureEscrowInstrument
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


