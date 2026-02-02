# Courier Delivery Standard

Industry standard defining event vocabulary for courier-based pickup and delivery.

**Standard**: `xyz.localprotocol.delivery.courier`
**Version**: `2026-01-30`

## Events

| Event | Description |
|-------|-------------|
| `pending` | Job accepted, work not started |
| `active` | Work in progress |
| `completed` | Successfully finished |
| `failed` | Unsuccessfully finished |
| `order_placed` | Order received by merchant |
| `preparing` | Merchant preparing order |
| `ready_for_pickup` | Order ready, awaiting courier |
| `courier_assigned` | Courier assigned to delivery |
| `courier_at_pickup` | Courier arrived at merchant |
| `picked_up` | Courier collected order |
| `in_transit` | Courier en route to customer |
| `courier_at_dropoff` | Courier arrived at customer |
| `delivered` | Order delivered to customer |
| `canceled` | Delivery canceled |

## Fields

- `name` (string, required): Standard identifier (`xyz.localprotocol.delivery.courier`).
- `version` (string, required): Version in YYYY-MM-DD format (e.g., `2026-01-30`).
- `extends` (array, optional): Single parent standard this extends for lineage and discovery.
- `title` (string, required): Human-readable title.
- `description` (string, optional): Human-readable description.
- `spec` (string, optional): URL to specification document.
- `events` (object, required): Map of all event IDs supported by this standard.

### Event Definition

- `description` (string, required): Human-readable description.

## Example

```json
{
  "name": "xyz.localprotocol.delivery.courier",
  "version": "2026-01-30",
  "title": "Courier Delivery Standard",
  "description": "Event vocabulary for courier-based pickup and delivery.",
  "spec": "https://localprotocol.xyz/spec/delivery/courier",
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
    },
    "order_placed": {
      "description": "Order received by merchant"
    },
    "preparing": {
      "description": "Merchant preparing order"
    },
    "ready_for_pickup": {
      "description": "Order ready, awaiting courier"
    },
    "courier_assigned": {
      "description": "Courier assigned to delivery"
    },
    "courier_at_pickup": {
      "description": "Courier arrived at merchant"
    },
    "picked_up": {
      "description": "Courier collected order"
    },
    "in_transit": {
      "description": "Courier en route to customer"
    },
    "courier_at_dropoff": {
      "description": "Courier arrived at customer"
    },
    "delivered": {
      "description": "Order delivered to customer"
    },
    "canceled": {
      "description": "Delivery canceled"
    }
  }
}
```

## Typical Progression

```
pending -> order_placed -> preparing -> ready_for_pickup -> courier_assigned
        -> courier_at_pickup -> picked_up -> in_transit
        -> courier_at_dropoff -> delivered -> completed
```

At any point, the delivery may transition to `canceled` or `failed`.
