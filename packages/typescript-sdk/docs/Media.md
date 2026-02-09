
# Media

Product media item (image, video, etc.).

## Properties

Name | Type
------------ | -------------
`type` | string
`url` | string
`altText` | string
`width` | number
`height` | number

## Example

```typescript
import type { Media } from '@localprotocol/sdk'

// TODO: Update the object below with actual values
const example = {
  "type": null,
  "url": null,
  "altText": null,
  "width": null,
  "height": null,
} satisfies Media

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as Media
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


