# SDK Current State and Target State

Date: 2026-02-06

## Purpose

This document explains:

1. The current SDK state in this repository.
2. The desired end state for SDKs across all Local Protocol capabilities.
3. A concrete plan to move from current to desired.

## Scope

This plan focuses on `local-protocol/` and in particular:

- `schemas/`
- `packages/python-sdk/`
- `apps/samples/server/`
- `packages/conformance/`
- documentation under `docs/`

## Current State

## 1) Source of truth exists for all major capability schemas

The repo already defines JSON Schemas for:

- Delivery: `schemas/delivery/`
- Order: `schemas/order/`
- Catalog: `schemas/catalog/`
- Payment: `schemas/payment/`
- Shared primitives: `schemas/shared/`

This means schema coverage is broader than what the current generated SDK exposes.

## 2) Python SDK generation exists, but committed output is partial

There is a generation pipeline:

- Script: `packages/python-sdk/generate_models.sh`
- Target: `packages/python-sdk/src/local_protocol_sdk/models`
- Entry command: `just build-python-sdk`

However, currently committed models are only under delivery:

- `packages/python-sdk/src/local_protocol_sdk/models/delivery/`

No committed generated modules exist yet for:

- order
- catalog
- payment
- shared

## 3) Runtime server surface is currently delivery-centric

Sample server endpoints implemented today:

- `POST /requests`
- `GET /requests`
- `GET /requests/{request_id}`
- `POST /requests/{request_id}/quotes`
- `GET /requests/{request_id}/quotes`
- `GET /requests/{request_id}/quotes/{quote_id}`
- `POST /deliveries`
- `GET /deliveries`
- `GET /deliveries/{delivery_id}`
- `PATCH /deliveries/{delivery_id}/event`
- discovery and health endpoints

Order capability APIs are documented but not implemented in the sample server.

## 4) Conformance is present and useful, but focused on delivery lifecycle

There is a solid conformance harness in:

- `packages/conformance/`

The tests strongly validate delivery and protocol basics (discovery, validation, idempotency, lifecycle, webhook behavior), but there is no equivalent breadth yet for order, catalog, and payment handler flows.

## 5) SDK function behavior today is model-centric

The generated SDK is model-only:

- typed Pydantic models for payloads
- schema-level validation via field constraints
- serialization helpers inherited from Pydantic (`model_validate`, `model_dump`, etc.)

It is not currently a high-level transport client SDK.

## Desired State

## 1) Full schema coverage in generated SDK artifacts

The Python SDK should include generated models for all schema domains:

- delivery
- order
- catalog
- payment
- shared

All generated modules should be committed and reproducible from one command.

## 2) Stable developer-facing SDK surface

The SDK should provide predictable import paths and package organization:

- `local_protocol_sdk.models.delivery.*`
- `local_protocol_sdk.models.order.*`
- `local_protocol_sdk.models.catalog.*` (desired public namespace)
- `local_protocol_sdk.models.payment.*`
- `local_protocol_sdk.models.shared.*`

Optional: add curated top-level exports for common objects to reduce import friction.

## 3) Typed client layer for implemented APIs

Beyond models, add a client package that wraps HTTP calls for implemented server endpoints:

- `LocalProtocolClient.create_request(...)`
- `LocalProtocolClient.get_request(...)`
- `LocalProtocolClient.create_quote(...)`
- `LocalProtocolClient.list_quotes(...)`
- `LocalProtocolClient.create_delivery(...)`
- `LocalProtocolClient.update_delivery_event(...)`

This client should handle:

- base URL configuration
- request/response model conversion
- nonce/idempotency ergonomics
- structured error mapping

## 4) Incremental expansion aligned with server capabilities

As order APIs move from docs into implementation, add typed SDK methods for them.
Same for catalog and payment workflows when corresponding runtime endpoints are introduced.

## 5) CI-backed reproducibility and drift prevention

Any schema change must be forced through generation checks:

- regenerate SDK
- fail CI if generated output is stale
- run conformance and SDK tests

## How to Get There

## Phase 0: Baseline and guardrails (short)

Actions:

1. Regenerate SDK from current `schemas/` and verify all domains emit models.
2. Capture and document any generation blockers (especially external `$ref` handling).
3. Add a CI check that fails if `just build-python-sdk` produces uncommitted changes.

Definition of done:

- A clean regeneration from `schemas/` is possible and deterministic.
- CI reports generation drift.

Progress notes (2026-02-09):

- Full-domain generation now works for all schema domains (delivery, order,
  catalog, payment, shared) plus vendored UCP types.
