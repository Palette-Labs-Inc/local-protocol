
# CreateDeliveryRequest

Body for creating a delivery from an accepted quote.

## Properties

Name | Type
------------ | -------------
`requestId` | string
`quoteId` | string
`nonce` | string
`webhookUrl` | string
`eventVocabulary` | string

## Example

```typescript
import type { CreateDeliveryRequest } from '@localprotocol/sdk'

// TODO: Update the object below with actual values
const example = {
  "requestId": null,
  "quoteId": null,
  "nonce": null,
  "webhookUrl": null,
  "eventVocabulary": null,
} satisfies CreateDeliveryRequest

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as CreateDeliveryRequest
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


