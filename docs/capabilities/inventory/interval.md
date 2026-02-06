# Interval

Single time interval usable for availability or closure schedules.

## Fields

- `day` (string, optional): Day of week (e.g., Monday, Tuesday). Use for weekly recurring intervals.
- `date` (string, optional): Calendar date in `YYYY-MM-DD` for one-off exceptions (e.g., a holiday closure).
- `from_hour` (integer, required): Start hour (0-23).
- `from_minute` (integer, required): Start minute (0-59).
- `to_hour` (integer, required): End hour (0-23).
- `to_minute` (integer, required): End minute (0-59).

Either `day` or `date` is required.

## Examples

Weekly interval:

```json
{ "day": "Friday", "from_hour": 11, "from_minute": 0, "to_hour": 22, "to_minute": 0 }
```

Date-specific interval:

```json
{ "date": "2026-12-25", "from_hour": 0, "from_minute": 0, "to_hour": 23, "to_minute": 59 }
```
