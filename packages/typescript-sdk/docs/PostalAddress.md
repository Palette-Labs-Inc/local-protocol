
# PostalAddress


## Properties

Name | Type
------------ | -------------
`extendedAddress` | string
`streetAddress` | string
`addressLocality` | string
`addressRegion` | string
`addressCountry` | string
`postalCode` | string
`firstName` | string
`lastName` | string
`phoneNumber` | string

## Example

```typescript
import type { PostalAddress } from '@localprotocol/sdk'

// TODO: Update the object below with actual values
const example = {
  "extendedAddress": null,
  "streetAddress": null,
  "addressLocality": null,
  "addressRegion": null,
  "addressCountry": null,
  "postalCode": null,
  "firstName": null,
  "lastName": null,
  "phoneNumber": null,
} satisfies PostalAddress

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as PostalAddress
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


