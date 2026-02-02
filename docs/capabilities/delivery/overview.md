# Delivery

The Delivery capability defines objects for negotiating and fulfilling point-to-point delivery work between a requester and a provider. It focuses on simple, composable primitives that can be exchanged over the protocol and extended as needed.

## Core Objects

- **Ask**: A requester-defined job, including pickup/dropoff locations and requested times.
- **Bid**: A provider-defined offer to complete the job, including price, locations, and estimated timing.

## Event Standards

Event standards define the event vocabularies providers use to communicate delivery progress. The system uses a conformance-based model:

- **Industry standards**: Protocol-governed vocabularies (e.g., `xyz.localprotocol.delivery.courier`).
- **Custom standards**: Provider-defined vocabularies (e.g., `com.acme.delivery.courier`).
- **Extensions**: Standards can extend a single parent standard by referencing `name@version` in `extends` for lineage and discovery. The child standard must list the full event vocabulary (including inherited events) in `events`.

Providers declare which standards they implement in their profile under the delivery capability `config.conforms_to` for discovery; the standard's `events` map is the declaration of conformance and is read directly (no chain traversal required).

See [Event Standards](standards/overview.md) for details.
