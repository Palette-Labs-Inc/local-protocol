# Payment Handler Guide

This document explains how payment handlers work in local-protocol.

## Overview

Payment handlers define how payment instruments are acquired for a transaction.
They are discovered in the quote response and used by the requester to approve or
deposit funds before creating a delivery.

## Handler Discovery

Payment handlers are included in every quote response under `payment.handlers[]`.
Each handler provides the information needed to acquire a payment instrument.

```json
{
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
        "config": { ... }
      }
    ]
  }
}
```

## Handler Structure

| Field | Description |
|-------|-------------|
| `id` | Unique identifier for this handler instance |
| `name` | Specification name in reverse-DNS format |
| `version` | Handler version (YYYY-MM-DD) |
| `spec` | URI to the handler specification |
| `config_schema` | URI to JSON Schema for validating the config |
| `instrument_schemas` | URIs to schemas for instruments this handler produces |
| `config` | Handler-specific configuration |

The handler structure follows UCP's `payment_handler.json` schema.

## Instrument Acquisition

After receiving a quote, the requester acquires a payment instrument:

1. **Select handler** - Choose from `quote.payment.handlers[]`
2. **Read config** - Use `handler.config` for handler-specific parameters
3. **Execute protocol** - Perform handler-specific actions (e.g., on-chain approval/permit or escrow deposit)
4. **Build instrument** - Create instrument conforming to `handler.instrument_schemas[]`
5. **Submit** - Include instrument as `payment_data` in delivery creation

## Binding Requirements

Payment instruments bind to the accepted quote:

- `payment_data.handler_id` must match one of `quote.payment.handlers[].id`
- The instrument is tied to the specific quote being accepted
- Multiple quotes may have different handlers; the requester chooses which quote to accept

## EVM Auth/Capture Escrow Handler

local-protocol defines one handler: `com.localprotocol.evm_auth_capture_escrow`.

### Config

```json
{
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
```

### Instrument Acquisition Flow

1. Read escrow contract address and accepted tokens from config
2. Approve/permit allowance or deposit funds into escrow
3. Receive `payment_info_hash` from on-chain transaction
4. Build instrument with hash and authorization parameters

### Instrument

```json
{
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
```

See [EVM Auth/Capture Escrow](escrow.md) for full details.

## Adding New Handlers

To add a new payment handler:

1. Create config schema in `schemas/payment/`
2. Create instrument schema extending `payment_instrument_base`
3. Add instrument to `schemas/payment/payment_instrument.json` oneOf
4. Document the handler in `docs/payment/`

## Related

- [Delivery Lifecycle](../delivery/lifecycle.md)
- [EVM Auth/Capture Escrow](escrow.md)
