
# ModifierGroup

Group of modifier options with selection constraints.

## Properties

Name | Type
------------ | -------------
`id` | string
`name` | string
`description` | string
`minimumSelections` | number
`maximumSelections` | number
`allowQuantities` | boolean
`maxPerModifier` | number
`modifierOptions` | [Array&lt;ModifierOption&gt;](ModifierOption.md)
`type` | string
`metadata` | { [key: string]: any; }

## Example

```typescript
import type { ModifierGroup } from '@localprotocol/sdk'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "name": null,
  "description": null,
  "minimumSelections": null,
  "maximumSelections": null,
  "allowQuantities": null,
  "maxPerModifier": null,
  "modifierOptions": null,
  "type": null,
  "metadata": null,
} satisfies ModifierGroup

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ModifierGroup
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


