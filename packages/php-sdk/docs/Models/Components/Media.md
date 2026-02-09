# Media

Product media item (image, video, etc.).


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `type`                                             | [Components\Type](../../Models/Components/Type.md) | :heavy_check_mark:                                 | Media type discriminator.                          |
| `url`                                              | *string*                                           | :heavy_check_mark:                                 | URL to the media resource.                         |
| `altText`                                          | *?string*                                          | :heavy_minus_sign:                                 | Accessibility text describing the media.           |
| `width`                                            | *?int*                                             | :heavy_minus_sign:                                 | Width in pixels.                                   |
| `height`                                           | *?int*                                             | :heavy_minus_sign:                                 | Height in pixels.                                  |