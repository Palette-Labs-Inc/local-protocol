# Event Standards

Event standards define event vocabularies for delivery domains. The system uses a conformance-based model:

- **Industry standards**: Governed by the protocol or industry consortiums (e.g., `xyz.localprotocol.delivery.food`).
- **Custom standards**: Defined by individual providers (e.g., `com.acme.delivery.custom`).

## How It Works

1. **Standards define events**: Each standard lists its full event vocabulary in `events` (including inherited events).
2. **Extensions add lineage**: A standard can extend a single parent standard by referencing `name@version` in `extends`.
3. **Providers declare conformance**: Providers list which standards they implement in their profile capability `config.conforms_to` for discovery.
4. **Clients read events directly**: Clients fetch the standard and use its `events` map; no recursive traversal is required.

## Repository Structure

The repository separates validation rules from standard definitions:

| Path | Purpose |
|------|---------|
| `schemas/delivery/standards/standard.json` | Shared JSON Schema that validates any delivery standard |
| `standards/delivery/*.json` | Actual standard documents (instance data) |

The schema defines *what a valid standard looks like* (required fields, types, patterns). The standard files *are* the standards themselves and serve as the source of truth for event vocabularies. There is one shared schema for all standards rather than per-standard schemas, since the standard documents already declare their event vocabularies.

## Extensions

Extensions must reference a version date of the single parent they extend:

```json
{
  "extends": ["xyz.localprotocol.delivery.core@2026-01-30"]
}
```

## Materialized Vocabularies

- The `events` map is the standard's declaration of conformance and must be complete, including any inherited events.
- `extends` indicates lineage and compatibility for discovery; it is not required to compute the vocabulary.
- If a child standard redefines an event ID from its parent, the child definition is authoritative.

## Core Standard (Optional)

The protocol provides a minimal core standard that other standards may extend. Core is optional but provides a shared baseline for interoperability.
Standards may extend core or another single parent standard, or define events without extending anything.

## Versioning

Standards use date-based versioning in `YYYY-MM-DD` format, consistent with UCP. Each version represents a snapshot of the standard on that date. Breaking changes require a new version date.

## Available Standards

- [Core](core.md): Minimal universal events (optional baseline)
- [Food](food.md): Restaurant and food delivery
