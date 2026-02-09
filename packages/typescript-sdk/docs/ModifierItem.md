
# ModifierItem

A purchasable modifier item within a modifier group.

## Properties

Name | Type
------------ | -------------
`id` | string
`name` | string
`description` | string
`price` | [Amount](Amount.md)
`metadata` | { [key: string]: any; }

## Example

```typescript
import type { ModifierItem } from '@localprotocol/sdk'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "name": null,
  "description": null,
  "price": null,
  "metadata": null,
} satisfies ModifierItem

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ModifierItem
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


