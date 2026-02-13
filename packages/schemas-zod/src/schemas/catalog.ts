import * as z from "zod";
import { Amount } from "./shared.js";
import { Media } from "./shared.js";

const META = {
  id: (path: string) => ({ id: path }),
  idAnd$id: (path: string, fullUrl: string) => ({ id: path, $id: fullUrl }),
} as const;
const BASE = "https://localprotocol.xyz/schemas";

// Interval
export const Interval = z
  .object({
    day: z.string().optional().describe("Day of week (e.g., Monday, Tuesday)."),
    date: z.string().describe("Calendar date in YYYY-MM-DD.").optional(),
    from_hour: z.int().min(0).max(23).describe("Start hour (0-23)."),
    from_minute: z.int().min(0).max(59).describe("Start minute (0-59)."),
    to_hour: z.int().min(0).max(23).describe("End hour (0-23)."),
    to_minute: z.int().min(0).max(59).describe("End minute (0-59)."),
  })
  .strict()
  .meta({
    ...META.idAnd$id("catalog/types/interval.json", `${BASE}/catalog/types/interval.json`),
    title: "Interval",
    description: "A single time interval for a day of the week or a specific date.",
  });

// Availability
export const Availability = z
  .object({
    timezone: z.string().optional().describe("IANA timezone for the intervals. Defaults to the merchant timezone when omitted."),
    intervals: z.array(Interval).min(1).describe("Availability intervals (weekly or date-specific)."),
  })
  .strict()
  .meta({
    ...META.idAnd$id("catalog/types/availability.json", `${BASE}/catalog/types/availability.json`),
    title: "Availability",
    description: "Availability schedule for a catalog, category, or item.",
  });

// Modifier item
export const ModifierItem = z
  .object({
    id: z.string().describe("Modifier item identifier."),
    name: z.string().describe("Modifier item name."),
    description: z.string().optional().describe("Optional modifier item description."),
    price: Amount.describe("Price for this modifier item."),
    metadata: z.record(z.string(), z.unknown()).optional().describe("Business-defined custom data extending the modifier item."),
  })
  .strict()
  .meta({
    ...META.idAnd$id("catalog/types/modifier_item.json", `${BASE}/catalog/types/modifier_item.json`),
    title: "Modifier Item",
    description: "A purchasable modifier item that can be selected within a modifier group.",
  });

// Modifier group (lazy for circular ref with ModifierOption)
export const ModifierGroup: z.ZodType<{
  id: string;
  name: string;
  description?: string;
  minimum_selections?: number;
  maximum_selections?: number;
  allow_quantities?: boolean;
  max_per_modifier?: number;
  modifier_options: unknown[];
  type?: string;
  metadata?: Record<string, unknown>;
}> = z.lazy(() =>
  z
    .object({
      id: z.string().describe("Modifier group identifier."),
      name: z.string().describe("Display name for the modifier group."),
      description: z.string().optional().describe("Optional modifier group description."),
      minimum_selections: z.int().min(0).optional().describe("Minimum number of selections required from this group."),
      maximum_selections: z.int().min(0).optional().describe("Maximum number of selections allowed from this group."),
      allow_quantities: z.boolean().optional().describe("Whether modifier options can be selected with quantities greater than 1."),
      max_per_modifier: z.int().min(0).optional().describe("Maximum quantity allowed per modifier option. Defaults to 1 (each modifier can be selected at most once)."),
      modifier_options: z.array(ModifierOption).min(1).describe("Ordered modifier options within this group. Order should be used for display."),
      type: z.string().optional().describe("Modifier group type classification."),
      metadata: z.record(z.string(), z.unknown()).optional().describe("Business-defined custom data extending the modifier group."),
    })
    .strict()
    .meta({
      ...META.idAnd$id("catalog/types/modifier_group.json", `${BASE}/catalog/types/modifier_group.json`),
      title: "Modifier Group",
      description: "Group of modifier options with selection constraints.",
    })
);

