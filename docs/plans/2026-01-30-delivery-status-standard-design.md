# Delivery Event Standard Design

## Overview

The Delivery Event Standard defines how delivery providers communicate job progress. It uses a conformance-based model where:

- **Protocol defines a required core** with universal events
- **Standards define events** for specific domains
- **Businesses declare conformance** to standards they implement

The key principle: **if a provider declares conformance to a standard, clients can rely on that standard's events being implemented correctly.**

Standards can be:

- **Industry standards**: Governed by the protocol or industry consortiums (e.g., `xyz.localprotocol.delivery.food`)
- **Custom standards**: Defined by individual providers (e.g., `com.acme.delivery.custom`)

All standards must reference core via the `extends` field.

### Why Everything Is a Standard

By making custom events follow the same format as industry standards, they become:

- **Discoverable**: Clients can fetch and understand any provider's event vocabulary
- **Reusable**: A custom standard can be adopted by other providers
- **Evolvable**: Popular custom standards can be promoted to industry standards
- **Interoperable**: Two providers using the same custom standard are automatically compatible

This creates a path from experimentation to standardization: providers can innovate with custom standards, and successful patterns can be adopted more widely.

```
+---------------------------------------------+
|  Custom Standards (provider-defined)        |  <- same format, provider namespace
+---------------------------------------------+
|  Industry Standards (protocol-governed)     |  <- interoperable across providers
+---------------------------------------------+
|  Core (required)                            |  <- universal events
+---------------------------------------------+
```

## Core Standard

The core standard defines universal events for delivery tracking. All domain standards must include these events.

### Events

| Event | Description |
|-------|-------------|
| `pending` | Job accepted, work not started |
| `active` | Work in progress |
| `completed` | Successfully finished |
| `failed` | Unsuccessfully finished |

### Enforcement

Domain standards must include core events in their `events` object. This is enforced via JSON Schema:

```json
{
  "events": {
    "required": ["pending", "active", "completed", "failed"]
  }
}
```

This ensures any client that understands core can work with any conforming standard.

### Rules

- Every domain standard must include core events (schema-enforced)
- Clients can always determine basic state from core events
- Event transitions follow: `pending` -> `active` -> `completed` | `failed`

### Schema

```json
{
  "$id": "https://localprotocol.xyz/standards/delivery/core.json",
  "name": "xyz.localprotocol.delivery.core",
  "version": "1.0.0",

  "events": {
    "pending":   {"description": "Job accepted, work not started"},
    "active":    {"description": "Work in progress"},
    "completed": {"description": "Successfully finished"},
    "failed":    {"description": "Unsuccessfully finished"}
  }
}
```

## Industry Standards

Industry standards define domain-specific events. They are governed by the protocol, industry consortiums, or recognized working groups.

### Standard Structure

```json
{
  "$id": "https://localprotocol.xyz/standards/delivery/food.json",
  "name": "xyz.localprotocol.delivery.food",
  "version": "1.0.0",
  "extends": "xyz.localprotocol.delivery.core@1.0.0",
  "spec": "https://localprotocol.xyz/spec/delivery/food",

  "title": "Food Delivery Standard",
  "description": "Event vocabulary for restaurant and food delivery",

  "events": {
    "pending":            {"description": "Job accepted, work not started"},
    "active":             {"description": "Work in progress"},
    "completed":          {"description": "Successfully finished"},
    "failed":             {"description": "Unsuccessfully finished"},
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

- Must reference core via `extends` field
- Must include human-readable descriptions
- Must be versioned using semver

### Namespace Governance

| Namespace | Governance |
|-----------|------------|
| `xyz.localprotocol.delivery.*` | Protocol working groups |
| `org.opendelivery.*` | Industry consortium (hypothetical) |
| `com.business.*` | Individual business (custom) |

## Versioning

Local-protocol uses [Semantic Versioning](https://semver.org/) for standards.

### Format

`MAJOR.MINOR.PATCH` (e.g., `1.2.0`)

### Version Bump Rules

| Change | Bump | Example |
|--------|------|---------|
| Add new event | Minor | `1.0.0` -> `1.1.0` |
| Add optional field to event | Minor | `1.0.0` -> `1.1.0` |
| Fix description typo | Patch | `1.0.0` -> `1.0.1` |
| Remove an event | **Major** | `1.0.0` -> `2.0.0` |
| Rename an event ID | **Major** | `1.0.0` -> `2.0.0` |
| Change required field to optional | **Major** | `1.0.0` -> `2.0.0` |

### Compatibility Rules

- **Patch versions** are always backward compatible
- **Minor versions** are backward compatible (clients handle unknown events gracefully)
- **Major versions** may break clients expecting the previous version

### Protocol Reference

```json
{
  "protocol": "xyz.localprotocol.delivery.core@1.0.0"
}
```

Providers MAY support version ranges in future (e.g., `>=1.0.0 <2.0.0`), but initially exact version match is required.

## Provider Conformance

Providers declare which standards they conform to in their profile. This is how clients discover compatibility.

### Profile Structure

```json
{
  "capabilities": {
    "xyz.localprotocol.delivery": {
      "version": "1.0.0",
      "spec": "https://localprotocol.xyz/spec/delivery",
      "schema": "https://localprotocol.xyz/schemas/delivery.json",

      "conforms_to": [
        "xyz.localprotocol.delivery.food@1.2.0"
      ]
    }
  }
}
```

### Custom Standards

Providers can define their own standards following the same format as industry standards. Custom standards must reference core via the `extends` field and include core events:

```json
{
  "name": "com.acme.delivery.custom",
  "version": "1.0.0",
  "extends": "xyz.localprotocol.delivery.core@1.0.0",
  "title": "Acme Custom Delivery",
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
    "sorting_at_warehouse": {
      "description": "Package being sorted at warehouse"
    },
    "on_truck": {
      "description": "Package loaded on delivery truck"
    },
    "delivered": {
      "description": "Package delivered"
    }
  }
}
```

The provider then references their custom standard in `conforms_to`:

```json
{
  "conforms_to": [
    "com.acme.delivery.custom@1.0.0"
  ]
}
```

### Fields

| Field | Required | Description |
|-------|----------|-------------|
| `version` | Yes | Provider's capability version |
| `conforms_to` | Yes | Array of standards (with versions) provider implements |

### Rules

- Provider MUST conform to at least one standard
- Standards can be industry standards (e.g., `xyz.localprotocol.delivery.food`) or custom standards (e.g., `com.acme.delivery.custom`)
- All standards MUST reference core via the `extends` field
- Provider MUST fully implement all events in declared standards
- Clients check `conforms_to` to determine compatibility

## Delivery Object

When a provider returns a delivery object, it includes event information.

### Structure

```json
{
  "id": "del_789",
  "event": "courier_at_pickup",
  "event_description": "Courier arrived at merchant",
  "event_vocabulary": "xyz.localprotocol.delivery.food@1.2.0",
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
  "event": "sorting_at_warehouse",
  "event_description": "Package being sorted at warehouse",
  "event_vocabulary": "com.acme.delivery.custom@1.0.0",
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
