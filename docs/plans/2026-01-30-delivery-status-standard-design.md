# Delivery Status Standard Design

## Overview

The Delivery Status Standard defines how delivery providers communicate job progress. It uses a conformance-based model where:

- **Protocol defines a required core** with universal phases
- **Industry standards extend core** with domain-specific statuses
- **Businesses declare conformance** to standards they implement
- **Businesses may add custom statuses** that are not expected to interoperate

The key principle: **if a provider declares conformance to a standard, clients can rely on that standard's statuses being implemented correctly.**

All statuses (including custom) must map to a **phase** from core. This ensures clients can always determine basic state (pending, active, completed, failed) even for unknown statuses.

```
+---------------------------------------------+
|  Custom (provider-specific)                 |  <- allowed, not interoperable
+---------------------------------------------+
|  Industry Standards (opt-in)                |  <- interoperable if declared
+---------------------------------------------+
|  Core (required)                            |  <- universal, guaranteed
+---------------------------------------------+
```

## Core Standard

The core standard defines only **phases** - the universal state categories. All concrete statuses come from industry standards or custom definitions.

### Phases

| Phase | Terminal | Description |
|-------|----------|-------------|
| `pending` | No | Job accepted, work not started |
| `active` | No | Work in progress |
| `completed` | Yes | Successfully finished |
| `failed` | Yes | Unsuccessfully finished |

### Rules

- Every status (from any standard or custom) must map to exactly one phase
- Clients can always determine basic state from phase, even for unknown statuses
- Phase transitions follow: `pending` -> `active` -> `completed` | `failed`

### Schema

```json
{
  "$id": "https://localprotocol.xyz/standards/delivery/core.json",
  "name": "xyz.localprotocol.delivery.core",
  "version": "1.0.0",

  "phases": {
    "pending":   {"terminal": false, "description": "Job accepted, work not started"},
    "active":    {"terminal": false, "description": "Work in progress"},
    "completed": {"terminal": true,  "description": "Successfully finished"},
    "failed":    {"terminal": true,  "description": "Unsuccessfully finished"}
  }
}
```

## Industry Standards

Industry standards define concrete statuses for specific domains. They are governed by the protocol, industry consortiums, or recognized working groups.

### Standard Structure

```json
{
  "$id": "https://localprotocol.xyz/standards/delivery/food.json",
  "name": "xyz.localprotocol.delivery.food",
  "version": "1.0.0",
  "protocol": "xyz.localprotocol.delivery.core@1.0.0",
  "spec": "https://localprotocol.xyz/spec/delivery/food",

  "title": "Food Delivery Standard",
  "description": "Status vocabulary for restaurant and food delivery",

  "statuses": {
    "order_placed":       {"phase": "pending",   "description": "Order received by merchant"},
    "preparing":          {"phase": "active",    "description": "Merchant preparing order"},
    "ready_for_pickup":   {"phase": "active",    "description": "Order ready, awaiting courier"},
    "courier_assigned":   {"phase": "active",    "description": "Courier assigned to delivery"},
    "courier_at_pickup":  {"phase": "active",    "description": "Courier arrived at merchant"},
    "picked_up":          {"phase": "active",    "description": "Courier collected order"},
    "in_transit":         {"phase": "active",    "description": "Courier en route to customer"},
    "courier_at_dropoff": {"phase": "active",    "description": "Courier arrived at customer"},
    "delivered":          {"phase": "completed", "description": "Order delivered to customer"},
    "canceled":           {"phase": "failed",    "description": "Delivery canceled"},
    "failed":             {"phase": "failed",    "description": "Delivery attempt unsuccessful"}
  }
}
```

### Requirements

- Must reference core protocol version via `protocol` field
- Must map every status to a core phase
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
| Add new status | Minor | `1.0.0` -> `1.1.0` |
| Add optional field to status | Minor | `1.0.0` -> `1.1.0` |
| Fix description typo | Patch | `1.0.0` -> `1.0.1` |
| Remove a status | **Major** | `1.0.0` -> `2.0.0` |
| Change a status's phase | **Major** | `1.0.0` -> `2.0.0` |
| Rename a status ID | **Major** | `1.0.0` -> `2.0.0` |
| Change required field to optional | **Major** | `1.0.0` -> `2.0.0` |

### Compatibility Rules

- **Patch versions** are always backward compatible
- **Minor versions** are backward compatible (clients handle unknown statuses via phase)
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
      ],

      "custom_statuses": {
        "driver_finishing_nearby_order": {
          "phase": "active",
          "description": "Driver completing adjacent delivery first"
        }
      }
    }
  }
}
```

### Fields

| Field | Required | Description |
|-------|----------|-------------|
| `version` | Yes | Provider's capability version |
| `conforms_to` | Yes | Array of standards (with versions) provider implements |
| `custom_statuses` | No | Provider-specific statuses (must include phase) |

### Rules

- Provider MUST fully implement all statuses in declared standards
- Provider MAY define custom statuses with `phase` and `description`
- Custom statuses are not expected to interoperate
- Clients check `conforms_to` to determine compatibility

## Delivery Object

When a provider returns a delivery object, it includes status information.

### Structure

```json
{
  "id": "del_789",
  "status": "courier_at_pickup",
  "phase": "active",
  "status_description": "Courier arrived at merchant",
  "status_vocabulary": "xyz.localprotocol.delivery.food@1.2.0",
  "updated_at": "2026-01-30T19:12:00Z"
}
```

### Fields

| Field | Required | Description |
|-------|----------|-------------|
| `status` | Yes | Current status ID |
| `phase` | Yes | Core phase (`pending`, `active`, `completed`, `failed`) |
| `status_description` | Yes | Human-readable description |
| `status_vocabulary` | No | Which standard defines this status (omit if custom) |
| `updated_at` | Yes | When status last changed (RFC 3339) |

### Why Include Phase Explicitly?

- Clients can always determine basic state without fetching vocabulary schemas
- Handles unknown/custom statuses gracefully
- No lookup required for basic UI (progress indicators, terminal detection)

### Custom Status Example

```json
{
  "id": "del_789",
  "status": "driver_finishing_nearby_order",
  "phase": "active",
  "status_description": "Driver completing adjacent delivery first",
  "updated_at": "2026-01-30T19:08:00Z"
}
```

No `status_vocabulary` indicates this is a provider-specific custom status.

## Future Considerations

The following topics are out of scope for this design but may be addressed later:

- **Job object structure** - Fields on an accepted delivery (assignee, tracking URL, etc.)
- **Cancellation rules** - Who can cancel, when, penalties/fees
- **Communication transport** - How updates are delivered (webhooks, polling, both)
- **Proof of delivery** - Signatures, photos, confirmation
- **Real-time tracking** - Driver location updates, ETA recalculation
