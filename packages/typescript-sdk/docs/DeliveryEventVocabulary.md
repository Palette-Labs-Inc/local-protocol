
# DeliveryEventVocabulary

Schema for delivery event vocabularies.

## Properties

Name | Type
------------ | -------------
`name` | string
`version` | string
`_extends` | Set&lt;string&gt;
`title` | string
`description` | string
`spec` | string
`events` | [{ [key: string]: DeliveryEvent; }](DeliveryEvent.md)

## Example

```typescript
import type { DeliveryEventVocabulary } from '@localprotocol/sdk'

// TODO: Update the object below with actual values
const example = {
  "name": null,
  "version": null,
  "_extends": null,
  "title": null,
  "description": null,
  "spec": null,
  "events": null,
} satisfies DeliveryEventVocabulary

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as DeliveryEventVocabulary
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


