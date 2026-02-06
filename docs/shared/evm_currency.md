# EvmCurrency

EVM token currency descriptor used in [Amount](amount.md). Schema: `schemas/shared/evm_currency.json`.

## Fields

- `chain_id` (integer, required): EVM chain id.
- `address` (string, required): Token contract address.
- `decimals` (integer, required): Decimal places for the token.

## Example

```json
{
  "chain_id": 8453,
  "address": "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",
  "decimals": 6
}
```
