# Catalog

The Catalog capability defines a denormalized catalog tree with category-based presentation. This supports POS and commerce platform ingest, customer-facing apps, and downstream integrations without joining across a separate canonical object graph.

## Design Goals

- Interoperate with major POS systems and commerce platforms.
- Support multiple catalogs per business/merchant.
- Provide a UI-ready category tree with embedded items and modifiers.
- Keep modifier configuration self-contained for each item.
- Allow availability at catalog, category, or item level, with catalog taking precedence.

## Core Model

- Merchant payloads contain catalogs, and each catalog embeds categories and items directly.
- Catalogs order categories via array order, categories order items via their `items` array, and nested categories are represented by `categories` on each category.
- Items embed modifier groups, modifier groups embed modifier options, and modifier options embed modifier items.
- Provider-specific fields that are not modeled natively belong in `metadata`.
- Items may appear directly in a catalog via `items` without category membership. If a UI or storage system requires a category, place these items into a synthetic category (for example, "Items" or "Uncategorized").
- Fulfillment modes are set on `Catalog.fulfillment_modes` (array of strings). Canonical values are `DELIVERY`, `PICKUP`, `DINE_IN`; custom values are allowed when needed.

## Schema Files

- `schemas/inventory/merchant.json` is the top-level payload.
- `schemas/inventory/catalog.json` defines catalogs and their embedded categories/items.
- `schemas/inventory/types/category.json` defines categories, child categories, and ordered item membership.
- `schemas/inventory/types/item.json` defines items and embedded modifier groups.
- `schemas/inventory/types/modifier_group.json` defines selection constraints and embedded modifier options.
- `schemas/inventory/types/modifier_option.json` defines option nodes and embedded modifier items.
- `schemas/inventory/types/modifier_item.json` defines purchasable modifier items.

## Availability

- `schemas/inventory/types/availability.json` and `schemas/inventory/types/interval.json` define weekly and date-specific schedules.
- Availability may be defined on a catalog, category, or item.
- If a catalog defines availability, it overrides category and item availability.
- If a category defines availability, it overrides item availability.

Intervals are neutral and can be reused by closure schedules (recurring unavailability windows applied at the merchant or location level).

## Source of Truth and Platform Pricing

- The merchant/business (or its delegate, such as a POS, ERP, or PIM) is the source of truth for catalog data.
- Platforms or marketplaces that mirror those catalogs may apply markups, discounts, or fees.
- Those platform-specific pricing adjustments are modeled separately from the catalog itself (e.g., in checkout totals/adjustments), not by mutating canonical item prices.
- If a business intentionally sets different base prices per platform, represent them as distinct catalogs with their own embedded item prices.
