
# ModifierOption

Selectable option within a modifier group.

## Properties

Name | Type
------------ | -------------
`id` | string
`modifierItem` | [ModifierItem](ModifierItem.md)
`childModifierGroups` | [Array&lt;ModifierGroup&gt;](ModifierGroup.md)
`isDefault` | boolean
`metadata` | { [key: string]: any; }

## Example

```typescript
import type { ModifierOption } from '@localprotocol/sdk'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "modifierItem": null,
  "childModifierGroups": null,
  "isDefault": null,
  "metadata": null,
} satisfies ModifierOption

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ModifierOption
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


