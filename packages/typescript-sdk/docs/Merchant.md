
# Merchant

Merchant catalog payload containing denormalized catalogs.

## Properties

Name | Type
------------ | -------------
`id` | string
`name` | string
`timezone` | string
`lastUpdated` | Date
`catalogs` | [Array&lt;Catalog&gt;](Catalog.md)
`metadata` | { [key: string]: any; }

## Example

```typescript
import type { Merchant } from '@localprotocol/sdk'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "name": null,
  "timezone": null,
  "lastUpdated": null,
  "catalogs": null,
  "metadata": null,
} satisfies Merchant

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as Merchant
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


