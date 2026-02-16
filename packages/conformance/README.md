# Local Protocol Conformance Tests

Test suite for validating Local Protocol server implementations against the specification.

## Overview

This package provides:

- **Integration test base class** with helpers for common operations
- **Protocol tests** validating core request/quote lifecycle
- **Delivery event tests** validating event lifecycle and webhook delivery
- **Standard schema tests** validating conformance to courier event vocabulary
- **Validation tests** ensuring schema compliance
- **Mock webhook server** for testing async callbacks

## Running Tests

### Against a Running Server

```bash
# Start the server in one terminal
just run-server

# Run tests in another terminal (from repository root)
just test-conformance http://localhost:8000

# Or run the script directly
./scripts/run_conformance.sh http://localhost:8000
```

### Individual Test Files

```bash
cd packages/conformance
uv run python protocol_test.py --server_url=http://localhost:8000
uv run python validation_test.py --server_url=http://localhost:8000
uv run python delivery_event_test.py --server_url=http://localhost:8000
```

## Test Categories

### `protocol_test.py`
- Discovery endpoint tests (`.well-known/ucp`)
- Request lifecycle (create, get, list)
- Quote lifecycle (create for request, list)
- Idempotency behavior via nonce field

### `validation_test.py`
- Required field validation for requests and quotes
- Data format validation (dates, currency codes)
- Constraint validation (non-negative prices)

### `delivery_event_test.py`
- Delivery creation from request/quote
- Event vocabulary and versioning (date-based format)
- Timestamp fields (created_at, updated_at)
- Event state management

### `event_lifecycle_test.py`
- Courier event transitions (created, assigned, enroute_pickup, collected, delivered, canceled)
- Full lifecycle progression

### `discovery_conformance_test.py`
- Standard conformance declarations
- UCP discovery registry shape validation (`services`, `capabilities`, `payment_handlers`)
- Version format validation (YYYY-MM-DD date format)
- Courier standard references

### `standard_schema_test.py`
- Courier standard structure validation
- Event definitions and descriptions
- Required fields and format validation

### `webhook_delivery_test.py`
- Webhook POST on event transitions
- Webhook payload structure
- Multiple transition handling
- No webhook when URL not provided

## Webhook Testing

The webhook tests validate that servers correctly push event notifications when delivery state changes.

### How It Works

1. **Mock webhook server** starts on `--mock_webhook_port` (default 8284)
2. Tests create a delivery with `webhook_url` pointing to the mock server
3. Tests trigger event transitions via `PATCH /deliveries/{id}/event`
4. The server under test POSTs to the webhook URL
5. Tests verify the mock server received the expected payloads

### Test Sequence

```
┌─────────────────┐     POST /deliveries          ┌─────────────────┐
│  Test Suite     │  ─────────────────────────►   │  Server Under   │
│                 │   {webhook_url: mock:8284}    │     Test        │
└─────────────────┘                               └─────────────────┘
        │                                                  │
        │         PATCH /deliveries/{id}/event             │
        │  ─────────────────────────────────────────────►  │
        │         {event: "assigned"}                      │
        │                                                  │
        │                                    ┌─────────────┴───────────┐
        │                                    │  Server sends webhook   │
        │                                    └─────────────┬───────────┘
        │                                                  │
┌───────┴─────────┐    POST /webhook                       │
│  Mock Webhook   │  ◄─────────────────────────────────────┘
│    Server       │   {event_type, delivery_id, event, ...}
└─────────────────┘
        │
        │  Test asserts webhook was received with correct payload
        ▼
```

### Expected Webhook Payload

When an event transition occurs, the server MUST POST this payload:

```json
{
  "event_type": "delivery_event",
  "delivery_id": "del_abc123",
  "event": "assigned",
  "event_description": "Courier assigned",
  "event_vocabulary": "xyz.localprotocol.delivery.courier@2026-01-30",
  "updated_at": "2026-01-30T10:30:00Z"
}
```

### Running Webhook Tests

```bash
# Run only webhook tests
cd packages/conformance
uv run python webhook_delivery_test.py --server_url=http://localhost:8000

# With custom webhook port (if 8284 is in use)
uv run python webhook_delivery_test.py \
  --server_url=http://localhost:8000 \
  --mock_webhook_port=9999
```

## Writing Custom Tests

Extend `IntegrationTestBase` for access to helpers:

```python
from integration_test_utils import IntegrationTestBase

class MyCustomTest(IntegrationTestBase):
    def test_my_scenario(self):
        # Create a request
        request = self.create_request_payload()
        response = self.post_request(request)
        self.assert_response_status(response, [200, 201])

        # Create a quote
        quote = self.create_quote_payload(price=2000)
        response = self.post_quote(request["id"], quote)
        self.assert_response_status(response, [200, 201])

        # Create a delivery with webhook
        delivery = self.create_delivery(webhook_url="http://example.com/hook")

        # Update delivery event
        response = self.update_delivery_event(
            delivery["id"],
            "assigned",
            "Courier assigned"
        )
        self.assert_response_status(response, 200)
```

## Configuration

Tests accept these flags:

| Flag | Description | Default |
|------|-------------|---------|
| `--server_url` | Base URL of server under test | Required |
| `--conformance_input` | Path to test config JSON | `test_data/delivery/conformance_input.json` |
| `--standards_dir` | Directory with standard fixtures | `test_data/standards` |
| `--schema_dir` | Directory with JSON schemas | None |
| `--verbose_http` | Log HTTP requests | `False` |
| `--mock_webhook_port` | Port for mock webhook server | `8284` |

## Requirements

- Python 3.10+
- uv package manager
- Running Local Protocol server to test against
