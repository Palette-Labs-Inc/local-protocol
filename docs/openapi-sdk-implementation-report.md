# OpenAPI SDK Implementation Report

Date: February 9, 2026

## Summary

Implemented the [OpenAPI Generator SDK plan](./OPENAPI_GENERATOR_SDK_PLAN.md) for `local-protocol/`, producing a curated OpenAPI 3.1 specification and generating PHP and TypeScript SDKs from it. Subsequently expanded the spec to include all domain schemas (catalog, order, payment, shared, UCP, delivery events) so the generated SDKs cover the same type surface as the existing JSON Schema-based Python SDK.

Python SDK generation remains on `datamodel-code-generator` from JSON Schemas -- it produces higher-fidelity Pydantic v2 models than OpenAPI Generator (see comparison below). OpenAPI Generator is used for PHP and TypeScript only.

This document records what was done, what was produced, and a comparison of the two generation approaches.

## What Was Done

### Phase 1: Scaffold and Bootstrap

Created directory structure:

```
openapi/
  specs/
    local-protocol.bootstrap.openapi.json
    local-protocol.v1.openapi.json
  config/
packages/
  php-sdk/
  python-sdk-openapi/
  typescript-sdk/
```

Bootstrapped an initial OpenAPI spec from the FastAPI sample server's `app.openapi()`. This produced a valid spec with all 12 route operations but mostly empty schemas -- the sample server routes use `dict[str, Any]` for request/response types, so FastAPI generates `additionalProperties: true` objects with no defined properties.

The bootstrap spec is kept as `local-protocol.bootstrap.openapi.json` for reference.

### Phase 2: Curate Canonical v1 Spec

Manually curated `local-protocol.v1.openapi.json` (1,297 lines) by reading:

- All route handlers (`routes/requests.py`, `routes/quotes.py`, `routes/deliveries.py`, `routes/discovery.py`)
- The in-memory database layer (`db.py`)
- All JSON Schema source files under `schemas/`

The curated spec contains:

- **12 API operations** across 8 path patterns
- **44 component schemas** covering all domains
- Proper `oneOf`, `anyOf`, `allOf` composition matching the source JSON Schemas
- Error response models (ErrorResponse, ValidationErrorResponse)
- Field-level constraints (patterns, ranges, enums, required fields)

### Phase 3: Install and Pin OpenAPI Generator CLI

Installed `@openapitools/openapi-generator-cli` v2.28.2 as a dev dependency (writes to `package.json`). Pinned the underlying generator engine to v7.19.0 (writes to `openapitools.json`).

Files added:
- `package.json` -- npm dev dependency
- `openapitools.json` -- generator version pin
- `node_modules/` -- (gitignored)

### Phase 4: Validate

The spec validates cleanly. The only warnings are "Unused model" for the 27 domain schemas not referenced by API paths -- these are included purely for SDK model generation, not tied to specific endpoints.

### Phase 5: Generate SDKs

Generated PHP and TypeScript SDKs (Python was initially generated but later removed in favor of the existing `datamodel-code-generator` pipeline -- see decision below):

| SDK | Generator | Output | Models | API Classes |
|-----|-----------|--------|--------|-------------|
| PHP | `php` | `packages/php-sdk/` | 43 | 4 |
| TypeScript | `typescript-fetch` | `packages/typescript-sdk/` | 43 | 4 |

Both SDKs produce 43 model files and 4 API client classes (DeliveriesApi, DiscoveryApi, QuotesApi, RequestsApi).

### Phase 6: Add `just` Commands

Added to `justfile`:

| Recipe | Purpose |
|--------|---------|
| `openapi-generator-setup` | Install and pin OpenAPI Generator CLI |
| `openapi-validate` | Validate the OpenAPI spec |
| `build-php-sdk` | Generate PHP SDK |
| `build-ts-sdk` | Generate TypeScript SDK |
| `build-openapi-sdks` | Validate + generate PHP and TypeScript SDKs |

### Domain Schema Expansion

The initial v1 spec only contained delivery API schemas (14 models). After comparing model counts with the existing JSON Schema Python SDK, all remaining domain schemas were added as OpenAPI component schemas:

