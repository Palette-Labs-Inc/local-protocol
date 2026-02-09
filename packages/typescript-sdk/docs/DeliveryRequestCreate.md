
# DeliveryRequestCreate

Body for creating a delivery request.

## Properties

Name | Type
------------ | -------------
`id` | string
`nonce` | string
`pickupLocation` | [Location](Location.md)
`dropoffLocation` | [Location](Location.md)
`pickupTime` | Date
`dropoffTime` | Date
`pickupInstructions` | string
`dropoffInstructions` | string

## Example

```typescript
import type { DeliveryRequestCreate } from '@localprotocol/sdk'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "nonce": null,
  "pickupLocation": null,
  "dropoffLocation": null,
  "pickupTime": null,
  "dropoffTime": null,
  "pickupInstructions": null,
  "dropoffInstructions": null,
} satisfies DeliveryRequestCreate

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as DeliveryRequestCreate
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


