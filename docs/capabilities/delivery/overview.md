# Delivery

The Delivery capability defines objects for negotiating and fulfilling point-to-point delivery work between a requester and a provider. It focuses on simple, composable primitives that can be exchanged over the protocol and extended as needed.

## Core Objects

- **Ask**: A requester-defined job, including pickup/dropoff locations and requested times.
- **Bid**: A provider-defined offer to complete the job, including price, locations, and estimated timing.

## Event Standards

Event standards define how providers communicate delivery progress. The system uses a conformance-based model:

- **Core**: Universal events all providers must support (pending, active, completed, failed).
- **Standards**: Event vocabularies for specific domains. Can be industry standards (e.g., `xyz.localprotocol.delivery.food`) or custom standards defined by providers.

See [Event Standards](standards/overview.md) for details.
