# Decision Log

Short, LLM-friendly record of notable decisions in this repo.

## 2026-01-30

- Renamed delivery objects: DeliveryRequest → Ask and DeliveryQuote → Bid.
- Times use estimates without explicit deadlines; revisit if we add expiry/valid-until later.
- Location requires at least one of postal address (UCP `postal_address`) or coordinates (`lat`, `lng`), covering house, roadside, and ambiguous-front-door cases.
- Delivery pricing uses UCP-style fields: `price` in minor units with separate `currency` (ISO 4217).
- We debated forcing payments through crypto. Since only "lost" money (network fees, processing fees, etc.) conveys meaningful signal about transaction value, requiring crypto isn't necessary. We can always later say "if you want better rewards, use crypto rails."
- Protocol fees are going to be the only meaningful sybil resistance mechanism we have, so we'll need to incorporate them sooner rather than later.
