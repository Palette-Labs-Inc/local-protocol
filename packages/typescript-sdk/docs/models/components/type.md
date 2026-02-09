# Type

Media type discriminator.

## Example Usage

```typescript
import { Type } from "@localprotocol/sdk/models/components";

let value: Type = "image";
```

## Values

This is an open enum. Unrecognized values will be captured as the `Unrecognized<string>` branded type.

```typescript
"image" | "video" | "model_3d" | Unrecognized<string>
```