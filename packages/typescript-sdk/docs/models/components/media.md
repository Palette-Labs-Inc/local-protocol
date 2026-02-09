# Media

Product media item (image, video, etc.).

## Example Usage

```typescript
import { Media } from "@localprotocol/sdk/models/components";

let value: Media = {
  type: "model_3d",
  url: "https://tasty-draft.org/",
};
```

## Fields

| Field                                              | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `type`                                             | [components.Type](../../models/components/type.md) | :heavy_check_mark:                                 | Media type discriminator.                          |
| `url`                                              | *string*                                           | :heavy_check_mark:                                 | URL to the media resource.                         |
| `altText`                                          | *string*                                           | :heavy_minus_sign:                                 | Accessibility text describing the media.           |
| `width`                                            | *number*                                           | :heavy_minus_sign:                                 | Width in pixels.                                   |
| `height`                                           | *number*                                           | :heavy_minus_sign:                                 | Height in pixels.                                  |