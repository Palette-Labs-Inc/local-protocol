# Catalog

The catalog capability is used for advertising availability of goods. Typically, it would be paired with an order capability, so those same goods could be ordered. 

The data model used in this capability is intended to:

- Interoperate with major POS systems and commerce platforms.
- Support multiple catalogs per business/merchant.
- Provide a UI-ready category tree with embedded items and modifiers.
- Keep modifier configuration self-contained for each item.
- Allow availability at catalog, category, or item level, with catalog taking precedence.

## Core Model

- Merchants have catalogs
- Catalogs have categories and items. Items may or may not belong to a category.
- Items are modified via modifier groups, modifier options, and modifier items.

- `schemas/catalog/merchant.json` is the top-level payload.
- `schemas/catalog/catalog.json` defines catalogs and their embedded categories/items.
- `schemas/catalog/types/category.json` defines categories, child categories, and ordered item membership.
- `schemas/catalog/types/item.json` defines items and embedded modifier groups.
- `schemas/catalog/types/modifier_group.json` defines selection constraints and embedded modifier options.
- `schemas/catalog/types/modifier_option.json` defines option nodes and embedded modifier items.
- `schemas/catalog/types/modifier_item.json` defines purchasable modifier items.

## Availability

Additionally, the catalog capability allows advertisement of availability of those items. 

- `schemas/catalog/types/availability.json` and `schemas/catalog/types/interval.json` define weekly and date-specific schedules.
- Availability may be defined on a catalog, category, or item.
- If a catalog defines availability, it overrides category and item availability.
- If a category defines availability, it overrides item availability.

Intervals are neutral and can be reused by closure schedules (recurring unavailability windows applied at the merchant or location level).

## Operations

The set of operations required to fulfill this capability are:

- Get all merchants
- Get all catalogs
- Get a catalog by id
- Get all catalogs for a particular merchant