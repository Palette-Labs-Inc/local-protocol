# Event Standards

Event standards define event vocabularies for delivery domains. The system uses a conformance-based model:

- **Industry standards**: Governed by the protocol or industry consortiums (e.g., `xyz.localprotocol.delivery.food`).
- **Custom standards**: Defined by individual providers (e.g., `com.acme.delivery.custom`).

## How It Works

1. **Standards define events**: Each standard lists the events it defines.
2. **Extensions add events**: A standard can extend one or more parent standards by referencing `name@version` in `extends`.
3. **Providers declare conformance**: Providers list which standards they implement in their profile.
4. **Clients merge vocabularies**: Clients compute the full event set by merging events across the extension chain.

## Extensions

Extensions must reference semver versions of the standards they extend:

```json
{
  "extends": [
    "xyz.localprotocol.delivery.core@1.0.0",
    "xyz.localprotocol.delivery.food@1.0.0"
  ]
}
```

## Core Standard (Optional)

The protocol provides a minimal core standard that other standards may extend. Core is optional but provides a shared baseline for interoperability.
Standards may extend core, extend other standards, or define events without extending anything.

## Versioning

Standards use [Semantic Versioning](https://semver.org/):

- **Major**: Breaking changes (removing events)
- **Minor**: Backward-compatible additions (new events)
- **Patch**: Non-functional changes (description fixes)

## Available Standards

- [Core](core.md): Minimal universal events (optional baseline)
- [Food](food.md): Restaurant and food delivery
