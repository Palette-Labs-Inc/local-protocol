# Events

The courier standard defines events for pickup-and-deliver workflows.

**Standard**: `xyz.localprotocol.delivery.courier@2026-01-30`

## Events

| Event | Description |
|-------|-------------|
| `pending` | Delivery accepted, awaiting courier assignment |
| `preparing` | Merchant preparing order |
| `ready_for_pickup` | Order ready, awaiting courier |
| `courier_assigned` | Courier assigned to delivery |
| `courier_at_pickup` | Courier arrived at merchant |
| `picked_up` | Courier collected order |
| `in_transit` | Courier en route to customer |
| `courier_at_dropoff` | Courier arrived at customer |
| `delivered` | Order delivered to customer |
| `canceled` | Delivery canceled |

## Typical Progression

```
pending -> preparing -> ready_for_pickup -> courier_assigned
        -> courier_at_pickup -> picked_up -> in_transit
        -> courier_at_dropoff -> delivered
```

At any point, the delivery may transition to `canceled`.

## Delivery Object

When a provider returns a delivery, it includes event information:

```json
{
  "id": "del_789",
  "event": "courier_at_pickup",
  "event_description": "Courier arrived at merchant",
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
