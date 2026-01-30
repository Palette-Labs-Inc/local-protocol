# Status Standards

Status standards define how delivery providers communicate job progress. The system uses a conformance-based model with two layers:

- **Core**: Required phases that all providers must support (pending, active, completed, failed).
- **Standards**: Status vocabularies that map to core phases. Can be industry standards or custom standards.

## How It Works

1. **Core defines phases**: Universal state categories that every status maps to.
2. **Standards define statuses**: Concrete status vocabularies for specific domains.
3. **Providers declare conformance**: Providers list which standards they implement in their profile.
4. **Clients check compatibility**: Clients verify providers conform to required standards.

## Standards

Standards can be:

- **Industry standards**: Governed by the protocol or industry consortiums (e.g., `xyz.localprotocol.delivery.food`)
- **Custom standards**: Defined by individual providers (e.g., `com.acme.delivery.custom`)

Both follow the same format and must reference core via the `protocol` field.

```
+---------------------------------------------+
|  Custom Standards (provider-defined)        |
+---------------------------------------------+
|  Industry Standards (protocol-governed)     |
+---------------------------------------------+
|  Core (required)                            |
+---------------------------------------------+
```

## Versioning

Standards use [Semantic Versioning](https://semver.org/):

- **Major**: Breaking changes (removing statuses, changing phases)
- **Minor**: Backward-compatible additions (new statuses)
- **Patch**: Non-functional changes (description fixes)

## Available Standards

- [Core](core.md): Universal phases (required)
- [Food](food.md): Restaurant and food delivery
