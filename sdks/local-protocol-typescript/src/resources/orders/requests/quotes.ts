// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../../core/resource';
import { APIPromise } from '../../../core/api-promise';
import { RequestOptions } from '../../../internal/request-options';
import { path } from '../../../internal/utils/path';

export class Quotes extends APIResource {
  /**
   * Returns a single order quote by ID.
   */
  retrieve(
    orderQuoteID: string,
    params: QuoteRetrieveParams,
    options?: RequestOptions,
  ): APIPromise<OrderQuote> {
    const { order_request_id } = params;
    return this._client.get(path`/orders/requests/${order_request_id}/quotes/${orderQuoteID}`, options);
  }

  /**
   * Returns all quotes for an order request.
   */
  list(orderRequestID: string, options?: RequestOptions): APIPromise<QuoteListResponse> {
    return this._client.get(path`/orders/requests/${orderRequestID}/quotes`, options);
  }
}

/**
 * An order quote.
 */
export interface OrderQuote {
  /**
   * Unique quote identifier.
   */
  id: string;

  /**
   * Quote expiration time (RFC 3339).
   */
  expires_at: string;

  /**
   * Shared intent identifier for tracing Request -> Quote -> Order.
   */
  intent_id: string;

  /**
   * Client-generated idempotency key.
   */
  nonce: string;

  /**
   * Price in minor currency units.
   */
  price: number;

  /**
   * Estimated readiness time (RFC 3339).
   */
  ready_at: string;
}

export type QuoteListResponse = Array<OrderQuote>;

export interface QuoteRetrieveParams {
  /**
   * Order request identifier.
   */
  order_request_id: string;
}

export declare namespace Quotes {
  export {
    type OrderQuote as OrderQuote,
    type QuoteListResponse as QuoteListResponse,
    type QuoteRetrieveParams as QuoteRetrieveParams,
  };
}
