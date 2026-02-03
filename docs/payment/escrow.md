# On-Chain Escrow

A neutral smart-contract escrow for B2B settlement on EVM chains. The requester
(payer, "Platform") locks funds in escrow, submits an escrow instrument at
checkout, and the escrow releases funds based on payer/payee attestations. The
provider (payee, "Business") receives funds on release. A guarantor provides
100% coverage; on dispute the guarantor's stake is used to make the payer or
payee whole.

Handler id (recommended): `com.localprotocol.evm_escrow`

## Handler configuration (business discovery)

Businesses advertise their escrow configuration in `ucp.payment_handlers`.
Token selection is explicit and configurable.

### Fields

- `chain_id` (integer, required): EVM chain id for the escrow contract.
- `contract_address` (string, required): Escrow contract address for the chain.
- `accepted_tokens` (array, required): Tokens accepted on the escrow contract chain.
- `expiry_seconds` (integer, required): Escrow expiry window in seconds (uses `block.timestamp`).

### Example

```json
{
  "id": "acme_escrow_prod",
  "version": "2026-02-02",
  "spec": "https://example.com/specs/local-protocol/escrow",
  "schema": "https://localprotocol.dev/schemas/payment/evm_escrow_instrument.json",
  "config": {
    "chain_id": 8453,
    "contract_address": "0x1111111111111111111111111111111111111111",
    "accepted_tokens": [
      {
        "address": "0x2222222222222222222222222222222222222222",
        "symbol": "USDC",
        "decimals": 6
      }
    ],
    "expiry_seconds": 86400
  }
}
```

## Escrow instrument

The requester ("Platform") submits a payment instrument that proves escrow
funding and binds it to the order.

### Fields

- `id` (string, required): Instrument id assigned by the requester ("Platform").
- `handler_id` (string, required): Handler instance id from discovery.
- `type` (string, required): `evm_escrow`.
- `escrow_id` (string, required): Escrow identifier from the contract.
- `chain_id` (integer, required): EVM chain id.
- `contract_address` (string, required): Escrow contract address.
- `token` (object, required): Token identifier.
- `amount` (string, required): Decimal string amount.
- `order_reference` (string, required): External order reference.
- `expires_at` (string, optional): RFC 3339 expiration timestamp. If present, it MUST match the on-chain escrow expiry derived from `expiry_seconds`.
- `metadata` (object, optional): Free-form key/value metadata.

### Example

```json
{
  "id": "instrument_001",
  "handler_id": "acme_escrow_prod",
  "type": "evm_escrow",
  "escrow_id": "escrow_abc123",
  "chain_id": 8453,
  "contract_address": "0x1111111111111111111111111111111111111111",
  "token": {
    "address": "0x2222222222222222222222222222222222222222",
    "symbol": "USDC",
    "decimals": 6
  },
  "amount": "42.50",
  "order_reference": "order_987",
  "expires_at": "2026-02-03T01:15:00Z",
  "metadata": {
    "route_id": "route_551",
    "contract_ref": "lp-2026-02-03-01"
  }
}
```

## Release attestation (dual signature)

Each party submits a signed attestation to the escrow contract. The escrow
releases funds when both attestations are present for the same escrow id and
order reference. If the payer disputes and the payee requests release, the
escrow pays both parties and the guarantor's coverage absorbs the loss. If the
payer disputes and the payee releases, the escrow refunds the payer and returns
the guarantor's coverage.

### Fields

- `escrow_id` (string, required)
- `order_reference` (string, required)
- `actor_role` (string, required): `payer` or `payee`.
- `statement` (string, required): `approve` or `dispute` for payer; `request` or `release` for payee.
- `issued_at` (string, required): RFC 3339 timestamp.
- `signature` (string, required): EIP-191 or EIP-712 signature over the payload.

### Example

```json
{
  "escrow_id": "escrow_abc123",
  "order_reference": "order_987",
  "actor_role": "payee",
  "statement": "request",
  "issued_at": "2026-02-02T23:10:00Z",
  "signature": "0xbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
}
```
