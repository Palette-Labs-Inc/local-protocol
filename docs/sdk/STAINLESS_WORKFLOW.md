# Stainless SDK Workflow (End-to-End)

This document describes the normal workflow for:

1. Making API/config changes in this repo.
2. Generating SDKs with Stainless.
3. Uploading preview and merge builds to Stainless.
4. Automatically updating linked SDK repos.
5. Publishing to package registries.

This reflects current Stainless guidance as of February 10, 2026.

## 1) Prerequisites

- Stainless CLI installed and authenticated.
- Stainless GitHub App installed for your Stainless-linked GitHub org, with access to each SDK `production_repo`.
- `production_repo` configured for each SDK target in `.stainless/stainless.yml`.
- CI workflow in the spec repo with both Stainless preview and merge jobs.
- OIDC auth requirements met (spec repo is in the same GitHub org as your Stainless org), or `stainless_api_key` configured for the action.
- Publishing enabled in target config if you want automatic registry publishing.

Quick checks:

```bash
cd /Users/davidpalette/palette/local-protocol

stl --version
stl auth whoami
stl lint
```

### 1.1) Auto-Update Checklist (PR -> SDK Repos)

For SDK repos to update automatically when a PR is merged in this repo, all of the following must be true:

1. `.stainless/stainless.yml` has `targets.<lang>.production_repo` for every target you want updated.
2. The Stainless GitHub App can read/write those SDK repos.
3. The spec repo runs `stainless-api/upload-openapi-spec-action/preview@v1` on PR open/sync/reopen.
4. The spec repo runs `stainless-api/upload-openapi-spec-action/merge@v1` on PR `closed` + `merged == true`.
5. The merge workflow uses the same Stainless `org` and `project` as preview.
6. The merged PR includes your OpenAPI/config changes and the merge build succeeds.

If one of these is missing, merged PRs will not propagate into SDK repositories.

## 2) One-Time Setup

### 2.1 Install and auth CLI

```bash
brew install stainless-api/tap/stl
stl auth login
```

### 2.2 Initialize local project linkage

Run once from repo root:

```bash
cd /Users/davidpalette/palette/local-protocol
stl init
```

### 2.3 Confirm key config

Open and verify:

- `.stainless/stainless.yml`
- `.stainless/workspace.json`

Key fields to confirm in `.stainless/stainless.yml`:

- `organization.name`
- `targets.<lang>.edition`
- `targets.<lang>.production_repo`
- `targets.<lang>.publish` (when ready)

## 3) Configure Publishing

If you want automatic publishing after SDK repo release PR merges, enable `publish` per target.

Example target block:

```yaml
targets:
  typescript:
    edition: typescript.2025-10-10
    package_name: local-protocol
    production_repo: Palette-Labs-Inc/local-protocol-typescript
    publish:
      npm:
        auth_method: oidc

  python:
    edition: python.2025-11-20
    package_name: local_protocol
    production_repo: Palette-Labs-Inc/local-protocol-python
    publish:
      pypi:
        auth_method: oidc

  php:
    edition: php.2025-10-08
    package_name: local-protocol
    production_repo: Palette-Labs-Inc/local-protocol-php
    composer_package_name: local-protocol/local-protocol
    publish:
      packagist: true
```

Notes:

- TypeScript/Python can use OIDC trusted publishing.
- PHP Packagist requires credentials/secrets in the SDK repo.

## 4) Add Stainless CI in Spec Repo (Required for Auto-Updates)

Create `.github/workflows/stainless.yml`:

```yaml
name: Stainless SDK Builds

on:
  pull_request:
    types: [opened, synchronize, reopened, closed]

concurrency:
  group: ${{ github.workflow }}-${{ github.event.pull_request.number }}
  cancel-in-progress: true

env:
  STAINLESS_ORG: YOUR_STAINLESS_ORG
  STAINLESS_PROJECT: local-protocol
  OAS_PATH: openapi/specs/local-protocol.v1.openapi.json
  CONFIG_PATH: .stainless/stainless.yml
  FAIL_ON: error

jobs:
  preview:
    if: github.event.action != 'closed'
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pull-requests: write
      id-token: write
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 2
      - name: Upload preview build to Stainless
        uses: stainless-api/upload-openapi-spec-action/preview@v1
        with:
          org: ${{ env.STAINLESS_ORG }}
          project: ${{ env.STAINLESS_PROJECT }}
          oas_path: ${{ env.OAS_PATH }}
          config_path: ${{ env.CONFIG_PATH }}
          fail_on: ${{ env.FAIL_ON }}

  merge:
    if: github.event.action == 'closed' && github.event.pull_request.merged == true
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pull-requests: write
      id-token: write
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 2
      - name: Upload merge build to Stainless
        uses: stainless-api/upload-openapi-spec-action/merge@v1
        with:
          org: ${{ env.STAINLESS_ORG }}
          project: ${{ env.STAINLESS_PROJECT }}
          oas_path: ${{ env.OAS_PATH }}
          config_path: ${{ env.CONFIG_PATH }}
          fail_on: ${{ env.FAIL_ON }}
```

If your org uses API keys instead of OIDC for the action, include:

```yaml
stainless_api_key: ${{ secrets.STAINLESS_API_KEY }}
```

Important:

