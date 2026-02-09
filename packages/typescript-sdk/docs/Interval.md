
# Interval

A single time interval for a day of the week or a specific date.

## Properties

Name | Type
------------ | -------------
`day` | string
`date` | Date
`fromHour` | number
`fromMinute` | number
`toHour` | number
`toMinute` | number

## Example

```typescript
import type { Interval } from '@localprotocol/sdk'

// TODO: Update the object below with actual values
const example = {
  "day": null,
  "date": null,
  "fromHour": null,
  "fromMinute": null,
  "toHour": null,
  "toMinute": null,
} satisfies Interval

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as Interval
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


