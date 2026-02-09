# Availability

Availability schedule for a catalog, category, or item.

## Example Usage

```typescript
import { Availability } from "@localprotocol/sdk/models/components";

let value: Availability = {
  intervals: [
    {
      date: new Date("2026-12-04"),
      fromHour: 235662,
      fromMinute: 713528,
      toHour: 336508,
      toMinute: 686351,
    },
  ],
};
```

## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `timezone`                                                 | *string*                                                   | :heavy_minus_sign:                                         | IANA timezone. Defaults to merchant timezone when omitted. |
| `intervals`                                                | *components.IntervalUnion*[]                               | :heavy_check_mark:                                         | Availability intervals (weekly or date-specific).          |