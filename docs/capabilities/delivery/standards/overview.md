# Status Standards

Status standards define how delivery providers communicate job progress. The system uses a conformance-based model with three layers:

- **Core**: Required phases that all providers must support (pending, active, completed, failed).
- **Industry Standards**: Domain-specific status vocabularies that providers opt into.
- **Custom Statuses**: Provider-specific statuses that are not expected to interoperate.

## How It Works

1. **Core defines phases**: Universal state categories that every status maps to.
2. **Industry standards define statuses**: Concrete status vocabularies for specific domains (e.g., food delivery).
3. **Providers declare conformance**: Providers list which standards they implement in their profile.
4. **Clients check compatibility**: Clients verify providers conform to required standards.

## Conformance Model

If a provider declares conformance to a standard, clients can rely on that standard's statuses being implemented correctly. All statuses (including custom) must map to a core phase, ensuring clients can always determine basic state.

```
+---------------------------------------------+
|  Custom (provider-specific)                 |
+---------------------------------------------+
|  Industry Standards (opt-in)                |
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
