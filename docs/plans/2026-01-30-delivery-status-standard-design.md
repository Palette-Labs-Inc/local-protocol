# Delivery Event Standard Design

## Overview

The Delivery Event Standard defines how delivery providers communicate job progress using domain-specific event vocabularies. It uses a conformance-based model where:

- **Standards define full event vocabularies** for specific domains (self-contained)
- **Businesses declare conformance** to the standards they implement for discovery
- **Extensions add lineage** by referencing a single parent standard with version date; child standards still list all events

Standards can be:

- **Industry standards**: Governed by the protocol or industry consortiums (e.g., `xyz.localprotocol.delivery.courier`)
- **Custom standards**: Defined by individual providers (e.g., `com.acme.delivery.courier`)

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
```

## Industry Standards

Industry standards define domain-specific events. Standards list all their events in the `events` map, making them self-contained.

### Courier Delivery Standard

```json
{
  "name": "xyz.localprotocol.delivery.courier",
  "version": "2026-01-30",
  "spec": "https://localprotocol.xyz/spec/delivery/courier",

  "title": "Courier Delivery Standard",
  "description": "Event vocabulary for courier-based pickup and delivery",

  "events": {
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
- Must list the full event vocabulary in `events`
- Must be versioned using YYYY-MM-DD format
- Extensions must reference a single parent standard with `name@version`

### Namespace Governance

| Namespace | Governance |
|-----------|------------|
| `xyz.localprotocol.delivery.*` | Protocol working groups |
| `org.opendelivery.*` | Industry consortium (hypothetical) |
| `com.<company>.*` | Individual business (custom) |

## Extensions

Custom standards can extend an industry standard and add events. The child `events` map must include the full parent vocabulary. This makes custom vocabularies reusable and allows them to gain traction over time.

```json
{
  "name": "com.acme.delivery.courier",
  "version": "2026-01-30",
  "extends": ["xyz.localprotocol.delivery.courier@2026-01-30"],
  "title": "Acme Courier Extension",
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
    "bagged": {
      "description": "Order sealed by merchant"
    },
    "handoff_window_opened": {
      "description": "Customer opened handoff window"
    }
  }
}
```

### Standalone Standards

Standards can also define events without extending anything:

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
  "extends": ["xyz.localprotocol.delivery.courier@2026-01-30"]
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
            "xyz.localprotocol.delivery.courier@2026-01-30",
            "com.acme.delivery.courier@2026-01-30"
          ]
        }
      }
    ]
  }
}
```

### Rules

- Provider MUST conform to at least one standard
- Standards can be industry standards (e.g., `xyz.localprotocol.delivery.courier`) or custom standards (e.g., `com.acme.delivery.courier`)
- Extensions MUST reference a single parent standard via `extends`
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
  "event_vocabulary": "xyz.localprotocol.delivery.courier@2026-01-30",
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
  "event_vocabulary": "com.acme.delivery.courier@2026-01-30",
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
