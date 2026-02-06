# Amount

Shared money object used for item prices and escrow amounts. Inventory fields may still be named `price`, but the underlying type is `Amount`. The integer string is stored in `value` to avoid `amount.amount` naming collisions.

## Fields

- `value` (string, required): Integer string in **minor units**.
- `currency` (string, required): Currency or token symbol (e.g., `USD`, `JPY`, `USDC`).
- `decimals` (integer, required): Number of decimal places for the currency or token.

## Mechanics

`value` is always an integer string. The human-readable value is:

```
display = value / (10 ^ decimals)
```

Examples:
- `value: "1099", decimals: 2` → `10.99`
- `value: "5000", decimals: 0` → `5000`
- `value: "4250000", decimals: 6` → `4.250000`

When comparing or summing amounts:
- Only combine values with the **same** `currency` and `decimals`.
- If you must combine different `decimals`, normalize by scaling the smaller precision to the larger one before arithmetic.

For escrow, `currency` should align with `token.symbol` and `decimals` should match `token.decimals`.

## Examples

USD ($10.99):

```json
{ "value": "1099", "currency": "USD", "decimals": 2 }
```

JPY (¥5000):

```json
{ "value": "5000", "currency": "JPY", "decimals": 0 }
```

KWD (3 decimals):

```json
{ "value": "1250", "currency": "KWD", "decimals": 3 }
```

USDC (6 decimals):

```json
{ "value": "4250000", "currency": "USDC", "decimals": 6 }
```
