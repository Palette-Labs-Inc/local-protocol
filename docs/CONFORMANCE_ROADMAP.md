# Conformance Infrastructure Roadmap

This document outlines the remaining work to complete the conformance infrastructure for Local Protocol, adapted from UCP patterns.

## Completed: Tier 1 - Critical Infrastructure

- [x] **Python SDK Generation** (`packages/python-sdk/`)
  - Pydantic model generation from JSON schemas
  - `just build-python-sdk` command

- [x] **Conformance Test Framework** (`packages/conformance/`)
  - `integration_test_utils.py` - Base test class and helpers
  - `protocol_test.py` - Discovery, ask/bid lifecycle, idempotency tests
  - `validation_test.py` - Schema validation tests
  - Test data fixtures

- [x] **Automation** (`justfile`, `scripts/`)
  - `just build-python-sdk` - Generate SDK
  - `just test-conformance <url>` - Run conformance tests
  - `scripts/run_conformance.sh` - Test orchestration

---

## Tier 2: Reference Implementation

### 2.1 Sample Server (`apps/samples/server/`)

A minimal FastAPI server implementing the Local Protocol spec for testing and reference.

#### Directory Structure
```
apps/samples/server/
├── pyproject.toml
├── README.md
├── server.py              # FastAPI entry point
├── config.py              # Configuration
├── db.py                  # SQLite data layer
├── models.py              # Internal models
├── routes/
│   ├── __init__.py
│   ├── discovery.py       # /.well-known/local-protocol, /healthz
│   ├── asks.py            # /asks endpoints
│   └── bids.py            # /asks/{id}/bids endpoints
└── services/
    ├── __init__.py
    ├── ask_service.py     # Ask business logic
    └── bid_service.py     # Bid business logic
```

#### Required Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/.well-known/local-protocol` | Service discovery |
| GET | `/healthz` | Health check |
| POST | `/asks` | Create delivery ask |
| GET | `/asks/{id}` | Get ask by ID |
| GET | `/asks` | List asks (optional) |
| POST | `/asks/{id}/bids` | Create bid for ask |
| GET | `/asks/{id}/bids` | List bids for ask |
| GET | `/asks/{id}/bids/{bid_id}` | Get bid by ID (optional) |

#### Implementation Tasks

- [ ] Create `apps/samples/server/pyproject.toml` with FastAPI, uvicorn, SQLite dependencies
- [ ] Implement `server.py` with FastAPI app and CORS configuration
- [ ] Implement `db.py` with SQLite storage for asks and bids
- [ ] Implement `routes/discovery.py` with well-known and health endpoints
- [ ] Implement `routes/asks.py` with CRUD operations
- [ ] Implement `routes/bids.py` with bid creation and listing
- [ ] Add idempotency support via `idempotency-key` header
- [ ] Add request validation using generated SDK models
- [ ] Write README with setup and usage instructions

#### Justfile Additions

```just
# Run sample server
run-server port="8000":
  cd apps/samples/server && uv run server.py --port {{port}}

# Run server and conformance tests together
test-with-server:
  #!/usr/bin/env bash
  cd apps/samples/server && uv run server.py --port 8000 &
  SERVER_PID=$!
  sleep 2
  just test-conformance http://localhost:8000
  kill $SERVER_PID
```

---

### 2.2 Sample Client (`apps/samples/client/`)

A simple Python client demonstrating how to interact with a Local Protocol server.

#### Directory Structure
```
apps/samples/client/
├── pyproject.toml
├── README.md
├── client.py              # Client implementation
└── examples/
    ├── happy_path.py      # Complete ask/bid flow
    └── error_handling.py  # Error scenarios
```

#### Implementation Tasks

- [ ] Create `client.py` with typed client using SDK models
- [ ] Implement `create_ask()`, `get_ask()`, `create_bid()`, `list_bids()` methods
- [ ] Add `examples/happy_path.py` demonstrating full flow
- [ ] Add `examples/error_handling.py` showing error scenarios
- [ ] Write README with usage examples

---

## Tier 3: Enhanced Automation

### 3.1 Additional Conformance Tests

Expand test coverage based on UCP patterns:

- [ ] `lifecycle_test.py` - Full ask→bid→accept→complete flow
- [ ] `webhook_test.py` - Status update webhook delivery
- [ ] `error_test.py` - Error response format validation
- [ ] `pagination_test.py` - List endpoint pagination (if implemented)

### 3.2 CI/CD Integration

- [ ] Add GitHub Actions workflow for conformance tests
- [ ] Add workflow to generate and publish SDK on schema changes
- [ ] Add workflow to build and test sample server

#### `.github/workflows/conformance.yml`
```yaml
name: Conformance Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v4
      - name: Generate SDK
        run: just build-python-sdk
      - name: Start sample server
        run: |
          cd apps/samples/server
          uv run server.py --port 8000 &
          sleep 3
      - name: Run conformance tests
        run: just test-conformance http://localhost:8000
```

### 3.3 Documentation Generation

- [ ] Add script to generate API documentation from schemas
- [ ] Add conformance test results reporting
- [ ] Add SDK documentation generation

---

## Tier 4: Advanced Features (Future)

### 4.1 Additional Transports

- [ ] WebSocket transport for real-time updates
- [ ] gRPC transport option

### 4.2 Security Testing

- [ ] Authentication/authorization tests
- [ ] Rate limiting tests
- [ ] Input sanitization tests

### 4.3 Performance Testing

- [ ] Load testing scripts
- [ ] Latency benchmarks
- [ ] Concurrent request handling

---

## Quick Reference

### Current Commands
```bash
just                                    # Show available commands
just build-python-sdk                   # Generate SDK from schemas
just test-conformance http://localhost:8000  # Run conformance tests
just fmt                                # Format code
just lint                               # Lint code
just clean                              # Clean generated files
```

### After Tier 2
```bash
just run-server                         # Start sample server on :8000
just run-server 3000                    # Start on custom port
just test-with-server                   # Run server + tests together
```

---

## Dependencies

| Package | Purpose |
|---------|---------|
| `fastapi` | Web framework for sample server |
| `uvicorn` | ASGI server |
| `httpx` | HTTP client for tests |
| `pydantic` | Data validation |
| `absl-py` | Test framework |
| `datamodel-code-generator` | Schema to Pydantic conversion |

---

## References

- [UCP Conformance Tests](https://github.com/user/ucp/packages/conformance)
- [UCP Sample Server](https://github.com/user/ucp/apps/samples/rest/python/server)
- [Local Protocol Spec](../ucp_spec.md)
