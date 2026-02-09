
# EvmAuthCaptureEscrowConfig

Handler configuration for auth/capture escrow on EVM chains.

## Properties

Name | Type
------------ | -------------
`chainId` | number
`contract` | string
`operator` | string
`receiver` | string
`acceptedTokens` | [Array&lt;EvmToken&gt;](EvmToken.md)

## Example

```typescript
import type { EvmAuthCaptureEscrowConfig } from '@localprotocol/sdk'

// TODO: Update the object below with actual values
const example = {
  "chainId": null,
  "contract": null,
  "operator": null,
  "receiver": null,
  "acceptedTokens": null,
} satisfies EvmAuthCaptureEscrowConfig

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as EvmAuthCaptureEscrowConfig
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


