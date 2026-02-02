# Local Protocol Sample Server

A minimal reference implementation of the Local Protocol for conformance testing.

## Quick Start

```bash
# From repository root
just run-server

# Or with custom port
just run-server 3000

# Or directly
cd apps/samples/server
uv run server.py --port 8000
```

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/.well-known/local-protocol` | Service discovery |
| GET | `/healthz` | Health check |
| POST | `/asks` | Create delivery ask |
| GET | `/asks` | List all asks |
| GET | `/asks/{id}` | Get ask by ID |
| POST | `/asks/{id}/bids` | Create bid for ask |
| GET | `/asks/{id}/bids` | List bids for ask |
| GET | `/asks/{id}/bids/{bid_id}` | Get specific bid |

## Example Usage

### Create an Ask

```bash
curl -X POST http://localhost:8000/asks \
  -H "Content-Type: application/json" \
  -H "idempotency-key: ask-123" \
  -d '{
    "id": "ask-001",
    "pickup_location": {
      "coordinates": {"latitude": 37.7749, "longitude": -122.4194}
    },
    "dropoff_location": {
      "coordinates": {"latitude": 37.7849, "longitude": -122.4094}
    },
    "pickup_time": "2024-01-15T10:00:00Z",
    "dropoff_time": "2024-01-15T11:00:00Z"
  }'
```

### Create a Bid

```bash
curl -X POST http://localhost:8000/asks/ask-001/bids \
  -H "Content-Type: application/json" \
  -H "idempotency-key: bid-123" \
  -d '{
    "id": "bid-001",
    "price": 1500,
    "currency": "USD",
    "pickup_location": {
      "coordinates": {"latitude": 37.7749, "longitude": -122.4194}
    },
    "dropoff_location": {
      "coordinates": {"latitude": 37.7849, "longitude": -122.4094}
    },
    "pickup_estimate": "2024-01-15T10:15:00Z",
    "dropoff_estimate": "2024-01-15T10:45:00Z"
  }'
```

### List Bids for Ask

```bash
curl http://localhost:8000/asks/ask-001/bids
```

## Running Conformance Tests

```bash
# Start server in one terminal
just run-server

# Run tests in another terminal
just test-conformance http://localhost:8000
```

## Features

- In-memory storage (resets on restart)
- Idempotency support via `idempotency-key` header
- Input validation with detailed error messages
- CORS enabled for browser clients

## Development

```bash
# Run with auto-reload
cd apps/samples/server
uv run server.py --reload

# Format code
just fmt

# Lint code
just lint
```
