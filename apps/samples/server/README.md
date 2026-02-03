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
| POST | `/deliveries` | Create delivery from accepted bid |
| GET | `/deliveries` | List all deliveries |
| GET | `/deliveries/{id}` | Get delivery by ID |
| PATCH | `/deliveries/{id}/event` | Update delivery event |

## Protocol Flow

The delivery lifecycle follows this sequence:

```
┌──────────────┐                              ┌──────────────┐                              ┌──────────────┐
│   Consumer   │                              │    Server    │                              │   Provider   │
└──────┬───────┘                              └──────┬───────┘                              └──────┬───────┘
       │                                             │                                             │
       │  POST /asks                                 │                                             │
       │  {nonce, pickup, dropoff, times}            │                                             │
       │────────────────────────────────────────────►│                                             │
       │                                             │                                             │
       │  201 {id, status: "open"}                   │                                             │
       │◄────────────────────────────────────────────│                                             │
       │                                             │                                             │
       │                                             │  GET /asks                                  │
       │                                             │◄────────────────────────────────────────────│
       │                                             │                                             │
       │                                             │  [{id, pickup, dropoff, ...}]               │
       │                                             │────────────────────────────────────────────►│
       │                                             │                                             │
       │                                             │  POST /asks/{id}/bids                       │
       │                                             │  {nonce, price, currency, estimates}        │
       │                                             │◄────────────────────────────────────────────│
       │                                             │                                             │
       │                                             │  201 {bid_id, status: "pending"}            │
       │                                             │────────────────────────────────────────────►│
       │                                             │                                             │
       │  GET /asks/{id}/bids                        │                                             │
       │────────────────────────────────────────────►│                                             │
       │                                             │                                             │
       │  [{bid_id, price, currency, ...}]           │                                             │
       │◄────────────────────────────────────────────│                                             │
       │                                             │                                             │
       │  POST /deliveries                           │                                             │
       │  {nonce, ask_id, bid_id, webhook_url}       │                                             │
       │────────────────────────────────────────────►│                                             │
       │                                             │                                             │
       │  201 {delivery_id, event: "created"}        │                                             │
       │◄────────────────────────────────────────────│                                             │
       │                                             │                                             │
       │                                             │  PATCH /deliveries/{id}/event               │
       │                                             │  {event: "assigned"}                        │
       │                                             │◄────────────────────────────────────────────│
       │                                             │                                             │
       │  POST webhook_url                           │                                             │
       │  {event: "assigned", delivery_id, ...}      │                                             │
       │◄────────────────────────────────────────────│                                             │
       │                                             │                                             │
       ▼                                             ▼                                             ▼
```

**Idempotency**: Each `POST` requires a `nonce` field. Retrying with the same nonce returns the original response without creating duplicates.

## Example Usage

### Create an Ask

```bash
curl -X POST http://localhost:8000/asks \
  -H "Content-Type: application/json" \
  -d '{
    "id": "ask-001",
    "nonce": "ask-nonce-001",
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
  -d '{
    "id": "bid-001",
    "nonce": "bid-nonce-001",
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

### Create a Delivery

```bash
curl -X POST http://localhost:8000/deliveries \
  -H "Content-Type: application/json" \
  -H "idempotency-key: del-123" \
  -d '{
    "ask_id": "ask-001",
    "bid_id": "bid-001",
    "webhook_url": "http://example.com/webhook"
  }'
```

### Update Delivery Event

```bash
curl -X PATCH http://localhost:8000/deliveries/del_abc123/event \
  -H "Content-Type: application/json" \
  -d '{
    "event": "in_transit",
    "event_description": "Order is in transit to delivery location"
  }'
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
- Idempotency support via required `nonce` field in payloads
- Input validation with detailed error messages
- CORS enabled for browser clients
- Delivery event standard conformance (core + food)
- Webhook event delivery for status updates

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
