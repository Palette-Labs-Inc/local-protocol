# Decision Log

Short, LLM-friendly record of notable decisions in this repo.

## 2026-01-30

- Renamed delivery objects: DeliveryRequest → Ask and DeliveryQuote → Bid.
- Times use estimates without explicit deadlines; revisit if we add expiry/valid-until later.
- Location requires coordinates (`lat`, `lng`) and allows optional postal address (UCP `postal_address`), covering house, roadside, and ambiguous-front-door cases.
- Delivery pricing uses UCP-style fields: `price` in minor units with separate `currency` (ISO 4217).
- DeliveryBid includes `pickup_estimate` / `dropoff_estimate`; DeliveryAsk includes `pickup_time` / `dropoff_time` (RFC 3339).
- Docs: capability docs live under `docs/capabilities/` with Delivery grouped into Objects (Bid, Ask) and Types (Location, Coordinates).
