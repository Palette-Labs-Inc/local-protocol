# Delivery

The Delivery capability defines objects for negotiating and fulfilling point-to-point delivery work between a requester and a provider. It focuses on simple, composable primitives that can be exchanged over the protocol and extended as needed.

## Core Objects

- **Ask**: A requester-defined job, including pickup/dropoff locations and requested times.
- **Bid**: A provider-defined offer to complete the job, including price, locations, and estimated timing.

## Event Standards

Event standards define the event vocabularies providers use to communicate delivery progress. The system uses a conformance-based model:

- **Industry standards**: Protocol-governed vocabularies (e.g., `xyz.localprotocol.delivery.food`).
- **Custom standards**: Provider-defined vocabularies (e.g., `com.acme.delivery.custom`).
- **Extensions**: Standards can extend other standards by referencing `name@version` in `extends` and adding events.

Providers declare which standards they implement in their profile; clients can merge events across the extension chain.
Core is optional and may be used as a shared baseline.

See [Event Standards](standards/overview.md) for details.
