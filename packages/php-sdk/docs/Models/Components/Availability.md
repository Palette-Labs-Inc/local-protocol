# Availability

Availability schedule for a catalog, category, or item.


## Fields

| Field                                                                                        | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `timezone`                                                                                   | *?string*                                                                                    | :heavy_minus_sign:                                                                           | IANA timezone. Defaults to merchant timezone when omitted.                                   |
| `intervals`                                                                                  | array<[Components\Interval1\|Components\Interval2](../../Models/Components/IntervalUnion.md)> | :heavy_check_mark:                                                                           | Availability intervals (weekly or date-specific).                                            |