# Events

The courier standard defines events for pickup-and-deliver workflows.

**Standard**: `xyz.localprotocol.delivery.courier@2026-01-30`

## Events

| Event | Description |
|-------|-------------|
| `created` | Delivery created |
| `assigned` | Courier assigned |
| `arrived_pickup` | Courier at pickup location |
| `collected` | Courier picked up |
| `arrived_dropoff` | Courier at dropoff location |
| `delivered` | Courier completed dropoff |
| `canceled` | Delivery canceled |

## Typical Progression

```
created -> assigned -> arrived_pickup -> collected -> arrived_dropoff -> delivered
```

At any point, the delivery may transition to `canceled`.

## Delivery Object

When a provider returns a delivery, it includes event information:

```json
{
  "id": "del_789",
  "event": "arrived_pickup",
  "event_description": "Courier at pickup location",
  "event_vocabulary": "xyz.localprotocol.delivery.courier@2026-01-30",
  "updated_at": "2026-01-30T19:12:00Z"
}
```

| Field | Description |
|-------|-------------|
| `event` | Current event ID from the vocabulary |
| `event_description` | Human-readable description |
| `event_vocabulary` | Standard that defines this event (`name@version`) |
| `updated_at` | When event last changed (RFC 3339) |

## Conformance

Providers declare which event vocabularies they support in their capability config:

```json
{
  "name": "xyz.localprotocol.delivery",
  "config": {
    "conforms_to": ["xyz.localprotocol.delivery.courier@2026-01-30"]
  }
}
```
