# Event Standards

Event standards define how delivery providers communicate job progress. The system uses a conformance-based model:

- **Core**: Required events that all providers must support (pending, active, completed, failed).
- **Standards**: Event vocabularies that extend core with domain-specific events.

## Enforcement Mechanism

All standards must include core events. This is enforced via JSON Schema - the `events` object requires `pending`, `active`, `completed`, and `failed` keys.

```json
{
  "events": {
    "required": ["pending", "active", "completed", "failed"]
  }
}
```

This ensures any client that understands core can work with any conforming standard.

## How It Works

1. **Core defines events**: Universal events that every standard must include.
2. **Standards extend core**: Domain-specific events alongside required core events.
3. **Providers declare conformance**: Providers list which standards they implement in their profile.
4. **Clients check compatibility**: Clients verify providers conform to required standards.

## Standards

Standards can be:

- **Industry standards**: Governed by the protocol or industry consortiums (e.g., `xyz.localprotocol.delivery.food`)
- **Custom standards**: Defined by individual providers (e.g., `com.acme.delivery.custom`)

Both follow the same format, must reference core via the `protocol` field, and must include core events.

```
+---------------------------------------------+
|  Custom Standards (provider-defined)        |
+---------------------------------------------+
|  Industry Standards (protocol-governed)     |
+---------------------------------------------+
|  Core (required)                            |
+---------------------------------------------+
```

## Why Everything Is a Standard

By using the same format for custom and industry standards, custom standards become:

- **Discoverable**: Clients can fetch and understand any provider's event vocabulary
- **Reusable**: Other providers can adopt a custom standard
- **Evolvable**: Popular custom standards can be promoted to industry standards
- **Interoperable**: Providers using the same standard are automatically compatible

This creates a path from experimentation to standardization.

## Versioning

Standards use [Semantic Versioning](https://semver.org/):

- **Major**: Breaking changes (removing events)
- **Minor**: Backward-compatible additions (new events)
- **Patch**: Non-functional changes (description fixes)

## Available Standards

- [Core](core.md): Universal events (required)
- [Food](food.md): Restaurant and food delivery
