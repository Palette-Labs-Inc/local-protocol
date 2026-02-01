# Food Delivery Standard

Industry standard defining event vocabulary for restaurant and food delivery.

**Standard**: `xyz.localprotocol.delivery.food`
**Version**: `1.0.0`
**Extends**: `["xyz.localprotocol.delivery.core@1.0.0"]`

This standard extends core for lineage and discovery and includes the core events in its `events` map alongside domain-specific events. The `events` list is self-contained.

## Events

### Core Events

| Event | Description |
|-------|-------------|
| `pending` | Job accepted, work not started |
| `active` | Work in progress |
| `completed` | Successfully finished |
| `failed` | Unsuccessfully finished |

### Domain Events

| Event | Description |
|-------|-------------|
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

- `name` (string, required): Standard identifier (`xyz.localprotocol.delivery.food`).
- `version` (string, required): Semantic version (e.g., `1.0.0`).
- `extends` (array, required): Single parent standard this extends (for lineage and discovery) (e.g., `xyz.localprotocol.delivery.core@1.0.0`).
- `title` (string, required): Human-readable title.
- `description` (string, optional): Human-readable description.
- `spec` (string, optional): URL to specification document.
- `events` (object, required): Map of all event IDs supported by this standard, including inherited events.

### Event Definition

- `description` (string, required): Human-readable description.

## Example

```json
{
  "name": "xyz.localprotocol.delivery.food",
  "version": "1.0.0",
  "extends": ["xyz.localprotocol.delivery.core@1.0.0"],
  "title": "Food Delivery Standard",
  "description": "Event vocabulary for restaurant and food delivery.",
  "spec": "https://localprotocol.xyz/spec/delivery/food",
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

A typical progression (core + food) looks like:

```
pending -> order_placed -> preparing -> ready_for_pickup -> courier_assigned
        -> courier_at_pickup -> picked_up -> in_transit
        -> courier_at_dropoff -> delivered -> completed
```

At any point, the delivery may transition to `canceled` (food) or `failed` (core).
