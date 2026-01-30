# Food Delivery Standard

Industry standard defining status vocabulary for restaurant and food delivery.

**Standard**: `xyz.localprotocol.delivery.food`
**Version**: `1.0.0`
**Protocol**: `xyz.localprotocol.delivery.core@1.0.0`

## Statuses

| Status | Phase | Description |
|--------|-------|-------------|
| `order_placed` | pending | Order received by merchant |
| `preparing` | active | Merchant preparing order |
| `ready_for_pickup` | active | Order ready, awaiting courier |
| `courier_assigned` | active | Courier assigned to delivery |
| `courier_at_pickup` | active | Courier arrived at merchant |
| `picked_up` | active | Courier collected order |
| `in_transit` | active | Courier en route to customer |
| `courier_at_dropoff` | active | Courier arrived at customer |
| `delivered` | completed | Order delivered to customer |
| `canceled` | failed | Delivery canceled |
| `failed` | failed | Delivery attempt unsuccessful |

## Fields

- `name` (string, required): Standard identifier (`xyz.localprotocol.delivery.food`).
- `version` (string, required): Semantic version (e.g., `1.0.0`).
- `protocol` (string, required): Core protocol reference (e.g., `xyz.localprotocol.delivery.core@1.0.0`).
- `title` (string, required): Human-readable title.
- `description` (string, optional): Human-readable description.
- `spec` (string, optional): URL to specification document.
- `statuses` (object, required): Map of status IDs to status definitions.

### Status Definition

- `phase` (string, required): Core phase this status maps to (`pending`, `active`, `completed`, `failed`).
- `description` (string, required): Human-readable description.

## Example

```json
{
  "name": "xyz.localprotocol.delivery.food",
  "version": "1.0.0",
  "protocol": "xyz.localprotocol.delivery.core@1.0.0",
  "title": "Food Delivery Standard",
  "description": "Status vocabulary for restaurant and food delivery.",
  "spec": "https://localprotocol.xyz/spec/delivery/food",
  "statuses": {
    "order_placed": {
      "phase": "pending",
      "description": "Order received by merchant"
    },
    "preparing": {
      "phase": "active",
      "description": "Merchant preparing order"
    },
    "ready_for_pickup": {
      "phase": "active",
      "description": "Order ready, awaiting courier"
    },
    "courier_assigned": {
      "phase": "active",
      "description": "Courier assigned to delivery"
    },
    "courier_at_pickup": {
      "phase": "active",
      "description": "Courier arrived at merchant"
    },
    "picked_up": {
      "phase": "active",
      "description": "Courier collected order"
    },
    "in_transit": {
      "phase": "active",
      "description": "Courier en route to customer"
    },
    "courier_at_dropoff": {
      "phase": "active",
      "description": "Courier arrived at customer"
    },
    "delivered": {
      "phase": "completed",
      "description": "Order delivered to customer"
    },
    "canceled": {
      "phase": "failed",
      "description": "Delivery canceled"
    },
    "failed": {
      "phase": "failed",
      "description": "Delivery attempt unsuccessful"
    }
  }
}
```

## Typical Progression

```
order_placed -> preparing -> ready_for_pickup -> courier_assigned
             -> courier_at_pickup -> picked_up -> in_transit
             -> courier_at_dropoff -> delivered
```

At any point, the delivery may transition to `canceled` or `failed`.
