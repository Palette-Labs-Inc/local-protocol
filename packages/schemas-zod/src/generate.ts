/**
 * Generate JSON Schema files from Zod schemas and write them under local-protocol/schemas/test.
 * Run from repo root: yarn workspace @local-protocol/schemas-zod generate
 * Or from this package: yarn build && yarn generate
 */

import * as fs from "node:fs";
import * as path from "node:path";
import * as z from "zod";
import { toJSONSchemaFromRegistry } from "./to-json-schema.js";
import { FiatCurrency, EvmCurrency, Amount, Media, EvmAmount } from "./schemas/shared.js";
import {
  PostalAddress,
  PaymentCredential,
  PaymentInstrument,
  Payment,
  paymentJsonSchema,
  paymentInstrumentJsonSchema,
} from "./schemas/ucp.js";
import {
  Coordinates,
  Location,
  locationJsonSchema,
  DeliveryRequest,
  DeliveryQuote,
  Delivery,
} from "./schemas/delivery.js";
import {
  DeliveryEventVocabulary,
  deliveryEventsJsonSchema,
  courierVocabularyData,
} from "./schemas/delivery-events.js";
import { CartItem, OrderRequest, OrderQuote, Order, Cart } from "./schemas/order.js";
import { EvmToken, EvmAuthCaptureEscrowConfig, EvmAuthCaptureEscrowInstrument } from "./schemas/payment.js";
import {
  Interval,
  Availability,
  ModifierItem,
  ModifierGroup,
  ModifierOption,
  CatalogItem,
  CatalogCategory,
  Catalog,
  Merchant,
} from "./schemas/catalog.js";

const registry = z.registry<Record<string, unknown>>();
registry.add(FiatCurrency, { id: "shared/fiat_currency.json" });
registry.add(EvmCurrency, { id: "shared/evm_currency.json" });
registry.add(Amount, { id: "shared/amount.json" });
registry.add(Media, { id: "shared/media.json" });
registry.add(EvmAmount, { id: "shared/evm_amount.json" });
registry.add(PostalAddress, { id: "ucp/shopping/types/postal_address.json" });
registry.add(PaymentCredential, { id: "ucp/shopping/types/payment_credential.json" });
registry.add(PaymentInstrument, { id: "ucp/shopping/types/payment_instrument.json" });
registry.add(Payment, { id: "ucp/shopping/payment.json" });
registry.add(Coordinates, { id: "delivery/types/coordinates.json" });
registry.add(Location, { id: "delivery/types/location.json" });
registry.add(DeliveryRequest, { id: "delivery/request.json" });
registry.add(DeliveryQuote, { id: "delivery/quote.json" });
registry.add(Delivery, { id: "delivery/delivery.json" });
registry.add(DeliveryEventVocabulary, { id: "delivery/events.json" });
registry.add(CartItem, { id: "order/types/cart_item.json" });
registry.add(OrderRequest, { id: "order/request.json" });
registry.add(OrderQuote, { id: "order/quote.json" });
registry.add(Order, { id: "order/order.json" });
registry.add(Cart, { id: "order/cart.json" });
registry.add(EvmToken, { id: "payment/types/evm_token.json" });
registry.add(EvmAuthCaptureEscrowConfig, { id: "payment/evm_auth_capture_escrow_config.json" });
registry.add(EvmAuthCaptureEscrowInstrument, { id: "payment/evm_auth_capture_escrow_instrument.json" });
registry.add(Interval, { id: "catalog/types/interval.json" });
registry.add(Availability, { id: "catalog/types/availability.json" });
registry.add(ModifierItem, { id: "catalog/types/modifier_item.json" });
registry.add(ModifierGroup, { id: "catalog/types/modifier_group.json" });
registry.add(ModifierOption, { id: "catalog/types/modifier_option.json" });
registry.add(CatalogItem, { id: "catalog/types/item.json" });
registry.add(CatalogCategory, { id: "catalog/types/category.json" });
registry.add(Catalog, { id: "catalog/catalog.json" });
registry.add(Merchant, { id: "catalog/merchant.json" });

const SCHEMAS_DIR = path.resolve(process.cwd(), "schemas");
const PACKAGE_SCHEMAS_DIR = path.resolve(process.cwd(), "..", "..", "schemas");
// Output under schemas/test so you can compare to originals without overwriting
const OUT_SUBDIR = "test";

// Schemas that have $id in the original; all others omit it
const SCHEMAS_WITH_$ID = new Set([
  "shared/fiat_currency.json",
  "shared/evm_currency.json",
  "shared/amount.json",
  "shared/media.json",
  "shared/evm_amount.json",
  "delivery/delivery.json",
  "delivery/events.json",
  "payment/types/evm_token.json",
  "payment/evm_auth_capture_escrow_config.json",
  "catalog/types/interval.json",
  "catalog/types/availability.json",
  "catalog/types/modifier_item.json",
  "catalog/types/modifier_group.json",
  "catalog/types/modifier_option.json",
  "catalog/types/item.json",
  "catalog/types/category.json",
  "catalog/catalog.json",
  "catalog/merchant.json",
]);

