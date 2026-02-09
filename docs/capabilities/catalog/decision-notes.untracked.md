# Inventory Decision Notes (Untracked)

This file is intentionally untracked. It contains the detailed rationale, examples, and compatibility notes that were removed from `DECISIONS.md` to keep the decision log concise.

## Rationale

- Normalized catalog objects preserve cross-menu reuse and provider mappings.
- Presentation trees stay UI-friendly without duplicating canonical data.
- First-class modifier options align with Square and Toast reference-style models.

## Options Considered

- Pure hierarchical menu tree (Toast-style nested groups/items). Rejected due to poor reuse across menus and weaker POS mapping.
- Fully normalized catalog without menu views (Square-style only). Rejected because UI needs a stable presentation tree.
- Embedded modifier options in modifier groups. Rejected because it complicates provider mapping and reuse.

## Why These Rejections

- Pure hierarchical menu tree:
  - Reuse problem: the same item in two menus is duplicated with separate copies, so a price or description update requires multi-place edits.
  - Provider mapping issue: Toast/Square expose canonical item and modifier identifiers; embedding forces ad-hoc ID generation or duplication.
  - Example: a “Lunch Burger” and “Dinner Burger” end up as two separate embedded objects even when they should be the same item.
- Fully normalized without menu views:
  - UI/ordering needs explicit grouping and ordering that normalized graphs alone do not provide.
  - Without a menu tree, clients must invent a presentation model (e.g., infer categories only), which differs across consumers.
  - Example: two menus can share the same items but must render differently (seasonal ordering, curated groupings); normalized-only can’t represent that without a view.
- Embedded modifier options:
  - Reuse problem: the same modifier item (e.g., “Cheddar”) used in multiple groups requires copying the option data in each group.
  - Provider mapping issue: Toast and Square treat options as first-class references. Embedding loses stable option identifiers and breaks direct mapping.
  - Example: “Cheddar” is default in “Burger Add-ons” but not in “Salad Add-ons”. With embedded options you must duplicate the option for each group; with a separate option object you can vary `is_default` per group (by using different option IDs pointing to the same modifier item) without duplicating the modifier item itself.

## Concrete Example (Embedded vs Separate)

- Embedded option (duplication):
  - Group A options: `{ name: "Cheddar", price: 100, is_default: true }`
  - Group B options: `{ name: "Cheddar", price: 100, is_default: false }`
  - Result: two separate copies of “Cheddar” that must be updated in lockstep.
- Separate option + item (reuse):
  - Modifier item: `{ id: "mi_cheddar", name: "Cheddar", price: 100 }`
  - Option A: `{ id: "mo_cheddar_default", modifier_item_id: "mi_cheddar", is_default: true }`
  - Option B: `{ id: "mo_cheddar_optional", modifier_item_id: "mi_cheddar", is_default: false }`
  - Result: one canonical modifier item; options express per-group behavior without duplicating the purchasable item.

## Compatibility Notes

- Toast v3: `menus` + nested `menuGroups` map to `menu_view.tree`; `modifierGroupReferences`/`modifierOptionReferences` map to canonical modifier objects; Toast identifiers stored in `external_ids`.
- Square: `CatalogItem` → item; `CatalogModifierList` → modifier_group; `CatalogModifier` → modifier_item; `CatalogItemModifierListInfo` → modifier_group constraints; Square IDs stored in `external_ids`.
- Google FoodMenus: menus/sections/items map to `menu_view`/`menu_group`/`menu_item_ref`; richer nutrition/allergen fields retained in `metadata`.

## Consequences

- Ingesters must build both canonical catalog objects and one or more menu views.
- Presentation trees are not authoritative for price or description; they only reference canonical items.
- UIs can render menu views without joining across the full catalog graph.
- Provider-specific features not modeled natively are preserved in `metadata` and `external_ids`.

## Non-goals (for v1)

- Localization support for menu fields.
- Item variants as first-class objects (modeled via modifier groups instead).
- Full POS scheduling semantics beyond weekly intervals.

## Open Questions

- Should `menu_view` allow per-node overrides (e.g., display name) or stay pure references?
- Do we need a standard enum for fulfillment modes or keep them free-form strings?
