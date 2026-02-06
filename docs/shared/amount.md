# Amount

Shared money object used for item prices and escrow amounts. Inventory fields may still be named `price`, but the underlying type is `Amount`. The integer string is stored in `value` to avoid `amount.amount` naming collisions. Schema: `schemas/shared/amount.json`.

## Fields

- `value` (string, required): Integer string in **minor units**.
- `currency` (object, required): Currency descriptor ([FiatCurrency](fiat_currency.md) or [EvmCurrency](evm_currency.md)).

## Mechanics

`value` is always an integer string. For EVM currencies, `value` is in atomic units. The human-readable value is:

```
display = value / (10 ^ currency.decimals)
```

For fiat currencies, the minor units are implied by the ISO 4217 currency (e.g., USD has 2, JPY has 0).

Examples:
- Fiat: `value: "1099", currency.symbol: "USD"` → `10.99` (USD has 2 minor units)
- Fiat: `value: "5000", currency.symbol: "JPY"` → `5000` (JPY has 0 minor units)
- EVM: `value: "4250000", currency.decimals: 6` → `4.250000`

When comparing or summing amounts:
- Only combine values with the **same** `currency` and `decimals`.
- If you must combine different `decimals`, normalize by scaling the smaller precision to the larger one before arithmetic.

For escrow, `currency` should align with the payment token. For EVM tokens, `currency.chain_id`, `currency.address`, and `currency.decimals` should match the token config.

## Examples

USD ($10.99):

```json
{ "value": "1099", "currency": { "symbol": "USD" } }
```

JPY (¥5000):

```json
{ "value": "5000", "currency": { "symbol": "JPY" } }
```

KWD (3 decimals):

```json
{ "value": "1250", "currency": { "symbol": "KWD" } }
```

USDC (6 decimals, Base):

```json
{
  "value": "4250000",
  "currency": {
    "chain_id": 8453,
    "address": "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",
    "decimals": 6
  }
}
```