- **Catalog** (9): Catalog, Merchant, CatalogItem, CatalogCategory, Availability, Interval, ModifierGroup, ModifierOption, ModifierItem
- **Order** (5): Cart, CartItem, OrderRequest, OrderQuote, Order
- **Payment** (3): EvmAuthCaptureEscrowConfig, EvmAuthCaptureEscrowInstrument, EvmToken
- **Shared** (4): Amount, FiatCurrency, EvmCurrency, Media
- **UCP** (5): Payment, PaymentCredential, PaymentInstrument, SelectedPaymentInstrument, PostalAddress
- **Delivery events** (2): DeliveryEvent, DeliveryEventVocabulary

Circular references (ModifierGroup <-> ModifierOption, CatalogCategory self-reference) are expressed with standard `$ref` and handled by all three generators. Schema inheritance (EvmAuthCaptureEscrowInstrument extends PaymentInstrument, SelectedPaymentInstrument extends PaymentInstrument) uses `allOf`.

## Files Produced

```
local-protocol/
  openapi/
    specs/
      local-protocol.bootstrap.openapi.json   # FastAPI auto-generated (reference)
      local-protocol.v1.openapi.json           # Curated canonical spec (1,297 lines)
    config/                                    # Empty, reserved for generator configs
  packages/
    php-sdk/                                   # Generated PHP SDK (OpenAPI Generator)
    typescript-sdk/                            # Generated TypeScript SDK (OpenAPI Generator)
    python-sdk/                                # Python SDK (datamodel-code-generator, unchanged)
  package.json                                 # npm devDependency for openapi-generator-cli
  openapitools.json                            # Pins generator to v7.19.0
  justfile                                     # Updated with 6 new recipes
```

## Decision: Drop OpenAPI Generator for Python

After comparing the generated output from both tools, OpenAPI Generator's Python SDK was removed from the pipeline. The existing `datamodel-code-generator` from JSON Schemas remains the sole Python generation path.

**Rationale:**

1. **Schema composition fidelity**: OpenAPI Generator flattens `oneOf` into loose optional fields (losing XOR constraints), flattens `allOf` into duplicated fields (losing class inheritance), and wraps field-level unions in verbose intermediary classes. `datamodel-code-generator` preserves all of these using idiomatic Pydantic v2 patterns.

2. **Code quality**: `datamodel-code-generator` produces ~12 lines per simple model using native Pydantic features (`Field(pattern=...)`, `Literal[...]`, `ConfigDict(extra="allow")`). OpenAPI Generator produces ~80+ lines per model with imperative `@field_validator` methods, manual `additional_properties` dicts, and `to_dict`/`from_dict` boilerplate.

3. **Dependency footprint**: The JSON Schema SDK requires only `pydantic>=2.0.0`. The OpenAPI SDK adds `urllib3`, `python-dateutil`, and `typing-extensions`.

4. **No API client needed from OpenAPI Generator**: The Python SDK's purpose is to provide domain model types. An HTTP client layer, if needed, can be written by hand or generated separately with a more idiomatic tool.

5. **PHP and TypeScript are unaffected**: The fidelity issues are specific to OpenAPI Generator's Python template. The PHP and TypeScript generators produce reasonable output for their ecosystems, and there is no competing high-fidelity generator for those languages from JSON Schema.

**Current pipeline:**

| Language | Tool | Source | Output |
|----------|------|--------|--------|
| Python | `datamodel-code-generator` | `schemas/*.json` | `packages/python-sdk/` |
| PHP | OpenAPI Generator | `openapi/specs/local-protocol.v1.openapi.json` | `packages/php-sdk/` |
| TypeScript | OpenAPI Generator | `openapi/specs/local-protocol.v1.openapi.json` | `packages/typescript-sdk/` |

## Model Coverage Comparison

### Counting classes, not files

The two Python SDKs organize code differently. Comparing file counts is misleading.

**JSON Schema SDK**: 44 classes across 32 files. Several files contain multiple classes due to `oneOf` variants (Interval1/Interval2, Location1/Location2), circular reference co-location (ModifierGroup + ModifierOption in `_internal.py`), and inlined subclasses (7 helper classes inside `evm_auth_capture_escrow_instrument.py`).

**OpenAPI SDK**: 43 classes across 43 files. Always one class per file.

### What overlaps

30 domain model types are present in both SDKs:

| Domain | Types |
|--------|-------|
| Shared | Amount, FiatCurrency, EvmCurrency, Media |
| Catalog | Catalog, Merchant, CatalogItem, CatalogCategory, Availability, Interval, ModifierGroup, ModifierOption, ModifierItem |
| Delivery | Delivery, DeliveryRequest, DeliveryQuote, DeliveryEventVocabulary, Coordinates, Location |
| Order | Cart, CartItem, Order, OrderRequest, OrderQuote |
| Payment | EvmAuthCaptureEscrowConfig, EvmAuthCaptureEscrowInstrument, EvmToken |
| UCP | Payment, PaymentCredential, PaymentInstrument, SelectedPaymentInstrument, PostalAddress |

