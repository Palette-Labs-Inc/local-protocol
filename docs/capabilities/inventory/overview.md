# Inventory

The Inventory capability defines a canonical catalog graph plus presentation-only menu trees. This supports POS ingest, customer-facing apps, and downstream integrations without duplicating core data.

## Design Goals

- Interoperate with major POS systems (Toast, Square, Google menus).
- Support multiple catalogs per merchant.
- Provide a UI-ready menu tree without duplicating canonical data.
- Keep modifiers reusable and compatible with POS reference models.
- Allow availability at menu or item level, with menu taking precedence.

## Core Model

- A **canonical catalog graph** contains reusable objects: catalogs, categories, items, modifier groups, modifier options, and modifier items.
- A **menu view** is a presentation-only tree that references canonical items for navigation and display.
- Provider identifiers are preserved via `external_ids` on every object.
- Provider-specific fields that are not modeled natively belong in `metadata`.

## Canonical Objects

- `schemas/inventory/merchant.json` is the top-level payload containing all catalog objects and menu views.
- `schemas/inventory/catalog.json` defines catalogs and their membership.
- `schemas/inventory/types/category.json` defines categories and ordered item membership.
- `schemas/inventory/types/item.json` defines items and modifier group references.
- `schemas/inventory/types/modifier_group.json` defines selection constraints and option membership.
- `schemas/inventory/types/modifier_option.json` defines option nodes referencing modifier items.
- `schemas/inventory/types/modifier_item.json` defines purchasable modifier items.

## Menu Views

- `schemas/inventory/menu_view.json` defines a presentation-only tree that references canonical items.
- `schemas/inventory/types/menu_group.json` groups child nodes for navigation.
- `schemas/inventory/types/menu_item_ref.json` references a canonical item.
- `schemas/inventory/types/menu_node.json` is the union of group and item nodes.

Menu views are not authoritative for price or description. They exist to structure and order items for UI display.

## Availability

- `schemas/inventory/types/availability.json` and `interval.json` define weekly and date-specific schedules.
- Availability may be defined on a menu view or an item.
- If a menu view defines availability, it overrides item availability.
Intervals are neutral and can be reused by closure schedules.

## Source of Truth and Platform Pricing

- The merchant (or its delegate, such as a POS) is the source of truth for catalog data.
- Platforms or businesses mirroring those menus (Uber Eats, DoorDash, Grubhub, etc.) may apply markups, discounts, or fees.
- Those platform-specific pricing adjustments are modeled **separately** from the catalog itself (e.g., in checkout totals/adjustments), not by mutating canonical item prices.
- If a merchant intentionally sets different base prices per platform, that should be represented as distinct catalogs with their own item prices.

## Provider Compatibility

| Provider | Mapping Notes |
| --- | --- |
| Toast v3 | `menuGroups` map to `menu_view.tree`; reference maps become canonical modifier objects; identifiers stored in `external_ids`. |
| Square | `CatalogItem` → item; `CatalogModifierList` → modifier_group; `CatalogModifier` → modifier_item; constraints map to modifier group limits. |
| Google FoodMenus | menus/sections/items map to `menu_view`/`menu_group`/`menu_item_ref`; rich attributes preserved in `metadata`. |

## Toast v3 Alignment (Why the Hybrid Model)

Toast’s menus v3 payload includes both:
- **A hierarchical presentation tree** via `menus -> menuGroups -> menuGroups/menuItems` (nested menu groups).
- **Canonical reference maps** for modifiers using `referenceId` values (menu items link to modifier groups by reference, and modifier groups link to modifier options by reference).

This creates two distinct kinds of data:
- **Structure and ordering** (best represented as a menu tree).
- **Reusable entities** (best represented as canonical objects with references).

That’s why Local Protocol keeps **both** canonical catalog objects and a **presentation-only** `menu_view` tree:
- The menu tree preserves Toast’s nested grouping and ordering.
- The canonical objects preserve reusable items/modifiers and map cleanly to Toast’s reference maps.
- Provider identifiers like `guid`, `referenceId`, and `multiLocationId` remain intact via `external_ids`, so multi-location versions and POS IDs are not lost.

## Decision Record

See `DECISIONS.md` for the full requirements-to-decisions trace.
