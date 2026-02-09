# ModifierItem

A purchasable modifier item within a modifier group.


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `id`                                                                                 | *string*                                                                             | :heavy_check_mark:                                                                   | Modifier item identifier.                                                            |
| `name`                                                                               | *string*                                                                             | :heavy_check_mark:                                                                   | Modifier item name.                                                                  |
| `description`                                                                        | *?string*                                                                            | :heavy_minus_sign:                                                                   | Optional modifier item description.                                                  |
| `price`                                                                              | [Components\Amount](../../Models/Components/Amount.md)                               | :heavy_check_mark:                                                                   | Amount with explicit currency. Value is always in minor units (e.g., cents for USD). |
| `metadata`                                                                           | array<string, *mixed*>                                                               | :heavy_minus_sign:                                                                   | Business-defined custom data.                                                        |