### What's only in the JSON Schema SDK (14 classes)

These are structural artifacts of how `datamodel-code-generator` represents schema composition. They are not independent domain types:

- **`oneOf` variant classes**: Interval1, Interval2, Location1, Location2
- **Inlined `allOf`/`oneOf` subclasses** inside EvmAuthCaptureEscrowInstrument: Currency, Currency1, Currency2, Currency3, MaxAmount, Amount (local)
- **Delivery event helpers**: Extend (RootModel wrapper for extension strings), Event (single event entry)

### What's only in the OpenAPI SDK (13 classes)

These fall into three categories:

**API request/response types (9)** -- shapes for HTTP request bodies and response payloads, defined in the spec's `paths` section. The JSON Schema SDK has no equivalent because it only models domain schemas, not API contracts:

| Type | Purpose |
|------|---------|
| `DeliveryRequestCreate` | POST /requests body |
| `DeliveryQuoteCreate` | POST /requests/{id}/quotes body |
| `CreateDeliveryRequest` | POST /deliveries body |
| `UpdateEventRequest` | PATCH /deliveries/{id}/event body |
| `DiscoveryResponse` | GET /.well-known/local-protocol response |
| `HealthResponse` | GET /healthz response |
| `ErrorResponse` | 4xx error body |
| `ValidationErrorResponse` | 422 error body |
| `ValidationErrorResponseDetail` | Nested validation error item |

**Domain type with different organization (1)**: `DeliveryEvent` is a standalone schema in the OpenAPI spec. In the JSON Schema SDK it exists as the `Event` class nested inside `events.py`.

**Generator artifact (1)**: `AmountCurrency` -- a 138-line wrapper class generated by OpenAPI Generator to represent the `oneOf: [FiatCurrency, EvmCurrency]` union on Amount.currency. The JSON Schema SDK handles this as a native Python union (`FiatCurrency | EvmCurrency`).

## Comparison of the Two Python SDKs

### Generation pipeline

| | JSON Schema SDK | OpenAPI SDK |
|---|---|---|
| Tool | `datamodel-code-generator` v0.53.0 | `openapi-generator-cli` v7.19.0 |
| Source | JSON Schema files (`schemas/`) | OpenAPI 3.1 spec (hand-curated) |
| Preprocessing | Strip `$id`, absolutify `$ref` paths | None |
| Runtime deps | `pydantic>=2.0.0` | `pydantic>=2`, `urllib3>=2.1`, `python-dateutil>=2.8.2`, `typing-extensions>=4.7.1` |
| Build system | hatchling | setuptools |
| Python | >=3.10 | >=3.9 |
| Output | Models only | Models + API clients + HTTP layer + configuration |
| PEP 561 | No `py.typed` | Has `py.typed` |

### Schema composition fidelity

The OpenAPI spec correctly uses `oneOf`, `anyOf`, and `allOf`. The fidelity loss happens in OpenAPI Generator's Python code generation, not in the spec format.

**`oneOf` + `not` (Interval: day XOR date)**

JSON Schema SDK -- two variant classes, constraint enforced:
```python
class Interval1(BaseModel):       # day required, date optional
  day: str
  date: date | None = None

class Interval2(BaseModel):       # date required, day optional
  day: str | None = None
  date: date

class Interval(RootModel[Interval1 | Interval2]):
  root: Interval1 | Interval2
```

OpenAPI SDK -- single flat class, constraint lost:
```python
class Interval(BaseModel):
    day: Optional[StrictStr] = None        # both optional
    var_date: Optional[date] = None        # XOR not enforced
```

**`anyOf` (Location: at least one of coordinates or postal_address)**

JSON Schema SDK -- two variants, at-least-one enforced:
```python
class Location1(BaseModel):       # postal_address required
  postal_address: PostalAddress
  coordinates: Coordinates | None = None

class Location2(BaseModel):       # coordinates required
  postal_address: PostalAddress | None = None
  coordinates: Coordinates

class Location(RootModel[Location1 | Location2]):
  root: Location1 | Location2
```

