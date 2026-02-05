# Availability Interval

Single availability interval for a day of the week.

## Fields

- `day` (string, required): Day of week (e.g., Monday, Tuesday).
- `from_hour` (integer, required): Start hour (0-23).
- `from_minute` (integer, required): Start minute (0-59).
- `to_hour` (integer, required): End hour (0-23).
- `to_minute` (integer, required): End minute (0-59).

## Example

```json
{ "day": "Friday", "from_hour": 11, "from_minute": 0, "to_hour": 22, "to_minute": 0 }
```
