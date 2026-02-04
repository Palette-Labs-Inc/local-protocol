# Delivery Lifecycle

This document describes the delivery lifecycle from ask to payment release.

## Overview

```
Ask → Bid (with payment.handlers) → Instrument Acquisition → Delivery Creation → Events → Payment Release
```

1. **Ask** - Requester posts delivery need (pickup, dropoff, times)
2. **Bid** - Provider responds with price and payment handlers
3. **Instrument Acquisition** - Requester approves/permits allowance or deposits funds using handler config
4. **Delivery Creation** - Requester accepts bid with payment instrument
5. **Events** - Delivery progresses through courier event vocabulary
6. **Payment Release** - `delivered` event triggers timeout, then auto-release

## Ask

Requester posts a delivery request with pickup/dropoff locations and times.

```json
POST /asks
{
  "id": "ask_123",
  "nonce": "req-abc",
  "pickup_location": {
    "postal_address": {
      "street_address": "123 Main St",
      "address_locality": "Springfield",
      "address_region": "IL",
      "postal_code": "62701",
      "address_country": "US"
    }
  },
  "dropoff_location": {
    "postal_address": {
      "street_address": "456 Oak Ave",
      "address_locality": "Springfield",
      "address_region": "IL",
      "postal_code": "62701",
      "address_country": "US"
    }
  },
  "pickup_time": "2026-02-04T18:00:00Z",
  "dropoff_time": "2026-02-04T19:00:00Z"
}
```

## Bid

Provider responds with price, time estimates, and payment handlers. The `payment`
field is required and contains handlers that describe how to acquire a payment
instrument.

```json
POST /asks/ask_123/bids
{
  "id": "bid_456",
  "nonce": "prov-xyz",
  "price": 599,
  "currency": "USD",
  "pickup_location": { ... },
  "dropoff_location": { ... },
  "pickup_estimate": "2026-02-04T18:05:00Z",
  "dropoff_estimate": "2026-02-04T18:45:00Z",
  "payment": {
    "handlers": [
      {
        "id": "courier_escrow_prod",
        "name": "com.localprotocol.evm_auth_capture_escrow",
        "version": "2026-02-02",
        "spec": "https://localprotocol.xyz/specs/payment/evm-auth-capture-escrow",
        "config_schema": "https://localprotocol.xyz/schemas/payment/evm_auth_capture_escrow_config.json",
        "instrument_schemas": [
          "https://localprotocol.xyz/schemas/payment/evm_auth_capture_escrow_instrument.json"
        ],
        "config": {
          "chain_id": 8453,
          "contract": "0x1111111111111111111111111111111111111111",
          "operator": "0x3333333333333333333333333333333333333333",
          "receiver": "0x5555555555555555555555555555555555555555",
          "accepted_tokens": [
            {
              "address": "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",
              "symbol": "USDC",
              "decimals": 6
            }
          ]
        }
      }
    ]
  }
}
```

## Instrument Acquisition

After receiving a bid, the requester uses the handler config to acquire a
payment instrument. For the EVM auth/capture escrow handler, this means
approving (or permitting) the escrow contract to spend up to the authorized
amount, or depositing funds into escrow, on-chain.

1. Read `payment.handlers[]` from the bid
2. Select a handler (e.g., `courier_escrow_prod`)
3. Use `handler.config` to interact with the escrow contract
4. Approve/permit allowance or deposit funds on-chain
5. Receive `payment_info_hash` identifying the approval/deposit

See [Payment Handler Guide](../payment/handler-guide.md) for details on handler
execution.

## Delivery Creation

Requester accepts a bid by submitting the ask ID, bid ID, and payment instrument.

```json
POST /deliveries
{
  "ask_id": "ask_123",
  "bid_id": "bid_456",
  "payment_data": {
    "id": "instr_001",
    "handler_id": "courier_escrow_prod",
    "type": "evm_auth_capture_escrow",
    "payment_info_hash": "0xaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "operator": "0x3333333333333333333333333333333333333333",
    "payer": "0x6666666666666666666666666666666666666666",
    "receiver": "0x5555555555555555555555555555555555555555",
    "chain_id": 8453,
    "contract": "0x1111111111111111111111111111111111111111",
    "token": {
      "address": "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",
      "symbol": "USDC",
      "decimals": 6
    },
    "max_amount": "5990000",
    "amount": "5990000",
    "preapproval_expires_at": "2026-02-04T18:30:00Z",
    "authorization_expires_at": "2026-02-05T18:30:00Z",
    "refund_expires_at": "2026-03-04T18:30:00Z",
    "nonce": "1"
  }
}
```

**Validation:**

- `bid_id` must reference a bid for the given `ask_id`
- `payment_data.handler_id` must match one of `bid.payment.handlers[].id`

**Response:**

```json
{
  "id": "del_789",
  "ask_id": "ask_123",
  "bid_id": "bid_456",
  "payment_instrument_id": "instr_001",
  "event": "created",
  "created_at": "2026-02-04T17:55:00Z"
}
```

## Delivery Events

Delivery progresses through events defined in the courier event vocabulary
(`events/delivery/courier.json`):

| Event | Description |
|-------|-------------|
| `created` | Delivery created |
| `assigned` | Courier assigned |
| `enroute_pickup` | Courier heading to pickup |
| `arrived_pickup` | Courier at pickup location |
| `collected` | Courier picked up |
| `arrived_dropoff` | Courier at dropoff location |
| `delivered` | Courier completed dropoff |
| `canceled` | Delivery canceled |

Events are delivered via webhook or polling.

## Payment Release

The `delivered` event serves as seller attestation. Payment follows an optimistic
release model:

1. Provider emits `delivered` event
2. Timeout window begins (configurable, e.g., 24-72 hours)
3. If no dispute from buyer within the window, funds auto-release from escrow
4. Buyer can optionally confirm early to release immediately

The operator captures funds from the escrow contract after the timeout expires.

## Sequence Diagram

```
Requester                    Provider                    Escrow Contract
    |                           |                           |
    |  1. POST /asks            |                           |
    |-------------------------->|                           |
    |                           |                           |
    |  2. POST /asks/{id}/bids  |                           |
    |<--------------------------|                           |
    |                           |                           |
    |  3. Authorize on-chain    |                           |
    |------------------------------------------------------>|
    |<------------------------------------------------------|
    |                           |                           |
    |  4. POST /deliveries      |                           |
    |-------------------------->|                           |
    |                           |                           |
    |  5. Events: created →     |                           |
    |     ... → delivered       |                           |
    |<--------------------------|                           |
    |                           |                           |
    |                           |  6. Capture (after timeout)
    |                           |-------------------------->|
```

## Related

- [Payment Handler Guide](../payment/handler-guide.md)
- [EVM Auth/Capture Escrow](../payment/escrow.md)
