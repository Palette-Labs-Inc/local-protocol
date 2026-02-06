# Catalog

The Catalog capability defines a canonical catalog graph with category-based presentation. This supports POS and commerce platform ingest, customer-facing apps, and downstream integrations without duplicating core data.

## Design Goals

- Interoperate with major POS systems and commerce platforms.
- Support multiple catalogs per business/merchant.
- Provide a UI-ready category structure without duplicating canonical data.
- Keep modifiers reusable and compatible with POS reference models.
- Allow availability at catalog, category, or item level, with catalog taking precedence.

## Core Model

- A **canonical catalog graph** contains reusable objects: catalogs, categories, items, modifier groups, modifier options, and modifier items.
- Catalogs order categories via `category_ids`, categories order items via `item_ids`, and parent categories order nested categories via `child_category_ids`.
- Categories may be nested with `parent_category_id` when a hierarchy is needed.
- Provider-specific fields that are not modeled natively belong in `metadata`.
- Items may appear directly in a catalog via `item_ids` without category membership. If a UI or storage system requires a category, place these items into a synthetic category (for example, "Items" or "Uncategorized").
- Fulfillment modes use canonical values (`DELIVERY`, `PICKUP`, `DINE_IN`), with custom values allowed when needed.

## Canonical Objects

- `schemas/inventory/merchant.json` is the top-level payload containing all catalog objects.
- `schemas/inventory/catalog.json` defines catalogs and their membership.
- `schemas/inventory/types/category.json` defines categories and ordered item membership.
- `schemas/inventory/types/item.json` defines items and modifier group references.
- `schemas/inventory/types/modifier_group.json` defines selection constraints and option membership.
- `schemas/inventory/types/modifier_option.json` defines option nodes referencing modifier items.
- `schemas/inventory/types/modifier_item.json` defines purchasable modifier items.
- `schemas/inventory/types/modifier_group_override.json` defines item-level overrides for modifier groups.

## Availability

- `schemas/inventory/types/availability.json` and `schemas/inventory/types/interval.json` define weekly and date-specific schedules.
- Availability may be defined on a catalog, category, or item.
- If a catalog defines availability, it overrides category and item availability.
- If a category defines availability, it overrides item availability.

Intervals are neutral and can be reused by closure schedules.

## Source of Truth and Platform Pricing

- The merchant/business (or its delegate, such as a POS, ERP, or PIM) is the source of truth for catalog data.
- Platforms or marketplaces that mirror those catalogs may apply markups, discounts, or fees.
- Those platform-specific pricing adjustments are modeled **separately** from the catalog itself (e.g., in checkout totals/adjustments), not by mutating canonical item prices.
- If a business intentionally sets different base prices per platform, represent them as distinct catalogs with their own item prices.
