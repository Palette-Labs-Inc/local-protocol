# Published schemas have broken $ref resolution

## Summary

There are two issues with how schemas are published on ucp.dev that break any tooling following `$ref` chains.

## Issue 1: Unversioned URLs serve stale content

The unversioned URLs (`https://ucp.dev/schemas/...`) serve an old schema version that differs from the `latest` release (`2026-01-23`).

For example, `https://ucp.dev/schemas/ucp.json` is a completely different (older) schema than `https://ucp.dev/2026-01-23/schemas/ucp.json`. The old version contains a broken ref:

```
$defs.services.additionalProperties.$ref: https://ucp.dev/services/service.json
```

This URL returns a 404. The file actually exists at `https://ucp.dev/schemas/service.json`.

Mike's `latest` alias (`2026-01-23`) does not appear to be serving at the unversioned path.

## Issue 2: Versioned release has unversioned internal refs

The `2026-01-23` release schemas contain `$ref` values pointing to unversioned URLs. For example, `https://ucp.dev/2026-01-23/schemas/ucp.json` contains:

```
$ref: https://ucp.dev/schemas/service.json#/$defs/base
```

This points to the unversioned path, which resolves to the stale old content (Issue 1). The `2026-01-23` release predates commit `a8b185d`, which introduced the `_rewrite_version_urls` function in `hooks.py`. That function rewrites refs to include the version prefix (e.g., `https://ucp.dev/2026-01-23/schemas/service.json#/$defs/base`), but it was not present when this release was built.

The `draft` deployment, built after `a8b185d`, does this correctly -- refs in `https://ucp.dev/draft/schemas/ucp.json` point to `https://ucp.dev/draft/schemas/...`.

## Impact

Any tooling that resolves `$ref` chains from published schemas hits broken URLs. For example, `datamodel-code-generator` crashes when generating Python SDK models from schemas that transitively reference `ucp.json`.

Neither unversioned nor versioned (`2026-01-23`) URLs produce a working ref chain. Only `draft` has correct internal refs.

## Suggested fixes

1. Ensure unversioned URLs (`https://ucp.dev/schemas/...`) serve the same content as the `latest` alias.
2. Cut a new release from current `main` (which includes the `_rewrite_version_urls` fix from `a8b185d`) to update the `latest` alias.

## Local Protocol workaround

To unblock Python SDK generation, the four UCP schemas referenced by
Local Protocol schemas have been vendored locally at `schemas/ucp/shopping/`
from UCP tag `v2026-01-23`. The three local `$ref`s now point to relative paths
into the vendored copies instead of `https://ucp.dev/...` URLs.

This vendoring is intended to be permanent — it provides version pinning and
build reproducibility independent of upstream hosting state. See
`schemas/ucp/README.md` for details on what is vendored and how to update.
