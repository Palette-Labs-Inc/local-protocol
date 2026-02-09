
# AmountCurrency

Currency descriptor (fiat or EVM token).

## Properties

Name | Type
------------ | -------------
`symbol` | string
`chainId` | number
`address` | string
`decimals` | number

## Example

```typescript
import type { AmountCurrency } from '@localprotocol/sdk'

// TODO: Update the object below with actual values
const example = {
  "symbol": null,
  "chainId": null,
  "address": null,
  "decimals": null,
} satisfies AmountCurrency

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as AmountCurrency
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


