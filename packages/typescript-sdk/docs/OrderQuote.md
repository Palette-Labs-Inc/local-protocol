
# OrderQuote

An order quote.

## Properties

Name | Type
------------ | -------------
`id` | string
`intentId` | string
`nonce` | string
`price` | number
`readyAt` | Date
`expiresAt` | Date

## Example

```typescript
import type { OrderQuote } from '@localprotocol/sdk'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "intentId": null,
  "nonce": null,
  "price": null,
  "readyAt": null,
  "expiresAt": null,
} satisfies OrderQuote

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as OrderQuote
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


