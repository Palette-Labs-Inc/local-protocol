
# Amount

Amount with explicit currency. Value is always in minor units (e.g., cents for USD).

## Properties

Name | Type
------------ | -------------
`value` | string
`currency` | [AmountCurrency](AmountCurrency.md)

## Example

```typescript
import type { Amount } from '@localprotocol/sdk'

// TODO: Update the object below with actual values
const example = {
  "value": null,
  "currency": null,
} satisfies Amount

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as Amount
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


