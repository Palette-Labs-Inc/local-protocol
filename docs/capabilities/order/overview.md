# Order

The Order capability defines objects for requesting, quoting, and confirming work to have something readied for a requester.

## Objects

- **[Cart](cart.md)**: A collection of items aggregated with intent to order.
- **[Request](request.md)**: A requester-defined intent to have something prepared.
- **[Quote](quote.md)**: A provider-defined offer including price and readiness timing.
- **[Order](order.md)**: A confirmed request backed by payment.

## Lifecycle

Cart → Request → Quote → Order

## API

See [API](api.md) for the minimal endpoints, idempotency rules, and errors.
