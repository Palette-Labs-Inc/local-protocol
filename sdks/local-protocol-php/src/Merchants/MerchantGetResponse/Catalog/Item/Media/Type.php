<?php

declare(strict_types=1);

namespace LocalProtocol\Merchants\MerchantGetResponse\Catalog\Item\Media;

/**
 * Media type discriminator.
 */
enum Type: string
{
    case IMAGE = 'image';

    case VIDEO = 'video';

    case MODEL_3D = 'model_3d';
}
