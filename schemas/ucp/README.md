# Vendored UCP Schemas

This directory contains a subset of UCP (Universal Commerce Protocol) schemas
vendored locally from the [UCP repository](https://github.com/anthropics/ucp)
at tag `v2026-01-23`.

Canonical LP UCP interoperability version is defined in `schemas/ucp/metadata.json`
and should track this vendored UCP baseline.

## Why vendor?

Three Local Protocol schemas reference UCP types:

| Local schema | UCP type referenced |
|---|---|
| `delivery/quote.json` | `shopping/payment.json` |
| `delivery/types/location.json` | `shopping/types/postal_address.json` |
| `payment/evm_auth_capture_escrow_instrument.json` | `shopping/types/payment_instrument.json` |

These were originally `$ref`s to `https://ucp.dev/schemas/shopping/...`, but
the hosted schemas have broken `$ref` chains that cause `datamodel-code-generator`
to fail during Python SDK generation. The issues are documented in
`docs/ucp-stale-latest-issue.md`. Vendoring locally decouples our build from
upstream hosting availability and gives us version pinning.

## What is vendored

Four files from UCP `v2026-01-23`, with `$id` fields stripped:

```
schemas/ucp/
  shopping/
    payment.json
    types/
      payment_credential.json
      payment_instrument.json
      postal_address.json
```

`payment_instrument.json` transitively depends on `postal_address.json` and
`payment_credential.json`, so all four are required.

## Modifications from upstream

The only modification is removing the `$id` field from each file.
`datamodel-code-generator` uses `$id` as the base URL for resolving relative
`$ref` values, which breaks cross-directory ref resolution when the `$id` host
is unreachable. Stripping `$id` lets the generator use filesystem paths instead.

The generation script (`packages/python-sdk/generate_models.sh`) also strips
`$id` from all schemas at generation time via a temp-copy preprocessing step,
so the vendored files could technically retain `$id` and the build would still
work. They are stripped here for consistency and to make the vendored copies
independently usable.

Note: vendoring is independent of whether `localprotocol.xyz` is live. Even
if local-protocol schemas were hosted, these UCP dependencies would still need
vendoring unless `ucp.dev` hosting is also fixed (see
`docs/ucp-stale-latest-issue.md`).

## Updating

To update to a newer UCP version:

1. Check out the desired tag in the UCP repo.
2. Copy the four files from `source/schemas/shopping/` into this directory.
3. Strip `$id` from each file.
4. Run `packages/python-sdk/generate_models.sh` to verify generation succeeds.
5. Check for schema changes that affect Local Protocol conformance tests
   (particularly `payment.json` structure — see `docs/ucp-stale-latest-issue.md`
   for context on past breaking changes).
