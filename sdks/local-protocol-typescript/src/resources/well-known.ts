// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../core/resource';
import { APIPromise } from '../core/api-promise';
import { RequestOptions } from '../internal/request-options';

export class WellKnown extends APIResource {
  /**
   * Returns server capabilities, supported standards, and endpoint paths.
   */
  retrieve(options?: RequestOptions): APIPromise<WellKnownRetrieveResponse> {
    return this._client.get('/.well-known/local-protocol', options);
  }
}

/**
 * Service discovery metadata.
 */
export interface WellKnownRetrieveResponse {
  /**
   * Supported capabilities by domain.
   */
  capabilities: { [key: string]: unknown };

  /**
   * Endpoint path map.
   */
  endpoints: { [key: string]: string };

  /**
   * Server name.
   */
  name: string;

  /**
   * Protocol version.
   */
  version: string;
}

export declare namespace WellKnown {
  export { type WellKnownRetrieveResponse as WellKnownRetrieveResponse };
}
