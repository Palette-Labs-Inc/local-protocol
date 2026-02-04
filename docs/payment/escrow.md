# EVM Auth/Capture Payments

An on-chain auth/capture flow for payments on EVM chains that mirrors the
classic authorization/capture flow. The buyer ("Platform")
authorizes funds into an EVM escrow contract, submits an authorization
instrument at checkout, and an operator captures funds for the seller
("Business"). Refunds are possible within the operator’s policies.
For background on the flow, see Coinbase’s overview of the Commerce Payments
Protocol: [blog.base.dev/commerce-payments-protocol](https://blog.base.dev/commerce-payments-protocol).

Handler id: `com.localprotocol.evm_auth_capture_escrow`

## Handler configuration (seller discovery)

Accepted tokens are explicitly listed and should be ERC-20 tokens supported by
the contract on the specified chain.

### Fields

- `chain_id` (integer, required): EVM chain id for the escrow contract.
- `contract` (string, required): Escrow contract address for the chain.
- `operator` (string, required): Operator address authorized to drive state transitions.
- `receiver` (string, required): Default receiver address for captures.
- `accepted_tokens` (array, required): Tokens accepted on the escrow contract chain.

### Example

```json
{
  "id": "acme_auth_capture_prod",
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
        "address": "0x2222222222222222222222222222222222222222",
        "symbol": "USDC",
        "decimals": 6
      }
    ]
  }
}
```

## Authorization instrument

The buyer ("Platform") submits a payment instrument that proves an
authorization exists and binds it to this payment.

The instrument includes all fields required to compute `payment_info_hash`,
with expiry windows acting as operator-enforced limits for captures and refunds.
Fee bounds are omitted from the instrument and assumed to be zero with a zero
address fee receiver (`0x0000000000000000000000000000000000000000`) when
recomputing the hash.

### Fields

- `id` (string, required): Instrument id assigned by the buyer ("Platform").
- `handler_id` (string, required): Handler instance id from discovery (`ucp.payment_handlers[].id`).
- `type` (string, required): `evm_auth_capture_escrow`.
- `payment_info_hash` (string, required): Hash that identifies the on-chain payment authorization.
- `operator` (string, required): Operator address used to compute the hash.
- `payer` (string, required): Payer address used to compute the hash (the buyer).
- `receiver` (string, required): Receiver address used to compute the hash
  (MUST match the handler default receiver or be allowed by operator policy).
- `token` (object, required): Token identifier used to compute the hash.
- `max_amount` (string, required): Maximum authorized amount (atomic units) used to compute the hash.
- `preapproval_expires_at` (string, required): Pre-approval expiration timestamp (RFC 3339) used to compute the hash.
- `authorization_expires_at` (string, required): Authorization expiration timestamp (RFC 3339) used to compute the hash.
- `refund_expires_at` (string, required): Refund expiration timestamp (RFC 3339) used to compute the hash.
- `nonce` (string, required): Unique nonce used to compute the hash.
- `chain_id` (integer, required): EVM chain id.
- `contract` (string, required): Escrow contract address.
- `amount` (string, required): Amount in atomic units (integer string, token decimals applied).

`amount` MUST be less than or equal to `max_amount`.

### Example

```json
{
  "id": "instrument_001",
  "handler_id": "acme_auth_capture_prod",
  "type": "evm_auth_capture_escrow",
  "payment_info_hash": "0xaaaaaaaabbbbbbbbccccccccddddddddeeeeeeeeffffffff0000000011111111",
  "operator": "0x3333333333333333333333333333333333333333",
  "payer": "0x6666666666666666666666666666666666666666",
  "chain_id": 8453,
  "contract": "0x1111111111111111111111111111111111111111",
  "receiver": "0x5555555555555555555555555555555555555555",
  "token": {
    "address": "0x2222222222222222222222222222222222222222",
    "symbol": "USDC",
    "decimals": 6
  },
  "max_amount": "5000000",
  "preapproval_expires_at": "2026-02-03T00:15:00Z",
  "authorization_expires_at": "2026-02-04T00:15:00Z",
  "refund_expires_at": "2026-03-05T00:15:00Z",
  "nonce": "1",
  "amount": "4250000"
}
```

## Capture and refund

The operator submits capture or refund transactions to the escrow contract.

### Fields

- `payment_info_hash` (string, required)
- `amount` (string, required)

### Example

```json
{
  "payment_info_hash": "0xaaaaaaaabbbbbbbbccccccccddddddddeeeeeeeeffffffff0000000011111111",
  "amount": "4250000"
}
```
