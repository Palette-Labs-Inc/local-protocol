# Decision Log

Short, LLM-friendly record of notable decisions in this repo.

## 2026-01-30

- Renamed delivery objects: DeliveryRequest → Ask and DeliveryQuote → Bid.
- Times use estimates without explicit deadlines; revisit if we add expiry/valid-until later.
- Location requires a postal address (UCP `postal_address`) and allows optional coordinates (`lat`, `lng`), covering house, roadside, and ambiguous-front-door cases.
- Delivery pricing uses UCP-style fields: `price` in minor units with separate `currency` (ISO 4217).