- Keep both jobs: `merge` is not intended to be used without `preview`.
- Keep `id-token: write` when using OIDC auth.
- If the spec repo is outside the Stainless-linked GitHub org, use `stainless_api_key` instead of OIDC.

## 5) Day-to-Day Developer Flow

### 5.1 Create a branch and edit API/config

```bash
cd /Users/davidpalette/palette/local-protocol
git checkout -b feat/my-api-change

# edit these as needed:
# - openapi/specs/local-protocol.v1.openapi.json
# - .stainless/stainless.yml
```

### 5.2 Validate and generate locally

Recommended:

```bash
stl lint
just build-sdk-local typescript
just build-sdk-local python
just build-sdk-local php
```

Or all targets at once:

```bash
just build-stainless-sdks-local
```

### 5.3 Review generated diffs

```bash
git status
git diff -- sdks/local-protocol-typescript
git diff -- sdks/local-protocol-python
git diff -- sdks/local-protocol-php
```

### 5.4 Commit and push PR

```bash
git add -A
git commit -m "feat(api): add <change>"
git push -u origin feat/my-api-change
```

Open a pull request in `Palette-Labs-Inc/local-protocol`.

## 6) What Happens on PR (Preview Build)

When PR is opened/updated:

1. GitHub Action runs `upload-openapi-spec-action/preview`.
2. Stainless builds preview SDK outputs.
3. Stainless posts PR comment with:
   - Target-by-target build status.
   - Links to inspect generated SDK changes.
   - Suggested commit message for downstream SDK updates.
4. You can edit that PR comment commit message to control semver semantics later.

## 7) What Happens on Merge

When PR is merged:

1. GitHub Action runs `upload-openapi-spec-action/merge`.
2. Stainless applies the approved preview build and commits generated SDK changes to each linked `production_repo` integrated branch (commonly `next` after linking).
3. Stainless opens or updates SDK repo release PRs from integrated branch to the production branch (default `main`, or the branch suffix in `production_repo` such as `org/repo#master`).

## 8) SDK Repo Release/Publish Flow

In each SDK repo (`local-protocol-typescript`, `local-protocol-python`, `local-protocol-php`):

1. Stainless creates or updates release PR.
2. Review release PR and CI.
3. Merge release PR.
4. If `publish` is configured for that target, package publish runs from the SDK repo release flow.

Useful commands:

```bash
gh pr list -R Palette-Labs-Inc/local-protocol-typescript --state open
gh pr list -R Palette-Labs-Inc/local-protocol-python --state open
gh pr list -R Palette-Labs-Inc/local-protocol-php --state open
```

Merge (example):

```bash
gh pr merge <PR_NUMBER> -R Palette-Labs-Inc/local-protocol-typescript --squash --delete-branch
gh pr merge <PR_NUMBER> -R Palette-Labs-Inc/local-protocol-python --squash --delete-branch
gh pr merge <PR_NUMBER> -R Palette-Labs-Inc/local-protocol-php --squash --delete-branch
```

## 9) Versioning Rules (Practical)

- `feat:` typically drives a minor bump.
- `fix:` typically drives a patch bump.
- `!` or `BREAKING CHANGE:` drives a major bump.

The commit message used by Stainless/release automation matters for this.

## 10) Custom Code Guidance

If you maintain custom code in generated SDK repos:

1. Put custom code on the integrated branch used by Stainless (commonly `next` once linked).
2. Keep custom code commits conventional (`feat`, `fix`, `chore`, etc.).
3. Avoid direct edits to generated files unless that is your intentional patch strategy.

## 11) Troubleshooting

### Preview succeeds locally but CI fails

- Check `OAS_PATH` and `CONFIG_PATH` in workflow.
- Ensure Stainless GitHub App has repo access.
- Ensure action has required permissions (`pull-requests: write`, `id-token: write`).

### Merge build runs but SDK repos do not update

- Confirm `production_repo` values in `.stainless/stainless.yml`.
- Confirm project is linked correctly in Stainless dashboard.
- Confirm merge action uses same org/project names as preview.
- Confirm preview ran for the same PR before merge (merge flow depends on preview context).
- Confirm Stainless GitHub App has access to the target SDK repos.

### No publish after SDK repo update

- Confirm `publish` blocks are enabled for target.
- Confirm OIDC/trusted publisher setup in npm/PyPI.
- Confirm Packagist secrets in PHP SDK repo.

## 12) Repo-Specific Commands (Local Protocol)

From this repo:

```bash
cd /Users/davidpalette/palette/local-protocol

# Validate config/spec
stl lint

# Generate all with production repo wiring
just build-sdks

# Generate all in local mode (no production repo access required)
just build-stainless-sdks-local

# Generate a single target in local mode
just build-sdk-local typescript
just build-sdk-local python
just build-sdk-local php
```

## 13) References

- https://www.stainless.com/docs/getting-started/quickstart-cli/
- https://www.stainless.com/docs/guides/preview-builds/
- https://www.stainless.com/docs/guides/automate-updates/
- https://www.stainless.com/docs/reference/config
- https://www.stainless.com/docs/guides/publish/
- https://www.stainless.com/docs/targets/typescript
- https://www.stainless.com/docs/targets/python
- https://www.stainless.com/docs/targets/php
- https://www.stainless.com/docs/guides/add-custom-code
- https://github.com/stainless-api/upload-openapi-spec-action
