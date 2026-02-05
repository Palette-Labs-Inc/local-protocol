# Inventory

The Inventory capability defines a canonical catalog graph with category-based presentation. This supports POS ingest, customer-facing apps, and downstream integrations without duplicating core data.

## Design Goals

- Interoperate with major POS systems (Toast, Square, Google menus).
- Support multiple catalogs per merchant.
- Provide a UI-ready category structure without duplicating canonical data.
- Keep modifiers reusable and compatible with POS reference models.
- Allow availability at catalog or item level, with catalog taking precedence.

## Core Model

- A **canonical catalog graph** contains reusable objects: catalogs, categories, items, modifier groups, modifier options, and modifier items.
- Catalogs order categories via `category_ids`, categories order items via `item_ids`, and parent categories order nested categories via `child_category_ids`.
- Categories may be nested with `parent_category_id` when a hierarchy is needed.
- Provider-specific fields that are not modeled natively belong in `metadata`.

## Canonical Objects

- `schemas/inventory/merchant.json` is the top-level payload containing all catalog objects.
- `schemas/inventory/catalog.json` defines catalogs and their membership.
- `schemas/inventory/types/category.json` defines categories and ordered item membership.
- `schemas/inventory/types/item.json` defines items and modifier group references.
- `schemas/inventory/types/modifier_group.json` defines selection constraints and option membership.
- `schemas/inventory/types/modifier_option.json` defines option nodes referencing modifier items.
- `schemas/inventory/types/modifier_item.json` defines purchasable modifier items.

## Availability

- `schemas/inventory/types/availability.json` and `schemas/inventory/types/interval.json` define weekly and date-specific schedules.
- Availability may be defined on a catalog or an item.
- If a catalog defines availability, it overrides item availability.

Intervals are neutral and can be reused by closure schedules.

## Source of Truth and Platform Pricing

- The merchant (or its delegate, such as a POS) is the source of truth for catalog data.
- Platforms or businesses mirroring those menus (Uber Eats, DoorDash, Grubhub, etc.) may apply markups, discounts, or fees.
- Those platform-specific pricing adjustments are modeled **separately** from the catalog itself (e.g., in checkout totals/adjustments), not by mutating canonical item prices.
- If a merchant intentionally sets different base prices per platform, that should be represented as distinct catalogs with their own item prices.

## Provider Compatibility

| Provider | Mapping Notes |
| --- | --- |
| Toast v3 | `menus` map to catalogs; `menuGroups` map to categories; nested groups map to `parent_category_id`. |
| Square | `CatalogItem` → item; `CatalogModifierList` → modifier_group; `CatalogModifier` → modifier_item; constraints map to modifier group limits. |
| Google FoodMenus | menus/sections/items map to catalog/category/item; rich attributes preserved in `metadata`. |

## Toast v3 Alignment (Without Menu Views)

Toast’s v3 model is a menu tree with nested groups. In the simplified model:
- `menus` map to catalogs.
- `menuGroups` map to categories.
- Nested groups map to `parent_category_id`.
- Menu item ordering is represented by `item_ids` within each category.

## Decision Record

See `DECISIONS.md` for the full requirements-to-decisions trace.
