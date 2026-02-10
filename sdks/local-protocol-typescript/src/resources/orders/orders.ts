// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../core/resource';
import * as RequestsAPI from './requests/requests';
import { RequestCreateParams, RequestCreateResponse, Requests } from './requests/requests';
import { APIPromise } from '../../core/api-promise';
import { RequestOptions } from '../../internal/request-options';
import { path } from '../../internal/utils/path';

/**
 * Create and retrieve orders and order-level requests.
 */
export class Orders extends APIResource {
  requests: RequestsAPI.Requests = new RequestsAPI.Requests(this._client);

  /**
   * Accept a quote and create an order. The `nonce` field provides idempotency.
   */
  create(body: OrderCreateParams, options?: RequestOptions): APIPromise<Order> {
    return this._client.post('/orders', { body, ...options });
  }

  /**
   * Returns a single order by ID.
   */
  retrieve(orderID: string, options?: RequestOptions): APIPromise<Order> {
    return this._client.get(path`/orders/${orderID}`, options);
  }
}

/**
 * An order.
 */
export interface Order {
  /**
   * Unique order identifier.
   */
  id: string;

  /**
   * Shared intent identifier for tracing Request -> Quote -> Order.
   */
  intent_id: string;

  /**
   * Client-generated idempotency key.
   */
  nonce: string;

  /**
   * Reference to the payment instrument used.
   */
  payment_instrument_id: string;
}

export interface OrderCreateParams {
  /**
   * Client-generated idempotency key.
   */
  nonce: string;

  /**
   * The accepted quote.
   */
  order_quote_id: string;

  /**
   * The order request to fulfill.
   */
  order_request_id: string;

  /**
   * Reference to the registered payment instrument.
   */
  payment_instrument_id: string;
}

Orders.Requests = Requests;

export declare namespace Orders {
  export { type Order as Order, type OrderCreateParams as OrderCreateParams };

  export {
    Requests as Requests,
    type RequestCreateResponse as RequestCreateResponse,
    type RequestCreateParams as RequestCreateParams,
  };
}
