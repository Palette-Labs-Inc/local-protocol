
# EvmAuthCaptureEscrowInstrumentAllOfMaxAmount

Maximum amount that can be authorized (atomic units). Currency chain_id MUST match the instrument chain_id; currency address and decimals MUST match token address and decimals.

## Properties

Name | Type
------------ | -------------
`value` | string
`currency` | [EvmCurrency](EvmCurrency.md)

## Example

```typescript
import type { EvmAuthCaptureEscrowInstrumentAllOfMaxAmount } from '@localprotocol/sdk'

// TODO: Update the object below with actual values
const example = {
  "value": null,
  "currency": null,
} satisfies EvmAuthCaptureEscrowInstrumentAllOfMaxAmount

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as EvmAuthCaptureEscrowInstrumentAllOfMaxAmount
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