OpenAPI SDK -- flat class, both optional:
```python
class Location(BaseModel):
    coordinates: Optional[Coordinates] = None
    postal_address: Optional[PostalAddress] = None
```

**`oneOf` on a field (Amount.currency: FiatCurrency | EvmCurrency)**

JSON Schema SDK -- native Python union, 1 line:
```python
currency: FiatCurrency | EvmCurrency
```

OpenAPI SDK -- 138-line wrapper class with `actual_instance` indirection:
```python
# amount.py
currency: AmountCurrency

# amount_currency.py
class AmountCurrency(BaseModel):
    actual_instance: Optional[Union[EvmCurrency, FiatCurrency]] = None
    # ... 138 lines of validation, serialization, deserialization
```

**`allOf` (SelectedPaymentInstrument extends PaymentInstrument)**

JSON Schema SDK -- class inheritance:
```python
class SelectedPaymentInstrument(PaymentInstrument):
  selected: bool | None = None
```

OpenAPI SDK -- flattened, no inheritance:
```python
class SelectedPaymentInstrument(BaseModel):   # extends BaseModel, not PaymentInstrument
    id: StrictStr                              # all parent fields duplicated
    handler_id: StrictStr
    type: StrictStr
    # ...
    selected: Optional[StrictBool] = None
```

### Model code style

| Aspect | JSON Schema SDK | OpenAPI SDK |
|--------|----------------|-------------|
| Lines per simple model | ~12 | ~80+ |
| Pattern validation | `Field(..., pattern="^[0-9]+$")` | `@field_validator` with `re.match()` |
| Literal/const | `type: Literal["evm_auth_capture_escrow"]` | `@field_validator` checking set membership |
| Extra fields | `ConfigDict(extra="allow")` | Manual `additional_properties: Dict[str, Any]` with custom `to_dict`/`from_dict` |
| Union types | `FiatCurrency \| EvmCurrency` | Wrapper class with `actual_instance` |
| Imports | Relative (`from . import ...`) | Absolute (`from local_protocol_openapi_sdk.models...`) |
| Re-exports | None (import by path) | All models re-exported from `__init__.py` |

### What the OpenAPI SDK adds

The OpenAPI SDK provides a full API client layer:

- **4 API classes** with typed methods for all 12 operations
- **3 method variants per endpoint**: `.method()` (returns data), `.method_with_http_info()` (returns ApiResponse with headers/status), `.method_without_preload_content()` (returns raw urllib3 response)
- **HTTP client** using urllib3 with connection pooling, timeouts, proxy/SOCKS support, mTLS
- **Configuration** class with server URLs, auth (API key, basic, OAuth2, bearer), SSL settings, retries
- **Serialization pipeline** with typed request/response handling and content-type negotiation

The JSON Schema SDK has none of this -- it is a model library only.

## Alternative Generators Evaluated

OpenAPI Generator's Python template is Java-based and template-driven, which accounts for the verbose, non-idiomatic output. Other options that may produce more idiomatic Python:

| Tool | Models | Client | Pydantic v2 | `oneOf`/`allOf` fidelity | Notes |
|------|--------|--------|-------------|--------------------------|-------|
| `datamodel-code-generator` | Yes | No | Native | High (RootModel, inheritance) | Already in use for JSON Schema SDK; also accepts OpenAPI input |
| `openapi-python-client` | Yes (attrs) | Yes (httpx) | No (uses attrs) | Medium (named variants, property merging) | Best OSS client generator; not Pydantic |
| Speakeasy | Yes | Yes (httpx) | Yes | High | Commercial (free tier for 1 SDK) |
| Stainless | Yes | Yes | Yes | High | Commercial, invite-only (powers Anthropic/OpenAI/Stripe SDKs) |
| Fern | Yes | Yes | Partial (v1 compat layer) | Medium | Commercial (free tier), Node CLI |

The most pragmatic path for higher-fidelity Python would be running `datamodel-code-generator --input-file-type openapi` against the v1 spec for models, paired with a thin hand-written or separately-generated httpx client.

## Remaining Work

From the original plan, Phase 7 (CI drift checks) was not implemented. The recommended CI step:

```bash
just build-openapi-sdks
git diff --exit-code openapi/specs packages/php-sdk packages/typescript-sdk
```

Additionally, the [Python SDK generation fixes plan](./plans/python-sdk-generation-fixes.md) addresses separate concerns about the JSON Schema SDK (model strictness, oneOf preservation, atomic generation, version pinning, stale README).
