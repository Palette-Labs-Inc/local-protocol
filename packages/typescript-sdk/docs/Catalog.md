
# Catalog

A catalog containing embedded categories, items, availability, and fulfillment configuration.

## Properties

Name | Type
------------ | -------------
`id` | string
`name` | string
`description` | string
`categories` | [Array&lt;CatalogCategory&gt;](CatalogCategory.md)
`items` | [Array&lt;CatalogItem&gt;](CatalogItem.md)
`availability` | [Availability](Availability.md)
`metadata` | { [key: string]: any; }

## Example

```typescript
import type { Catalog } from '@localprotocol/sdk'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "name": null,
  "description": null,
  "categories": null,
  "items": null,
  "availability": null,
  "metadata": null,
} satisfies Catalog

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as Catalog
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


