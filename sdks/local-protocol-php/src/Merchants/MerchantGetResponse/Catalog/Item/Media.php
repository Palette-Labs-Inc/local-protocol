<?php

declare(strict_types=1);

namespace LocalProtocol\Merchants\MerchantGetResponse\Catalog\Item;

use LocalProtocol\Core\Attributes\Optional;
use LocalProtocol\Core\Attributes\Required;
use LocalProtocol\Core\Concerns\SdkModel;
use LocalProtocol\Core\Contracts\BaseModel;
use LocalProtocol\Merchants\MerchantGetResponse\Catalog\Item\Media\Type;

/**
 * Product media item (image, video, etc.).
 *
 * @phpstan-type MediaShape = array{
 *   type: Type|value-of<Type>,
 *   url: string,
 *   altText?: string|null,
 *   height?: int|null,
 *   width?: int|null,
 * }
 */
final class Media implements BaseModel
{
    /** @use SdkModel<MediaShape> */
    use SdkModel;

    /**
     * Media type discriminator.
     *
     * @var value-of<Type> $type
     */
    #[Required(enum: Type::class)]
    public string $type;

    /**
     * URL to the media resource.
     */
    #[Required]
    public string $url;

    /**
     * Accessibility text describing the media.
     */
    #[Optional('alt_text')]
    public ?string $altText;

    /**
     * Height in pixels.
     */
    #[Optional]
    public ?int $height;

    /**
     * Width in pixels.
     */
    #[Optional]
    public ?int $width;

    /**
     * `new Media()` is missing required properties by the API.
     *
     * To enforce required parameters use
     * ```
     * Media::with(type: ..., url: ...)
     * ```
     *
     * Otherwise ensure the following setters are called
     *
     * ```
     * (new Media)->withType(...)->withURL(...)
     * ```
     */
    public function __construct()
    {
        $this->initialize();
    }

    /**
     * Construct an instance from the required parameters.
     *
     * You must use named parameters to construct any parameters with a default value.
     *
     * @param Type|value-of<Type> $type
     */
    public static function with(
        Type|string $type,
        string $url,
        ?string $altText = null,
        ?int $height = null,
        ?int $width = null,
    ): self {
        $self = new self;

        $self['type'] = $type;
        $self['url'] = $url;

        null !== $altText && $self['altText'] = $altText;
        null !== $height && $self['height'] = $height;
        null !== $width && $self['width'] = $width;

        return $self;
    }

    /**
     * Media type discriminator.
     *
     * @param Type|value-of<Type> $type
     */
    public function withType(Type|string $type): self
    {
        $self = clone $this;
        $self['type'] = $type;

        return $self;
    }

    /**
     * URL to the media resource.
     */
    public function withURL(string $url): self
    {
        $self = clone $this;
        $self['url'] = $url;

        return $self;
    }

    /**
     * Accessibility text describing the media.
     */
    public function withAltText(string $altText): self
    {
        $self = clone $this;
        $self['altText'] = $altText;

        return $self;
    }

    /**
     * Height in pixels.
     */
    public function withHeight(int $height): self
    {
        $self = clone $this;
        $self['height'] = $height;

        return $self;
    }

    /**
     * Width in pixels.
     */
    public function withWidth(int $width): self
    {
        $self = clone $this;
        $self['width'] = $width;

        return $self;
    }
}
