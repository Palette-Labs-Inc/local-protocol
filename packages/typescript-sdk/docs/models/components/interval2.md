# Interval2

## Example Usage

```typescript
import { Interval2 } from "@localprotocol/sdk/models/components";

let value: Interval2 = {
  date: new Date("2024-04-05"),
  fromHour: 643559,
  fromMinute: 876174,
  toHour: 868973,
  toMinute: 675827,
};
```

## Fields

| Field                                | Type                                 | Required                             | Description                          |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `day`                                | *string*                             | :heavy_minus_sign:                   | Day of week (e.g., Monday, Tuesday). |
| `date`                               | [Date](../../types/rfcdate.md)       | :heavy_check_mark:                   | Calendar date in YYYY-MM-DD.         |
| `fromHour`                           | *number*                             | :heavy_check_mark:                   | Start hour (0-23).                   |
| `fromMinute`                         | *number*                             | :heavy_check_mark:                   | Start minute (0-59).                 |
| `toHour`                             | *number*                             | :heavy_check_mark:                   | End hour (0-23).                     |
| `toMinute`                           | *number*                             | :heavy_check_mark:                   | End minute (0-59).                   |