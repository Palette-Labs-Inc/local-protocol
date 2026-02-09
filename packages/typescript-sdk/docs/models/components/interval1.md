# Interval1

## Example Usage

```typescript
import { Interval1 } from "@localprotocol/sdk/models/components";

let value: Interval1 = {
  day: "<value>",
  fromHour: 658320,
  fromMinute: 172238,
  toHour: 18742,
  toMinute: 568543,
};
```

## Fields

| Field                                | Type                                 | Required                             | Description                          |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `day`                                | *string*                             | :heavy_check_mark:                   | Day of week (e.g., Monday, Tuesday). |
| `date`                               | [Date](../../types/rfcdate.md)       | :heavy_minus_sign:                   | Calendar date in YYYY-MM-DD.         |
| `fromHour`                           | *number*                             | :heavy_check_mark:                   | Start hour (0-23).                   |
| `fromMinute`                         | *number*                             | :heavy_check_mark:                   | Start minute (0-59).                 |
| `toHour`                             | *number*                             | :heavy_check_mark:                   | End hour (0-23).                     |
| `toMinute`                           | *number*                             | :heavy_check_mark:                   | End minute (0-59).                   |