# Delivery

The Delivery capability defines objects for negotiating and fulfilling point-to-point delivery work between a requester and a provider. It focuses on simple, composable primitives that can be exchanged over the protocol and extended as needed.

Core objects:

- **Ask**: A requester-defined job, including pickup/dropoff locations and requested times.
- **Bid**: A provider-defined offer to complete the job, including price, locations, and estimated timing.
