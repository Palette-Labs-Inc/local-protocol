# Core Standard

The core standard defines universal events for delivery tracking. All domain standards must include these events - this is enforced via JSON Schema.

**Standard**: `xyz.localprotocol.delivery.core`
**Version**: `1.0.0`

## Events

| Event | Description |
|-------|-------------|
| `pending` | Job accepted, work not started |
| `active` | Work in progress |
| `completed` | Successfully finished |
| `failed` | Unsuccessfully finished |

## Enforcement

Domain standards must include core events in their `events` object. The JSON Schema enforces this:

```json
{
  "events": {
    "required": ["pending", "active", "completed", "failed"]
  }
}
```

This ensures any client that understands core can work with any conforming standard.

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
