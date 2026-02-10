// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../core/resource';
import * as QuotesAPI from './quotes';
import { DeliveryQuote, QuoteCreateParams, QuoteListResponse, QuoteRetrieveParams, Quotes } from './quotes';
import { APIPromise } from '../../core/api-promise';
import { RequestOptions } from '../../internal/request-options';
import { path } from '../../internal/utils/path';

export class Requests extends APIResource {
  quotes: QuotesAPI.Quotes = new QuotesAPI.Quotes(this._client);

  /**
   * Submit a new delivery request. The `nonce` field provides idempotency.
   */
  create(body: RequestCreateParams, options?: RequestOptions): APIPromise<DeliveryRequest> {
    return this._client.post('/requests', { body, ...options });
  }

  /**
   * Returns a single delivery request by ID.
   */
  retrieve(requestID: string, options?: RequestOptions): APIPromise<DeliveryRequest> {
    return this._client.get(path`/requests/${requestID}`, options);
  }

  /**
   * Returns all delivery requests.
   */
  list(options?: RequestOptions): APIPromise<RequestListResponse> {
    return this._client.get('/requests', options);
  }
}

/**
 * Geographic coordinates.
 */
export interface Coordinates {
  /**
   * Latitude in decimal degrees.
   */
  latitude: number;

  /**
   * Longitude in decimal degrees.
   */
  longitude: number;
}

/**
 * A delivery request.
 */
export interface DeliveryRequest {
  /**
   * Unique request identifier.
   */
  id: string;

  /**
   * A location specified by coordinates and/or postal address. At least one must be
   * provided.
   */
  dropoff_location: Location;

  /**
   * Requested dropoff time (RFC 3339).
   */
  dropoff_time: string;

  /**
   * Client-generated idempotency key.
   */
  nonce: string;

  /**
   * A location specified by coordinates and/or postal address. At least one must be
   * provided.
   */
  pickup_location: Location;

  /**
   * Requested pickup time (RFC 3339).
   */
  pickup_time: string;

  /**
   * Dropoff directions, access codes, or delivery notes.
   */
  dropoff_instructions?: string;

  /**
   * Pickup directions, access codes, or handling notes.
   */
  pickup_instructions?: string;
}

/**
 * A location specified by coordinates and/or postal address. At least one must be
 * provided.
 */
export interface Location {
  /**
   * Geographic coordinates.
   */
  coordinates?: Coordinates;

  postal_address?: PostalAddress;
}

export interface PostalAddress {
  /**
   * Country (ISO 3166-1 alpha-2 recommended).
   */
  address_country?: string;

  /**
   * City or locality.
   */
  address_locality?: string;

  /**
   * State, province, or region.
   */
  address_region?: string;

  /**
   * Address extension (apartment number, C/O, etc.).
   */
  extended_address?: string;

  /**
   * Contact first name.
   */
  first_name?: string;

  /**
   * Contact last name.
   */
  last_name?: string;

  /**
   * Contact phone number.
   */
  phone_number?: string;

  /**
   * Postal code.
   */
  postal_code?: string;

  /**
   * The street address.
   */
  street_address?: string;
}

export type RequestListResponse = Array<DeliveryRequest>;

export interface RequestCreateParams {
  /**
   * Unique request identifier.
   */
  id: string;

  /**
   * A location specified by coordinates and/or postal address. At least one must be
   * provided.
   */
  dropoff_location: Location;

  /**
   * Requested dropoff time (RFC 3339).
   */
  dropoff_time: string;

  /**
   * Client-generated idempotency key.
   */
  nonce: string;

  /**
   * A location specified by coordinates and/or postal address. At least one must be
   * provided.
   */
  pickup_location: Location;

  /**
   * Requested pickup time (RFC 3339).
   */
  pickup_time: string;

  /**
   * Dropoff directions, access codes, or delivery notes.
   */
  dropoff_instructions?: string;

  /**
   * Pickup directions, access codes, or handling notes.
   */
  pickup_instructions?: string;
}

Requests.Quotes = Quotes;

export declare namespace Requests {
  export {
    type Coordinates as Coordinates,
    type DeliveryRequest as DeliveryRequest,
    type Location as Location,
    type PostalAddress as PostalAddress,
    type RequestListResponse as RequestListResponse,
    type RequestCreateParams as RequestCreateParams,
  };

  export {
    Quotes as Quotes,
    type DeliveryQuote as DeliveryQuote,
    type QuoteListResponse as QuoteListResponse,
    type QuoteCreateParams as QuoteCreateParams,
    type QuoteRetrieveParams as QuoteRetrieveParams,
  };
}
