// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../core/resource';
import * as MerchantsAPI from './merchants';
import * as PaymentInstrumentsAPI from './payment-instruments';
import { APIPromise } from '../core/api-promise';
import { RequestOptions } from '../internal/request-options';
import { path } from '../internal/utils/path';

export class Merchants extends APIResource {
  /**
   * Returns a merchant with its full denormalized catalog tree.
   */
  retrieve(merchantID: string, options?: RequestOptions): APIPromise<MerchantRetrieveResponse> {
    return this._client.get(path`/merchants/${merchantID}`, options);
  }
}

/**
 * Availability schedule for a catalog, category, or item.
 */
export interface Availability {
  /**
   * Availability intervals (weekly or date-specific).
   */
  intervals: Array<Availability.Interval>;

  /**
   * IANA timezone. Defaults to merchant timezone when omitted.
   */
  timezone?: string;
}

export namespace Availability {
  /**
   * A single time interval for a day of the week or a specific date.
   */
  export interface Interval {
    /**
     * Start hour (0-23).
     */
    from_hour: number;

    /**
     * Start minute (0-59).
     */
    from_minute: number;

    /**
     * End hour (0-23).
     */
    to_hour: number;

    /**
     * End minute (0-59).
     */
    to_minute: number;

    /**
     * Calendar date in YYYY-MM-DD.
     */
    date?: string;

    /**
     * Day of week (e.g., Monday, Tuesday).
     */
    day?: string;
  }
}

/**
 * A category grouping items in a catalog.
 */
export interface CatalogCategory {
  /**
   * Category identifier.
   */
  id: string;

  /**
   * Ordered items in this category.
   */
  items: Array<CatalogCategory.Item>;

  /**
   * Category display name.
   */
  name: string;

  /**
   * Category availability.
   */
  availability?: Availability;

  /**
   * Ordered child categories for nested category trees.
   */
  categories?: Array<CatalogCategory>;

  /**
   * Optional category description.
   */
  description?: string;

  /**
   * Business-defined custom data.
   */
  metadata?: { [key: string]: unknown };
}

export namespace CatalogCategory {
  /**
   * A menu item with embedded modifier groups.
   */
  export interface Item {
    /**
     * Item identifier.
     */
    id: string;

    /**
     * Item description.
     */
    description: string;

    /**
     * Item name.
     */
    name: string;

    /**
     * Base price for the item.
     */
    price: PaymentInstrumentsAPI.Amount;

    /**
     * Item availability.
     */
    availability?: MerchantsAPI.Availability;

    /**
     * Item media (images, videos, 3D models).
     */
    media?: Array<Item.Media>;

    /**
     * Business-defined custom data.
     */
    metadata?: { [key: string]: unknown };

    /**
     * Modifier groups available for this item.
     */
    modifier_groups?: Array<MerchantsAPI.ModifierGroup>;
  }

  export namespace Item {
    /**
     * Product media item (image, video, etc.).
     */
    export interface Media {
      /**
       * Media type discriminator.
       */
      type: 'image' | 'video' | 'model_3d';

      /**
       * URL to the media resource.
       */
      url: string;

      /**
       * Accessibility text describing the media.
       */
      alt_text?: string;

      /**
       * Height in pixels.
       */
      height?: number;

      /**
       * Width in pixels.
       */
      width?: number;
    }
  }
}

/**
 * Group of modifier options with selection constraints.
 */
export interface ModifierGroup {
  /**
   * Modifier group identifier.
   */
  id: string;

  /**
   * Ordered modifier options within this group.
   */
  modifier_options: Array<ModifierOption>;

  /**
   * Display name for the modifier group.
   */
  name: string;

  /**
   * Whether options can be selected with quantities > 1.
   */
  allow_quantities?: boolean;

  /**
   * Optional modifier group description.
   */
  description?: string;

  /**
   * Maximum quantity per modifier option.
   */
  max_per_modifier?: number;

  /**
   * Maximum selections allowed.
   */
  maximum_selections?: number;

  /**
   * Business-defined custom data.
   */
  metadata?: { [key: string]: unknown };