function getSchemasDir(): string {
  if (fs.existsSync(SCHEMAS_DIR)) return SCHEMAS_DIR;
  if (fs.existsSync(PACKAGE_SCHEMAS_DIR)) return PACKAGE_SCHEMAS_DIR;
  return SCHEMAS_DIR;
}

function getOutputDir(): string {
  return path.join(getSchemasDir(), OUT_SUBDIR);
}

const ROOT_KEY_ORDER_DEFAULT = ["$schema", "$id", "title", "description", "type", "additionalProperties", "properties", "required", "anyOf", "oneOf"];
const ROOT_KEY_ORDER_REQUIRED_FIRST = ["$schema", "$id", "title", "description", "type", "required", "properties", "additionalProperties", "anyOf", "oneOf"];
const PROP_KEY_ORDER = ["$ref", "type", "format", "pattern", "description", "minimum", "maximum", "oneOf", "anyOf", "items", "additionalProperties"];

function sortKeys(obj: Record<string, unknown>, keyOrder: string[]): Record<string, unknown> {
  const result: Record<string, unknown> = {};
  for (const k of keyOrder) {
    if (k in obj && obj[k] !== undefined) result[k] = obj[k];
  }
  for (const k of Object.keys(obj)) {
    if (!keyOrder.includes(k)) result[k] = obj[k];
  }
  return result;
}

// Remove pattern from sub-schemas that have format date-time (originals don't include it)
function removeDateTimePatterns(obj: unknown): void {
  if (obj == null || typeof obj !== "object") return;
  if (Array.isArray(obj)) {
    obj.forEach(removeDateTimePatterns);
    return;
  }
  const o = obj as Record<string, unknown>;
  if (o.format === "date-time" && "pattern" in o) delete o.pattern;
  for (const v of Object.values(o)) removeDateTimePatterns(v);
}

const SAFE_INTEGER_MAX = 9007199254740991;

// Normalize Zod JSON Schema output: additionalProperties {} -> true; strip default integer maximum
function normalizeZodOutput(obj: unknown): void {
  if (obj == null || typeof obj !== "object") return;
  if (Array.isArray(obj)) {
    obj.forEach(normalizeZodOutput);
    return;
  }
  const o = obj as Record<string, unknown>;
  if (o.additionalProperties && typeof o.additionalProperties === "object" && Object.keys(o.additionalProperties as object).length === 0) {
    o.additionalProperties = true;
  }
  if (o.type === "integer" && (o as { maximum?: number }).maximum === SAFE_INTEGER_MAX) {
    delete (o as Record<string, unknown>).maximum;
  }
  for (const v of Object.values(o)) normalizeZodOutput(v);
}

// Replace anyOf with oneOf only where the original uses oneOf (e.g. amount currency)
function oneOfWhereOriginal(schema: Record<string, unknown>, id: string): void {
  if (id === "shared/amount.json" && schema.properties && typeof schema.properties === "object") {
    const currency = (schema.properties as Record<string, unknown>).currency as Record<string, unknown> | undefined;
    if (currency && "anyOf" in currency) {
      currency.oneOf = currency.anyOf;
      delete currency.anyOf;
    }
  }
}

function reorderSchema(schema: Record<string, unknown>, id: string): Record<string, unknown> {
  const rootOrder =
    id.startsWith("shared/") || id.startsWith("catalog/") || id.startsWith("payment/")
      ? ROOT_KEY_ORDER_REQUIRED_FIRST
      : ROOT_KEY_ORDER_DEFAULT;
  const out = sortKeys(schema, rootOrder);
  if (out.properties && typeof out.properties === "object") {
    const props = out.properties as Record<string, unknown>;
    const reordered: Record<string, unknown> = {};
    for (const [k, v] of Object.entries(props)) {
      reordered[k] = typeof v === "object" && v !== null && !Array.isArray(v)
        ? sortKeys(v as Record<string, unknown>, PROP_KEY_ORDER)
        : v;
    }
    out.properties = reordered;
  }
  if (Array.isArray(out.anyOf)) {
    out.anyOf = (out.anyOf as unknown[]).map((item) =>
      typeof item === "object" && item !== null && !Array.isArray(item)
        ? reorderSchema(item as Record<string, unknown>, "")
        : item
    );
  }
  if (Array.isArray(out.oneOf)) {
    out.oneOf = (out.oneOf as unknown[]).map((item) =>
      typeof item === "object" && item !== null && !Array.isArray(item)
        ? reorderSchema(item as Record<string, unknown>, "")
        : item
    );
  }
  if (Array.isArray(out.allOf)) {
    out.allOf = (out.allOf as unknown[]).map((item) =>
      typeof item === "object" && item !== null && !Array.isArray(item)
        ? reorderSchema(item as Record<string, unknown>, id)
        : item
    );
  }
  return out;
}

