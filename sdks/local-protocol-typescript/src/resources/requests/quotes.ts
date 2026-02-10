// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../core/resource';
import * as PaymentInstrumentsAPI from '../payment-instruments';
import * as RequestsAPI from './requests';
import { APIPromise } from '../../core/api-promise';
import { RequestOptions } from '../../internal/request-options';
import { path } from '../../internal/utils/path';

export class Quotes extends APIResource {
  /**
   * Submit a quote for a delivery request. The `nonce` field provides idempotency.
   */
  create(requestID: string, body: QuoteCreateParams, options?: RequestOptions): APIPromise<DeliveryQuote> {
    return this._client.post(path`/requests/${requestID}/quotes`, { body, ...options });
  }

  /**
   * Returns a single quote by ID.
   */
  retrieve(
    quoteID: string,
    params: QuoteRetrieveParams,
    options?: RequestOptions,
  ): APIPromise<DeliveryQuote> {
    const { request_id } = params;
    return this._client.get(path`/requests/${request_id}/quotes/${quoteID}`, options);
  }

  /**
   * Returns all quotes for a delivery request.
   */
  list(requestID: string, options?: RequestOptions): APIPromise<QuoteListResponse> {
    return this._client.get(path`/requests/${requestID}/quotes`, options);
  }
}

/**
 * A delivery quote.
 */
export interface DeliveryQuote {
  /**
   * Unique quote identifier.
   */
  id: string;

  /**
   * ISO 4217 currency code.
   */
  currency: string;

  /**
   * Estimated dropoff time (RFC 3339).
   */
  dropoff_estimate: string;

  /**
   * A location specified by coordinates and/or postal address. At least one must be
   * provided.
   */
  dropoff_location: RequestsAPI.Location;

  /**
   * Client-generated idempotency key.
   */
  nonce: string;

  /**
   * Payment handlers available for accepting this quote.
   */
  payment: DeliveryQuote.Payment;

  /**
   * Estimated pickup time (RFC 3339).
   */
  pickup_estimate: string;

  /**
   * A location specified by coordinates and/or postal address. At least one must be
   * provided.
   */
  pickup_location: RequestsAPI.Location;

  /**
   * Price in minor currency units.
   */
  price: number;

  /**
   * Time when the quote expires (RFC 3339).
   */
  expires_at?: string;
}

export namespace DeliveryQuote {
  /**
   * Payment handlers available for accepting this quote.
   */
  export interface Payment {
    /**
     * Payment instruments available. Each instrument is associated with a handler via
     * handler_id.
     */
    instruments?: Array<Payment.Instrument>;
  }

  export namespace Payment {
    /**
     * A payment instrument with selection state.
     */
    export interface Instrument extends PaymentInstrumentsAPI.PaymentInstrument {
      /**
       * Whether this instrument is selected by the user.
       */
      selected?: boolean;
    }
  }
}

export type QuoteListResponse = Array<DeliveryQuote>;

export interface QuoteCreateParams {
  /**
   * Unique quote identifier.
   */
  id: string;

  /**
   * ISO 4217 currency code.
   */
  currency: string;

  /**
   * Estimated dropoff time (RFC 3339).
   */
  dropoff_estimate: string;

  /**
   * A location specified by coordinates and/or postal address. At least one must be
   * provided.
   */
  dropoff_location: RequestsAPI.Location;

  /**
   * Client-generated idempotency key.
   */
  nonce: string;

  /**
   * Payment handlers available for accepting this quote.
   */
  payment: QuoteCreateParams.Payment;

  /**
   * Estimated pickup time (RFC 3339).
   */
  pickup_estimate: string;

  /**
   * A location specified by coordinates and/or postal address. At least one must be
   * provided.
   */
  pickup_location: RequestsAPI.Location;

  /**
   * Price in minor currency units.
   */
  price: number;

  /**
   * Time when the quote expires (RFC 3339).
   */
  expires_at?: string;
}

export namespace QuoteCreateParams {
  /**
   * Payment handlers available for accepting this quote.
   */
  export interface Payment {
    /**
     * Payment instruments available. Each instrument is associated with a handler via
     * handler_id.
     */
    instruments?: Array<Payment.Instrument>;
  }

  export namespace Payment {
    /**
     * A payment instrument with selection state.
     */
    export interface Instrument extends PaymentInstrumentsAPI.PaymentInstrument {
      /**
       * Whether this instrument is selected by the user.
       */
      selected?: boolean;
    }
  }
}

export interface QuoteRetrieveParams {
  /**
   * Delivery request identifier.
   */
  request_id: string;
}

export declare namespace Quotes {
  export {
    type DeliveryQuote as DeliveryQuote,
    type QuoteListResponse as QuoteListResponse,
    type QuoteCreateParams as QuoteCreateParams,
    type QuoteRetrieveParams as QuoteRetrieveParams,
  };
}
