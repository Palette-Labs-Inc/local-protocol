
# Location

A location specified by coordinates and/or postal address. At least one must be provided.

## Properties

Name | Type
------------ | -------------
`coordinates` | [Coordinates](Coordinates.md)
`postalAddress` | [PostalAddress](PostalAddress.md)

## Example

```typescript
import type { Location } from '@localprotocol/sdk'

// TODO: Update the object below with actual values
const example = {
  "coordinates": null,
  "postalAddress": null,
} satisfies Location

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as Location
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


