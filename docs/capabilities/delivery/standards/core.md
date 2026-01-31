# Core Standard

The core standard defines minimal universal events for delivery tracking. Other standards may extend core, but it is optional.
Providers may list core in `conforms_to` to advertise a shared baseline.

**Standard**: `xyz.localprotocol.delivery.core`
**Version**: `1.0.0`

## Events

| Event | Description |
|-------|-------------|
| `pending` | Job accepted, work not started |
| `active` | Work in progress |
| `completed` | Successfully finished |
| `failed` | Unsuccessfully finished |

## Fields

- `name` (string, required): Standard identifier (`xyz.localprotocol.delivery.core`).
- `version` (string, required): Semantic version (e.g., `1.0.0`).
- `events` (object, required): Map of event IDs to event definitions.

### Event Definition

- `description` (string, required): Human-readable description.

## Example

```json
{
  "name": "xyz.localprotocol.delivery.core",
  "version": "1.0.0",
  "events": {
    "pending": {
      "description": "Job accepted, work not started"
    },
    "active": {
      "description": "Work in progress"
    },
    "completed": {
      "description": "Successfully finished"
    },
    "failed": {
      "description": "Unsuccessfully finished"
    }
  }
}
```

## Event Transitions

Events follow a simple progression:

```
pending -> active -> completed
                  -> failed
```

- Deliveries start in `pending`
- Move to `active` when work begins
- End in either `completed` (success) or `failed` (unsuccessful)
