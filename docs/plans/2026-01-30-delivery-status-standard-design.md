# Delivery Event Standard Design

## Overview

The Delivery Event Standard defines how delivery providers communicate job progress using domain-specific event vocabularies. It uses a conformance-based model where:

- **Standards define full event vocabularies** for specific domains (self-contained)
- **Businesses declare conformance** to the standards they implement for discovery
- **Extensions add lineage** by referencing a single parent standard with version date; child standards still list all events

Standards can be:

- **Industry standards**: Governed by the protocol or industry consortiums (e.g., `xyz.localprotocol.delivery.food`)
- **Custom standards**: Defined by individual providers (e.g., `com.acme.delivery.custom`)

## Why Everything Is a Standard

By making custom events follow the same format as industry standards, they become:

- **Discoverable**: Clients can fetch and understand any provider's event vocabulary
- **Reusable**: A custom standard can be adopted by other providers
- **Evolvable**: Popular custom standards can be promoted to industry standards
- **Interoperable**: Two providers using the same custom standard are automatically compatible

This creates a path from experimentation to standardization.

```
+---------------------------------------------+
|  Custom Standards (provider-defined)        |  <- same format, provider namespace
+---------------------------------------------+
|  Industry Standards (protocol-governed)     |  <- interoperable across providers
+---------------------------------------------+
|  Core (optional baseline)                   |  <- minimal universal events
+---------------------------------------------+
```

## Core Standard (Optional)

The core standard defines minimal universal events for delivery tracking. Other standards may extend core, but it is optional.
Providers can include core in `config.conforms_to` to advertise a shared baseline.
Standards that extend core must include these events in their `events` map.

### Events

| Event | Description |
|-------|-------------|
| `pending` | Job accepted, work not started |
| `active` | Work in progress |
| `completed` | Successfully finished |
| `failed` | Unsuccessfully finished |

### Schema

```json
{
  "$id": "https://localprotocol.xyz/schemas/delivery/standards/core.json",
  "name": "xyz.localprotocol.delivery.core",
  "version": "2026-01-30",
  "events": {
    "pending":   {"description": "Job accepted, work not started"},
    "active":    {"description": "Work in progress"},
    "completed": {"description": "Successfully finished"},
    "failed":    {"description": "Unsuccessfully finished"}
  }
}
```

## Industry Standards

Industry standards define domain-specific events and can extend core or another single parent standard.
When they extend, their `events` map is a full vocabulary that includes the parent events.
Extending core is optional; some standards may define events without any parent.

### Standard Structure

```json
{
  "$id": "https://localprotocol.xyz/schemas/delivery/standards/food.json",
  "name": "xyz.localprotocol.delivery.food",
  "version": "2026-01-30",
  "extends": ["xyz.localprotocol.delivery.core@2026-01-30"],
  "spec": "https://localprotocol.xyz/spec/delivery/food",

  "title": "Food Delivery Standard",
  "description": "Event vocabulary for restaurant and food delivery",

  "events": {
    "pending":   {"description": "Job accepted, work not started"},
    "active":    {"description": "Work in progress"},
    "completed": {"description": "Successfully finished"},
    "failed":    {"description": "Unsuccessfully finished"},
    "order_placed":       {"description": "Order received by merchant"},
    "preparing":          {"description": "Merchant preparing order"},
    "ready_for_pickup":   {"description": "Order ready, awaiting courier"},
    "courier_assigned":   {"description": "Courier assigned to delivery"},
    "courier_at_pickup":  {"description": "Courier arrived at merchant"},
    "picked_up":          {"description": "Courier collected order"},
    "in_transit":         {"description": "Courier en route to customer"},
    "courier_at_dropoff": {"description": "Courier arrived at customer"},
    "delivered":          {"description": "Order delivered to customer"},
    "canceled":           {"description": "Delivery canceled"}
  }
}
```

### Requirements

- Must include human-readable descriptions
- Must list the full event vocabulary in `events`, which serves as the declaration of conformance for the standard (including inherited events)
- Must be versioned using YYYY-MM-DD format
- Extensions must reference a single parent standard with `name@version`

### Namespace Governance

| Namespace | Governance |
|-----------|------------|
| `xyz.localprotocol.delivery.*` | Protocol working groups |
| `org.opendelivery.*` | Industry consortium (hypothetical) |
| `com.business.*` | Individual business (custom) |