  /**
   * Minimum selections required.
   */
  minimum_selections?: number;

  /**
   * Modifier group type classification.
   */
  type?: string;
}

/**
 * Selectable option within a modifier group.
 */
export interface ModifierOption {
  /**
   * Modifier option identifier.
   */
  id: string;

  /**
   * Modifier item for this option.
   */
  modifier_item: ModifierOption.ModifierItem;

  /**
   * Nested modifier groups required after selecting this option.
   */
  child_modifier_groups?: Array<ModifierGroup>;

  /**
   * Whether this option is selected by default.
   */
  is_default?: boolean;

  /**
   * Business-defined custom data.
   */
  metadata?: { [key: string]: unknown };
}

export namespace ModifierOption {
  /**
   * Modifier item for this option.
   */
  export interface ModifierItem {
    /**
     * Modifier item identifier.
     */
    id: string;

    /**
     * Modifier item name.
     */
    name: string;

    /**
     * Price for this modifier item.
     */
    price: PaymentInstrumentsAPI.Amount;

    /**
     * Optional modifier item description.
     */
    description?: string;

    /**
     * Business-defined custom data.
     */
    metadata?: { [key: string]: unknown };
  }
}

/**
 * Merchant catalog payload containing denormalized catalogs.
 */
export interface MerchantRetrieveResponse {
  /**
   * Merchant identifier.
   */
  id: string;

  /**
   * Catalogs available for the merchant.
   */
  catalogs: Array<MerchantRetrieveResponse.Catalog>;

  /**
   * Merchant name.
   */
  name: string;

  /**
   * IANA timezone for availability schedules.
   */
  timezone: string;

  /**
   * RFC 3339 timestamp of the latest catalog update.
   */
  last_updated?: string;

  /**
   * Business-defined custom data.
   */
  metadata?: { [key: string]: unknown };
}

export namespace MerchantRetrieveResponse {
  /**
   * A catalog containing embedded categories, items, availability, and fulfillment
   * configuration.
   */
  export interface Catalog {
    /**
     * Catalog identifier.
     */
    id: string;

    /**
     * Ordered top-level categories.
     */
    categories: Array<MerchantsAPI.CatalogCategory>;

    /**
     * Catalog name.
     */
    name: string;

    /**
     * Catalog-wide availability override.
     */
    availability?: MerchantsAPI.Availability;

    /**
     * Catalog description.
     */
    description?: string;

    /**
     * Items not assigned to a category.
     */
    items?: Array<Catalog.Item>;

    /**
     * Business-defined custom data.
     */
    metadata?: { [key: string]: unknown };
  }

  export namespace Catalog {
    /**
     * A menu item with embedded modifier groups.
     */
    export interface Item {
      /**
       * Item identifier.
       */
      id: string;

      /**
       * Item description.
       */
      description: string;

      /**
       * Item name.
       */
      name: string;

      /**
       * Base price for the item.
       */
      price: PaymentInstrumentsAPI.Amount;

      /**
       * Item availability.
       */
      availability?: MerchantsAPI.Availability;

      /**
       * Item media (images, videos, 3D models).
       */
      media?: Array<Item.Media>;

      /**
       * Business-defined custom data.
       */
      metadata?: { [key: string]: unknown };

      /**
       * Modifier groups available for this item.
       */
      modifier_groups?: Array<MerchantsAPI.ModifierGroup>;
    }

    export namespace Item {
      /**
       * Product media item (image, video, etc.).
       */
      export interface Media {
        /**
         * Media type discriminator.
         */
        type: 'image' | 'video' | 'model_3d';

        /**
         * URL to the media resource.
         */
        url: string;

        /**
         * Accessibility text describing the media.
         */
        alt_text?: string;

        /**
         * Height in pixels.
         */
        height?: number;

        /**
         * Width in pixels.
         */
        width?: number;
      }
    }
  }
}

export declare namespace Merchants {
  export {
    type Availability as Availability,
    type CatalogCategory as CatalogCategory,
    type ModifierGroup as ModifierGroup,
    type ModifierOption as ModifierOption,
    type MerchantRetrieveResponse as MerchantRetrieveResponse,
  };
}
