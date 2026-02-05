# Amount

Shared money object used for item prices and escrow amounts. Inventory fields may still be named `price`, but the underlying type is `Amount`.

## Fields

- `amount` (string, required): Integer string in **minor units**.
- `currency` (string, required): Currency or token symbol (e.g., `USD`, `JPY`, `USDC`).
- `decimals` (integer, required): Number of decimal places for the currency or token.

## Mechanics

`amount` is always an integer string. The human-readable value is:

```
display = amount / (10 ^ decimals)
```

Examples:
- `amount: "1099", decimals: 2` → `10.99`
- `amount: "5000", decimals: 0` → `5000`
- `amount: "4250000", decimals: 6` → `4.250000`

When comparing or summing amounts:
- Only combine values with the **same** `currency` and `decimals`.
- If you must combine different `decimals`, normalize by scaling the smaller precision to the larger one before arithmetic.

For escrow, `currency` should align with `token.symbol` and `decimals` should match `token.decimals`.

## Examples

USD ($10.99):

```json
{ "amount": "1099", "currency": "USD", "decimals": 2 }
```

JPY (¥5000):

```json
{ "amount": "5000", "currency": "JPY", "decimals": 0 }
```

KWD (3 decimals):

```json
{ "amount": "1250", "currency": "KWD", "decimals": 3 }
```

USDC (6 decimals):

```json
{ "amount": "4250000", "currency": "USDC", "decimals": 6 }
```