// Modifier option (lazy for circular ref with ModifierGroup)
export const ModifierOption: z.ZodType<{
  id: string;
  modifier_item: unknown;
  child_modifier_groups?: unknown[];
  is_default?: boolean;
  metadata?: Record<string, unknown>;
}> = z.lazy(() =>
  z
    .object({
      id: z.string().describe("Modifier option identifier."),
      modifier_item: ModifierItem.describe("Modifier item for this option."),
      child_modifier_groups: z.array(ModifierGroup).optional().describe("Nested modifier groups required after selecting this option."),
      is_default: z.boolean().optional().describe("Whether this option is selected by default."),
      metadata: z.record(z.string(), z.unknown()).optional().describe("Business-defined custom data extending the modifier option."),
    })
    .strict()
    .meta({
      ...META.idAnd$id("catalog/types/modifier_option.json", `${BASE}/catalog/types/modifier_option.json`),
      title: "Modifier Option",
      description: "Selectable option within a modifier group.",
    })
);

// Catalog item
export const CatalogItem = z
  .object({
    id: z.string().describe("Item identifier."),
    name: z.string().describe("Item name."),
    description: z.string().describe("Item description."),
    price: Amount.describe("Base price for the item."),
    media: z.array(Media).optional().describe("Item media (images, videos, 3D models)."),
    modifier_groups: z.array(ModifierGroup).optional().describe("Modifier groups available for this item."),
    availability: Availability.optional().describe("Item availability. Ignored when the catalog or category defines availability."),
    metadata: z.record(z.string(), z.unknown()).optional().describe("Business-defined custom data extending the item."),
  })
  .strict()
  .meta({
    ...META.idAnd$id("catalog/types/item.json", `${BASE}/catalog/types/item.json`),
    title: "Catalog Item",
    description: "A menu item with embedded modifier groups.",
  });

// Catalog category 
export const CatalogCategory: z.ZodType<{
  id: string;
  name: string;
  description?: string;
  categories?: unknown[];
  items: unknown[];
  availability?: unknown;
  metadata?: Record<string, unknown>;
}> = z.lazy(() =>
  z
    .object({
      id: z.string().describe("Category identifier."),
      name: z.string().describe("Category display name."),
      description: z.string().optional().describe("Optional category description."),
      categories: z.array(CatalogCategory).optional().describe("Ordered list of child categories for nested category trees."),
      items: z.array(CatalogItem).describe("Ordered list of items in this category."),
      availability: Availability.optional().describe("Category availability. Ignored when the catalog defines availability."),
      metadata: z.record(z.string(), z.unknown()).optional().describe("Business-defined custom data extending the category."),
    })
    .strict()
    .meta({
      ...META.idAnd$id("catalog/types/category.json", `${BASE}/catalog/types/category.json`),
      title: "Catalog Category",
      description: "A category grouping items in a catalog.",
    })
);

// Catalog
export const Catalog = z
  .object({
    id: z.string().describe("Catalog identifier."),
    name: z.string().describe("Catalog name."),
    description: z.string().optional().describe("Catalog description."),
    categories: z.array(CatalogCategory).describe("Ordered top-level categories included in this catalog. Nested categories live under each category's categories array."),
    items: z.array(CatalogItem).optional().describe("Ordered items included in this catalog that are not assigned to a category. Consumers that require category membership should place these items into a synthetic category."),
    availability: Availability.optional().describe("Catalog availability. When present, it overrides category and item availability."),
    metadata: z.record(z.string(), z.unknown()).optional().describe("Business-defined custom data extending the catalog."),
  })
  .strict()
  .meta({
    ...META.idAnd$id("catalog/catalog.json", `${BASE}/catalog/catalog.json`),
    title: "Catalog",
    description: "A catalog containing embedded categories, items, availability, and fulfillment configuration.",
  });

// Merchant
export const Merchant = z
  .object({
    id: z.string().describe("Merchant identifier."),
    name: z.string().describe("Merchant name."),
    timezone: z.string().describe("IANA timezone for availability schedules."),
    last_updated: z.iso.datetime().optional().describe("RFC 3339 timestamp of the latest catalog update."),
    catalogs: z.array(Catalog).min(1).describe("Catalogs available for the merchant."),
    metadata: z.record(z.string(), z.unknown()).optional().describe("Business-defined custom data extending the merchant."),
  })
  .strict()
  .meta({
    ...META.idAnd$id("catalog/merchant.json", `${BASE}/catalog/merchant.json`),
    title: "Merchant",
    description: "Merchant catalog payload containing denormalized catalogs.",
  });
