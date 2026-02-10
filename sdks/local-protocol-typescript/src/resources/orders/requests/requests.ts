// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../../core/resource';
import * as QuotesAPI from './quotes';
import { OrderQuote, QuoteListResponse, QuoteRetrieveParams, Quotes } from './quotes';
import { APIPromise } from '../../../core/api-promise';
import { RequestOptions } from '../../../internal/request-options';

export class Requests extends APIResource {
  quotes: QuotesAPI.Quotes = new QuotesAPI.Quotes(this._client);

  /**
   * Submit a new order request with a cart. The `nonce` field provides idempotency.
   */
  create(body: RequestCreateParams, options?: RequestOptions): APIPromise<RequestCreateResponse> {
    return this._client.post('/orders/requests', { body, ...options });
  }
}

/**
 * An order request.
 */
export interface RequestCreateResponse {
  /**
   * Unique request identifier.
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
}

export interface RequestCreateParams {
  /**
   * Unique cart identifier.
   */
  id: string;

  /**
   * Shared intent identifier for tracing Request -> Quote -> Order.
   */
  intent_id: string;

  /**
   * Items in the cart.
   */
  items: Array<RequestCreateParams.Item>;

  /**
   * Client-generated idempotency key.
   */
  nonce: string;
}

export namespace RequestCreateParams {
  /**
   * An item in a cart.
   */
  export interface Item {
    /**
     * Item identifier.
     */
    id: string;

    /**
     * Quantity requested.
     */
    quantity: number;
  }
}

Requests.Quotes = Quotes;

export declare namespace Requests {
  export {
    type RequestCreateResponse as RequestCreateResponse,
    type RequestCreateParams as RequestCreateParams,
  };

  export {
    Quotes as Quotes,
    type OrderQuote as OrderQuote,
    type QuoteListResponse as QuoteListResponse,
    type QuoteRetrieveParams as QuoteRetrieveParams,
  };
}
