# Availability

Availability schedule for a menu view or item.

## Fields

- `timezone` (string, optional): IANA timezone for the intervals. Defaults to merchant timezone when omitted.
- `intervals` (array, required): Availability intervals (weekly or date-specific).

Intervals use the `interval` type. Use `day` for weekly schedules and `date` for one-off exceptions (e.g., holiday hours). The same interval shape can be reused for closure schedules.

## Example

```json
{
  "timezone": "America/Denver",
  "intervals": [
    { "day": "Monday", "from_hour": 10, "from_minute": 0, "to_hour": 18, "to_minute": 0 }
  ]
}
```
