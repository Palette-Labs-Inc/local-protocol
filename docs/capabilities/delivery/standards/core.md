# Core Standard

The core standard defines universal phases for delivery status tracking. All providers must support these phases, and all statuses (from any standard or custom) must map to exactly one phase.

**Standard**: `xyz.localprotocol.delivery.core`
**Version**: `1.0.0`

## Phases

| Phase | Terminal | Description |
|-------|----------|-------------|
| `pending` | No | Job accepted, work not started |
| `active` | No | Work in progress |
| `completed` | Yes | Successfully finished |
| `failed` | Yes | Unsuccessfully finished |

## Fields

- `name` (string, required): Standard identifier (`xyz.localprotocol.delivery.core`).
- `version` (string, required): Semantic version (e.g., `1.0.0`).
- `phases` (object, required): Map of phase IDs to phase definitions.
  - `pending` (object, required): Phase definition.
  - `active` (object, required): Phase definition.
  - `completed` (object, required): Phase definition.
  - `failed` (object, required): Phase definition.

### Phase Definition

- `terminal` (boolean, required): Whether this phase represents a final state.
- `description` (string, required): Human-readable description.

## Example

```json
{
  "name": "xyz.localprotocol.delivery.core",
  "version": "1.0.0",
  "phases": {
    "pending": {
      "terminal": false,
      "description": "Job accepted, work not started"
    },
    "active": {
      "terminal": false,
      "description": "Work in progress"
    },
    "completed": {
      "terminal": true,
      "description": "Successfully finished"
    },
    "failed": {
      "terminal": true,
      "description": "Unsuccessfully finished"
    }
  }
}
```

## Phase Transitions

Phases follow a simple progression:

```
pending -> active -> completed
                  -> failed
```

- Deliveries start in `pending`
- Move to `active` when work begins
- End in either `completed` (success) or `failed` (unsuccessful)
