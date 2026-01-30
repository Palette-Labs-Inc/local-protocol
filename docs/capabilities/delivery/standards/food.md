# Food Delivery Standard

Industry standard defining event vocabulary for restaurant and food delivery.

**Standard**: `xyz.localprotocol.delivery.food`
**Version**: `1.0.0`
**Protocol**: `xyz.localprotocol.delivery.core@1.0.0`

## Events

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
| `failed` | Delivery attempt unsuccessful |

## Fields

- `name` (string, required): Standard identifier (`xyz.localprotocol.delivery.food`).
- `version` (string, required): Semantic version (e.g., `1.0.0`).
- `protocol` (string, required): Core protocol reference (e.g., `xyz.localprotocol.delivery.core@1.0.0`).
- `title` (string, required): Human-readable title.
- `description` (string, optional): Human-readable description.
- `spec` (string, optional): URL to specification document.
- `events` (object, required): Map of event IDs to event definitions.

### Event Definition

- `description` (string, required): Human-readable description.

## Example

```json
{
  "name": "xyz.localprotocol.delivery.food",
  "version": "1.0.0",
  "protocol": "xyz.localprotocol.delivery.core@1.0.0",
  "title": "Food Delivery Standard",
  "description": "Event vocabulary for restaurant and food delivery.",
  "spec": "https://localprotocol.xyz/spec/delivery/food",
  "events": {
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
    },
    "failed": {
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
