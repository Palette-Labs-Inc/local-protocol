# Local Protocol Conformance Tests

Test suite for validating Local Protocol server implementations against the specification.

## Overview

This package provides:

- **Integration test base class** with helpers for common operations
- **Protocol tests** validating core ask/bid lifecycle
- **Validation tests** ensuring schema compliance
- **Mock webhook server** for testing async callbacks

## Running Tests

### Against a Running Server

```bash
# From repository root
make test-conformance SERVER_URL=http://localhost:8000

# Or directly
./scripts/run_conformance.sh http://localhost:8000
```

### Individual Test Files

```bash
cd packages/conformance
uv run python protocol_test.py --server_url=http://localhost:8000
uv run python validation_test.py --server_url=http://localhost:8000
```

## Test Categories

### `protocol_test.py`
- Discovery endpoint tests (`.well-known/local-protocol`)
- Ask lifecycle (create, get, list)
- Bid lifecycle (create for ask, list)
- Idempotency behavior

### `validation_test.py`
- Required field validation
- Data format validation (dates, currency codes)
- Constraint validation (non-negative prices)

## Writing Custom Tests

Extend `IntegrationTestBase` for access to helpers:

```python
from integration_test_utils import IntegrationTestBase

class MyCustomTest(IntegrationTestBase):
    def test_my_scenario(self):
        # Create an ask
        ask = self.create_ask_payload()
        response = self.post_ask(ask)
        self.assert_response_status(response, [200, 201])

        # Create a bid
        bid = self.create_bid_payload(price=2000)
        response = self.post_bid(ask["id"], bid)
        self.assert_response_status(response, [200, 201])
```

## Configuration

Tests accept these flags:

| Flag | Description | Default |
|------|-------------|---------|
| `--server_url` | Base URL of server under test | Required |
| `--conformance_input` | Path to test config JSON | `test_data/delivery/conformance_input.json` |
| `--verbose_http` | Log HTTP requests | `False` |
| `--mock_webhook_port` | Port for mock webhook server | `8284` |

## Requirements

- Python 3.10+
- uv package manager
- Running Local Protocol server to test against
