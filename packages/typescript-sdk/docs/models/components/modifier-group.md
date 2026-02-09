# ModifierGroup

Group of modifier options with selection constraints.

## Example Usage

```typescript
import { ModifierGroup } from "@localprotocol/sdk/models/components";

let value: ModifierGroup = {
  id: "<id>",
  name: "<value>",
  modifierOptions: [
    {
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
    },
  ],
};
```

## Fields

| Field                                                                     | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `id`                                                                      | *string*                                                                  | :heavy_check_mark:                                                        | Modifier group identifier.                                                |
| `name`                                                                    | *string*                                                                  | :heavy_check_mark:                                                        | Display name for the modifier group.                                      |
| `description`                                                             | *string*                                                                  | :heavy_minus_sign:                                                        | Optional modifier group description.                                      |
| `minimumSelections`                                                       | *number*                                                                  | :heavy_minus_sign:                                                        | Minimum selections required.                                              |
| `maximumSelections`                                                       | *number*                                                                  | :heavy_minus_sign:                                                        | Maximum selections allowed.                                               |
| `allowQuantities`                                                         | *boolean*                                                                 | :heavy_minus_sign:                                                        | Whether options can be selected with quantities > 1.                      |
| `maxPerModifier`                                                          | *number*                                                                  | :heavy_minus_sign:                                                        | Maximum quantity per modifier option.                                     |
| `modifierOptions`                                                         | [components.ModifierOption](../../models/components/modifier-option.md)[] | :heavy_check_mark:                                                        | Ordered modifier options within this group.                               |
| `type`                                                                    | *string*                                                                  | :heavy_minus_sign:                                                        | Modifier group type classification.                                       |
| `metadata`                                                                | Record<string, *any*>                                                     | :heavy_minus_sign:                                                        | Business-defined custom data.                                             |