- Two `datamodel-code-generator` bugs were identified and worked around in
  `generate_models.sh` via temp-copy preprocessing: `$id` base-URL hijacking
  and nested cross-directory `$ref` misresolution.
- Four UCP schema dependencies vendored locally at `schemas/ucp/shopping/`
  from tag `v2026-01-23` to decouple from broken upstream hosting.
- Upstream UCP hosting issues documented in `docs/ucp-stale-latest-issue.md`.
- CI drift check not yet implemented.

## Phase 1: Full model coverage commitment (short)

Actions:

1. Commit generated models for order, catalog, payment, and shared schemas.
2. Add or refresh `__init__.py` exports for each generated domain.
3. Expand SDK README with domain-by-domain import examples.

Definition of done:

- `packages/python-sdk/src/local_protocol_sdk/models/` contains all schema domains.
- Developers can import and validate all protocol objects directly.

Progress notes (2026-02-09):

- `schemas/inventory/` renamed to `schemas/catalog/` so the filesystem path
  matches the domain name used everywhere else (schema titles, docs nav, SDK
  import target). `$id` fields updated to `schemas/catalog/`.
- SDK now generates `models.catalog.*` instead of `models.inventory.*`.

## Phase 2: Typed REST client for implemented endpoints (medium)

Actions:

1. Add a client module, for example:
   - `packages/python-sdk/src/local_protocol_sdk/client/rest.py`
2. Implement typed methods for current sample server routes.
3. Add timeout/retry policy and typed error classes.
4. Add integration tests against the sample server.

Definition of done:

- A consumer can complete request -> quote -> delivery flow using only SDK client methods and SDK models.

## Phase 3: Align API contracts with machine-readable transport specs (medium)

Actions:

1. Introduce REST contract files (OpenAPI) for implemented endpoints.
2. Ensure model schemas and transport contracts do not drift.
3. Optionally generate client stubs from OpenAPI where it improves consistency.

Definition of done:

- Server behavior, schema models, and transport contract are synchronized and test-enforced.

## Phase 4: Expand to order/catalog/payment runtime + SDK methods (longer)

Actions:

1. Implement order endpoints described in docs.
2. Add SDK client methods for order lifecycle.
3. Add catalog read/search endpoints and matching SDK methods.
4. Add payment handler-specific flows where applicable.
5. Extend conformance tests for each new capability.

Definition of done:

- SDK supports all implemented runtime capabilities with typed methods and tests.

## Phase 5: Optional transport SDKs (MCP/A2A) (future)

Actions:

1. Define machine-readable contracts for MCP and A2A bindings.
2. Add transport adapters in SDK (or separate packages) where there is concrete demand.
3. Keep transport adapters thin and schema-driven.

Definition of done:

- SDK users can interact with Local Protocol over chosen transports using typed interfaces.

## Proposed Work Breakdown

## Workstream A: Generation quality

- Regeneration determinism
- external reference handling strategy
- generation drift CI check

## Workstream B: SDK package ergonomics

- import path stability
- curated exports
- docs and examples

## Workstream C: Runtime clients

- typed REST client
- typed exceptions
- integration tests

## Workstream D: Capability expansion

- order runtime + tests + SDK methods
- catalog runtime + tests + SDK methods
- payment runtime + tests + SDK methods

## Risks and Mitigations

## Risk: External `$ref` dependencies cause unstable generation

Mitigation:

- pin schema versions
- cache or vendor critical references where needed
- fail fast in CI when generation breaks

## Risk: SDK outpaces actual server implementation

Mitigation:

- only add client methods for implemented endpoints
- mark planned APIs clearly as not-yet-implemented
- gate with integration tests

## Risk: Breaking import paths for consumers

Mitigation:

- define stable public import contracts
- use semantic versioning for SDK package
- document deprecations before removals

## Immediate Next Steps

1. Run `just build-python-sdk` and confirm full-domain model generation output.
2. Commit regenerated SDK artifacts and update README usage examples.
3. Add CI step to detect SDK generation drift.
4. Start a first typed REST client implementation for the existing delivery endpoints.

## Practical Command Set

From `local-protocol/`:

```bash
just build-python-sdk
just run-server
just test-conformance http://localhost:8000
```

From `packages/python-sdk/`:

```bash
./generate_models.sh
uv run ruff check .
uv run ruff format .
```

## Success Criteria Summary

The migration is successful when:

1. SDK models cover every schema domain in `schemas/`.
2. SDK generation is deterministic and CI-enforced.
3. Implemented server endpoints have typed SDK client methods.
4. Conformance and integration tests validate both protocol behavior and SDK behavior.
5. New capability rollouts (order, catalog, payment) include schema, runtime, tests, and SDK in one consistent delivery path.
