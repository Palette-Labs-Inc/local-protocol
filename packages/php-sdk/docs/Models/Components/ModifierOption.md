# ModifierOption

Selectable option within a modifier group.


## Fields

| Field                                                                       | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `id`                                                                        | *string*                                                                    | :heavy_check_mark:                                                          | Modifier option identifier.                                                 |
| `modifierItem`                                                              | [Components\ModifierItem](../../Models/Components/ModifierItem.md)          | :heavy_check_mark:                                                          | A purchasable modifier item within a modifier group.                        |
| `childModifierGroups`                                                       | array<[Components\ModifierGroup](../../Models/Components/ModifierGroup.md)> | :heavy_minus_sign:                                                          | Nested modifier groups required after selecting this option.                |
| `isDefault`                                                                 | *?bool*                                                                     | :heavy_minus_sign:                                                          | Whether this option is selected by default.                                 |
| `metadata`                                                                  | array<string, *mixed*>                                                      | :heavy_minus_sign:                                                          | Business-defined custom data.                                               |