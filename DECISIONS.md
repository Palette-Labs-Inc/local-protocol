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

Requirements
- Universal commerce support for customers, POS ingest, and downstream integrations.
- Multiple catalogs per restaurant.
- Presentation-only menu trees for UI navigation.
- Modifier options as first-class objects, not embedded in groups.
- Compatibility with Toast, Square, and other POS providers.
- Restaurant is the source of truth, with mirrors/delegates (POS, apps).
- Availability may be defined at menu or item level, with menu taking precedence.

Decisions
- Adopt a hybrid model: canonical catalog graph plus presentation-only menu views.
- Keep catalog objects normalized (items, categories, modifier groups, modifier options, modifier items).
- Model menu trees as `menu_view` nodes that reference canonical items.
- Encode modifier options separately from modifier groups (option → modifier item).
- Include `external_ids` on all objects to preserve provider identifiers.
- Allow item availability but override it with menu-level availability when present.

Rationale
- Normalized catalog objects preserve cross-menu reuse and provider mappings.
- Presentation trees stay UI-friendly without duplicating canonical data.
- First-class modifier options align with Square and Toast reference-style models.

Options Considered
- Pure hierarchical menu tree (Toast-style nested groups/items). Rejected due to poor reuse across menus and weaker POS mapping.
- Fully normalized catalog without menu views (Square-style only). Rejected because UI needs a stable presentation tree.
- Embedded modifier options in modifier groups. Rejected because it complicates provider mapping and reuse.

Compatibility Notes
- Toast v3: `menus` + nested `menuGroups` map to `menu_view.tree`; `modifierGroupReferences`/`modifierOptionReferences` map to canonical modifier objects; Toast identifiers stored in `external_ids`.
- Square: `CatalogItem` → item; `CatalogModifierList` → modifier_group; `CatalogModifier` → modifier_item; `CatalogItemModifierListInfo` → modifier_group constraints; Square IDs stored in `external_ids`.
- Google FoodMenus: menus/sections/items map to `menu_view`/`menu_group`/`menu_item_ref`; richer nutrition/allergen fields retained in `metadata`.

Consequences
- Ingesters must build both canonical catalog objects and one or more menu views.
- Presentation trees are not authoritative for price or description; they only reference canonical items.
- UIs can render menu views without joining across the full catalog graph.
- Provider-specific features not modeled natively are preserved in `metadata` and `external_ids`.

Non-goals (for v1)
- Localization support for menu fields.
- Item variants as first-class objects (modeled via modifier groups instead).
- Full POS scheduling semantics beyond weekly intervals.

Open Questions
- Should `menu_view` allow per-node overrides (e.g., display name) or stay pure references?
- Do we need a standard enum for fulfillment modes or keep them free-form strings?
