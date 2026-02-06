# Decision Log

Short, LLM-friendly record of notable decisions in this repo.

## 2026-01-30

- Renamed delivery objects: DeliveryRequest → Request and DeliveryQuote → Quote.
- Times use estimates without explicit deadlines; revisit if we add expiry/valid-until later.
- Location requires at least one of postal address (UCP `postal_address`) or coordinates (`latitude`, `longitude`), covering house, roadside, and ambiguous-front-door cases.
- Delivery pricing uses UCP-style fields: `price` in minor units with separate `currency` (ISO 4217).
- We debated forcing payments through crypto. Since only "lost" money (network fees, processing fees, etc.) conveys meaningful signal about transaction value, requiring crypto isn't necessary. We can always later say "if you want better rewards, use crypto rails."
- Protocol fees are going to be the only meaningful sybil resistance mechanism we have, so we'll need to incorporate them sooner rather than later.

## 2026-02-05

Decisions
- Adopt a catalog + category model aligned with Square-style catalogs and the backend schema.
- Keep catalog objects normalized (items, categories, modifier groups, modifier options, modifier items).
- Use ordered `category_ids` and `item_ids` lists for presentation instead of a separate menu tree.
- Allow nested categories via `parent_category_id` when needed.
- Encode modifier options separately from modifier groups (option → modifier item).
- Allow item availability but override it with catalog availability when present.

## 2026-02-06

Decisions
- Switch inventory catalog models to denormalized, embedded objects (catalogs contain categories/items; items contain modifier groups/options/items).
- Use array order for category, item, and modifier ordering instead of `*_ids` membership lists.
- Keep ids on embedded objects for provider mapping, but do not require cross-object references.
- Drop modifier group overrides; item-level differences are expressed by embedding the final group definition.