// Normalize generated schema so it matches the original: strip id, optional $id, key order, oneOf, no date-time pattern, Zod quirks
function normalizeSchema(schema: Record<string, unknown>, id: string): Record<string, unknown> {
  const copy = JSON.parse(JSON.stringify(schema)) as Record<string, unknown>;
  delete copy.id;
  if (!SCHEMAS_WITH_$ID.has(id)) delete copy.$id;
  removeDateTimePatterns(copy);
  normalizeZodOutput(copy);
  oneOfWhereOriginal(copy, id);
  return reorderSchema(copy, id);
}

// Recursively reorder generated to match original's key order at every level; use generated's values (so $ref stay relativized).
function reorderToMatch(original: unknown, generated: unknown): unknown {
  if (generated === undefined || generated === null) return original;
  if (typeof original !== "object" || original === null) return generated;
  if (Array.isArray(original)) {
    const genArr = Array.isArray(generated) ? generated : [];
    return original.map((origItem, i) =>
      i < genArr.length ? reorderToMatch(origItem, genArr[i]) : origItem
    );
  }
  const origObj = original as Record<string, unknown>;
  const genObj = generated as Record<string, unknown>;
  const result: Record<string, unknown> = {};
  for (const k of Object.keys(origObj)) {
    if (k in genObj) {
      result[k] = reorderToMatch(origObj[k], genObj[k]);
    } else {
      result[k] = origObj[k];
    }
  }
  return result;
}

function relativizeRefInSchema(
  schema: Record<string, unknown>,
  fromPath: string,
  allIds: Set<string>,
  outDir: string
): void {
  function walk(obj: unknown): void {
    if (obj == null || typeof obj !== "object") return;
    if (Array.isArray(obj)) {
      obj.forEach(walk);
      return;
    }
    const o = obj as Record<string, unknown>;
    if (typeof o.$ref === "string" && allIds.has(o.$ref)) {
      const toPath = o.$ref as string;
      const toFull = path.join(outDir, toPath);
      const fromFull = path.join(outDir, fromPath);
      o.$ref = path.relative(path.dirname(fromFull), toFull).replace(/\\/g, "/") || path.basename(toPath);
      return;
    }
    for (const v of Object.values(o)) walk(v);
  }
  walk(schema);
}

function main(): void {
  const schemasDir = getSchemasDir();
  const outDir = getOutputDir();
  const schemas = toJSONSchemaFromRegistry(registry);
  const ids = new Set(Object.keys(schemas));

  const schemaOverrides = new Map<string, () => Record<string, unknown>>([
    ["ucp/shopping/payment.json", paymentJsonSchema],
    ["ucp/shopping/types/payment_instrument.json", paymentInstrumentJsonSchema],
    ["delivery/events.json", deliveryEventsJsonSchema],
    [
      "delivery/types/location.json",
      () =>
        locationJsonSchema({
          postal_address: path.relative("delivery/types", "ucp/shopping/types/postal_address.json").replace(/\\/g, "/"),
          coordinates: "coordinates.json",
        }),
    ],
  ]);

  for (const [id, schema] of Object.entries(schemas)) {
    const filePath = path.join(outDir, id);
    const dir = path.dirname(filePath);
    fs.mkdirSync(dir, { recursive: true });

    const override = schemaOverrides.get(id);
    let toWrite: Record<string, unknown>;
    if (override) {
      toWrite = override();
    } else {
      relativizeRefInSchema(schema, id, ids, outDir);
      toWrite = normalizeSchema(schema, id);
    }
    const originalPath = path.join(schemasDir, id);
    if (fs.existsSync(originalPath)) {
      const originalJson = fs.readFileSync(originalPath, "utf8");
      const original = JSON.parse(originalJson) as Record<string, unknown>;
      toWrite = reorderToMatch(original, toWrite) as Record<string, unknown>;
    }

    fs.writeFileSync(filePath, JSON.stringify(toWrite, null, 2) + "\n", "utf8");
    console.log("Generated", id);
  }

  const courierDest = path.join(outDir, "delivery/events/courier.json");
  fs.mkdirSync(path.dirname(courierDest), { recursive: true });
  fs.writeFileSync(
    courierDest,
    JSON.stringify(courierVocabularyData(), null, 2) + "\n",
    "utf8"
  );
  console.log("Generated", "delivery/events/courier.json");
}

main();
