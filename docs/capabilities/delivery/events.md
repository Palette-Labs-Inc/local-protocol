# Events

The courier standard defines events for pickup-and-deliver workflows.

**Standard**: `xyz.localprotocol.delivery.courier@2026-01-30`

## Event Types

Events use fully qualified names: `{namespace}.{event}@{version}`

| Event | Fully Qualified | Description |
|-------|-----------------|-------------|
| `created` | `xyz.localprotocol.delivery.courier.created@2026-01-30` | Delivery created |
| `assigned` | `xyz.localprotocol.delivery.courier.assigned@2026-01-30` | Courier assigned |
| `enroute_pickup` | `xyz.localprotocol.delivery.courier.enroute_pickup@2026-01-30` | Courier heading to pickup |
| `arrived_pickup` | `xyz.localprotocol.delivery.courier.arrived_pickup@2026-01-30` | Courier at pickup location |
| `collected` | `xyz.localprotocol.delivery.courier.collected@2026-01-30` | Courier picked up |
| `arrived_dropoff` | `xyz.localprotocol.delivery.courier.arrived_dropoff@2026-01-30` | Courier at dropoff location |
| `delivered` | `xyz.localprotocol.delivery.courier.delivered@2026-01-30` | Courier completed dropoff |
| `canceled` | `xyz.localprotocol.delivery.courier.canceled@2026-01-30` | Delivery canceled |

## Typical Progression

```
created -> assigned -> enroute_pickup -> arrived_pickup -> collected -> arrived_dropoff -> delivered
```

At any point, the delivery may transition to `canceled`.

## Event Object

When returning an event:

```json
{
  "id": "del_789",
  "event": "xyz.localprotocol.delivery.courier.arrived_pickup@2026-01-30",
  "updated_at": "2026-01-30T19:12:00Z"
}
```

| Field | Description |
|-------|-------------|
| `event` | Fully qualified event identifier (`{namespace}.{event}@{version}`) |
| `updated_at` | When event occurred (RFC 3339) |

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