## Extensions

Custom standards can extend a single industry standard and add events. The child `events` map must include the full parent vocabulary. This makes custom vocabularies reusable and allows them to gain traction over time.

```json
{
  "name": "com.acme.delivery.food",
  "version": "2026-01-30",
  "extends": ["xyz.localprotocol.delivery.food@2026-01-30"],
  "title": "Acme Food Extension",
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
    },
    "bagged": {
      "description": "Order sealed by merchant"
    },
    "handoff_window_opened": {
      "description": "Customer opened handoff window"
    }
  }
}
```

### Standard Without Core

```json
{
  "name": "xyz.localprotocol.delivery.ocean",
  "version": "2026-01-30",
  "title": "Ocean Freight Standard",
  "description": "Event vocabulary for international shipping by sea",
  "events": {
    "booking_confirmed": { "description": "Cargo booking confirmed" },
    "loaded_on_vessel": { "description": "Container loaded onto vessel" },
    "arrived_at_port": { "description": "Vessel arrived at destination port" }
  }
}
```

Clients read the event vocabulary directly from the standard's `events` map; no traversal is required. `extends` is for lineage and discovery, and if a child redefines an event ID, the child definition is authoritative.

## Versioning

Local-protocol uses date-based versioning in `YYYY-MM-DD` format, consistent with UCP.

### Format

`YYYY-MM-DD` (e.g., `2026-01-30`)

Each version represents a snapshot of the standard on that date. Breaking changes require a new version date.

### Extends Reference

```json
{
  "extends": ["xyz.localprotocol.delivery.core@2026-01-30"]
}
```

Initially, exact version match is required.

## Provider Conformance

Providers declare which standards they conform to in their discovery profile capability config. This is how clients discover compatibility.

### Profile Structure

In UCP discovery, this appears in `ucp.capabilities` as a capability object (other required fields omitted for brevity).

```json
{
  "ucp": {
    "version": "YYYY-MM-DD",
    "capabilities": [
      {
        "name": "xyz.localprotocol.delivery",
        "version": "2026-01-30",
        "spec": "https://localprotocol.xyz/spec/delivery",
        "schema": "https://localprotocol.xyz/schemas/delivery.json",
        "config": {
          "conforms_to": [
            "xyz.localprotocol.delivery.food@2026-01-30",
            "com.acme.delivery.food@2026-01-30"
          ]
        }
      }
    ]
  }
}
```

### Rules

- Provider MUST conform to at least one standard
- Standards can be industry standards (e.g., `xyz.localprotocol.delivery.food`) or custom standards (e.g., `com.acme.delivery.custom`)
- Extensions MUST reference a single parent standard via `extends`
- Conformance to core is optional
- Provider MUST fully implement all events in declared standards
- Clients check `config.conforms_to` to determine compatibility
- `config.conforms_to` is for discovery; clients read the standard's `events` map directly and do not traverse `extends`

## Delivery Object

When a provider returns a delivery object, it includes event information.

### Structure

```json
{
  "id": "del_789",
  "event": "courier_at_pickup",
  "event_description": "Courier arrived at merchant",
  "event_vocabulary": "xyz.localprotocol.delivery.food@2026-01-30",
  "updated_at": "2026-01-30T19:12:00Z"
}
```

### Fields

| Field | Required | Description |
|-------|----------|-------------|
| `event` | Yes | Current event ID |
| `event_description` | Yes | Human-readable description |
| `event_vocabulary` | Yes | Which standard defines this event |
| `updated_at` | Yes | When event last changed (RFC 3339) |

### Custom Standard Example

```json
{
  "id": "del_789",
  "event": "bagged",
  "event_description": "Order sealed by merchant",
  "event_vocabulary": "com.acme.delivery.food@2026-01-30",
  "updated_at": "2026-01-30T19:08:00Z"
}
```

Custom standards follow the same format as industry standards and are always referenced in `event_vocabulary`.

## Future Considerations

The following topics are out of scope for this design but may be addressed later:

- **Job object structure** - Fields on an accepted delivery (assignee, tracking URL, etc.)
- **Cancellation rules** - Who can cancel, when, penalties/fees
- **Communication transport** - How updates are delivered (webhooks, polling, both)
- **Proof of delivery** - Signatures, photos, confirmation
- **Real-time tracking** - Driver location updates, ETA recalculation
