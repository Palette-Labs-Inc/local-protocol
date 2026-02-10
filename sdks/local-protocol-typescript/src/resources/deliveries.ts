// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../core/resource';
import { APIPromise } from '../core/api-promise';
import { RequestOptions } from '../internal/request-options';
import { path } from '../internal/utils/path';

/**
 * Accept quotes and manage delivery lifecycle state.
 */
export class Deliveries extends APIResource {
  /**
   * Accept a quote and create a delivery. The `nonce` field provides idempotency.
   */
  create(body: DeliveryCreateParams, options?: RequestOptions): APIPromise<Delivery> {
    return this._client.post('/deliveries', { body, ...options });
  }

  /**
   * Returns a single delivery by ID.
   */
  retrieve(deliveryID: string, options?: RequestOptions): APIPromise<Delivery> {
    return this._client.get(path`/deliveries/${deliveryID}`, options);
  }

  /**
   * Returns all deliveries.
   */
  list(options?: RequestOptions): APIPromise<DeliveryListResponse> {
    return this._client.get('/deliveries', options);
  }

  /**
   * Transition a delivery to a new event state. If a webhook URL was registered, the
   * server pushes an event notification in the background.
   */
  updateEvent(
    deliveryID: string,
    body: DeliveryUpdateEventParams,
    options?: RequestOptions,
  ): APIPromise<Delivery> {
    return this._client.patch(path`/deliveries/${deliveryID}/event`, { body, ...options });
  }
}

/**
 * A delivery resource.
 */
export interface Delivery {
  /**
   * Unique delivery identifier.
   */
  id: string;

  /**
   * Creation timestamp (RFC 3339).
   */
  created_at: string;

  /**
   * Current event identifier.
   */
  event: string;

  /**
   * Human-readable description of the current event.
   */
  event_description: string;

  /**
   * Event vocabulary standard in use.
   */
  event_vocabulary: string;

  /**
   * Reference to the payment instrument used to create this delivery.
   */
  payment_instrument_id: string;

  /**
   * Reference to the accepted quote.
   */
  quote_id: string;

  /**
   * Reference to the delivery request.
   */
  request_id: string;

  /**
   * Last update timestamp (RFC 3339).
   */
  updated_at: string;

  /**
   * Registered webhook URL, if any.
   */
  webhook_url?: string | null;
}

export type DeliveryListResponse = Array<Delivery>;

export interface DeliveryCreateParams {
  /**
   * Client-generated idempotency key.
   */
  nonce: string;

  /**
   * The accepted quote.
   */
  quote_id: string;

  /**
   * The delivery request to fulfill.
   */
  request_id: string;

  /**
   * Event vocabulary standard to use.
   */
  event_vocabulary?: string;

  /**
   * Optional URL to receive delivery event webhook notifications.
   */
  webhook_url?: string | null;
}

export interface DeliveryUpdateEventParams {
  /**
   * Event identifier from the delivery's event vocabulary.
   */
  event: string;

  /**
   * Human-readable event description.
   */
  event_description: string;
}

export declare namespace Deliveries {
  export {
    type Delivery as Delivery,
    type DeliveryListResponse as DeliveryListResponse,
    type DeliveryCreateParams as DeliveryCreateParams,
    type DeliveryUpdateEventParams as DeliveryUpdateEventParams,
  };
}
