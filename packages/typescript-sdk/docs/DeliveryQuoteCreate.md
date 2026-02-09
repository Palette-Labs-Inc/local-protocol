
# DeliveryQuoteCreate

Body for creating a delivery quote.

## Properties

Name | Type
------------ | -------------
`id` | string
`nonce` | string
`price` | number
`currency` | string
`pickupLocation` | [Location](Location.md)
`dropoffLocation` | [Location](Location.md)
`pickupEstimate` | Date
`dropoffEstimate` | Date
`expiresAt` | Date

## Example

```typescript
import type { DeliveryQuoteCreate } from '@localprotocol/sdk'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "nonce": null,
  "price": null,
  "currency": null,
  "pickupLocation": null,
  "dropoffLocation": null,
  "pickupEstimate": null,
  "dropoffEstimate": null,
  "expiresAt": null,
} satisfies DeliveryQuoteCreate

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as DeliveryQuoteCreate
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


