# ModifierOption

Selectable option within a modifier group.

## Example Usage

```typescript
import { ModifierOption } from "@localprotocol/sdk/models/components";

let value: ModifierOption = {
  id: "<id>",
  modifierItem: {
    id: "<id>",
    name: "<value>",
    price: {
      value: "<value>",
      currency: {
        chainId: 793765,
        address: "9303 Belmont Road",
        decimals: 989280,
      },
    },
  },
};
```

## Fields

| Field                                                                   | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `id`                                                                    | *string*                                                                | :heavy_check_mark:                                                      | Modifier option identifier.                                             |
| `modifierItem`                                                          | [components.ModifierItem](../../models/components/modifier-item.md)     | :heavy_check_mark:                                                      | A purchasable modifier item within a modifier group.                    |
| `childModifierGroups`                                                   | [components.ModifierGroup](../../models/components/modifier-group.md)[] | :heavy_minus_sign:                                                      | Nested modifier groups required after selecting this option.            |
| `isDefault`                                                             | *boolean*                                                               | :heavy_minus_sign:                                                      | Whether this option is selected by default.                             |
| `metadata`                                                              | Record<string, *any*>                                                   | :heavy_minus_sign:                                                      | Business-defined custom data.                                           |