# Availability

Weekly availability schedule for a menu view or item.

## Fields

- `timezone` (string, optional): IANA timezone for the intervals. Defaults to restaurant timezone when omitted.
- `intervals` (array, required): Weekly availability intervals.

## Example

```json
{
  "timezone": "America/Denver",
  "intervals": [
    { "day": "Monday", "from_hour": 10, "from_minute": 0, "to_hour": 18, "to_minute": 0 }
  ]
}
```
