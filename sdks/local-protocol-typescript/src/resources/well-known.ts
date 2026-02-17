// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../core/resource';
import { APIPromise } from '../core/api-promise';
import { RequestOptions } from '../internal/request-options';

/**
 * Discover server capabilities, standards, and endpoints.
 */
export class WellKnown extends APIResource {
  /**
   * Returns server capabilities, supported standards, and endpoint paths.
   */
  retrieve(options?: RequestOptions): APIPromise<WellKnownRetrieveResponse> {
    return this._client.get('/.well-known/ucp', options);
  }
}

/**
 * Service discovery metadata.
 */
export interface WellKnownRetrieveResponse {
  /**
   * Canonical UCP discovery profile.
   */
  ucp: WellKnown.Ucp;
}

export declare namespace WellKnown {
  export interface Ucp {
    version: string;
    services: { [key: string]: Array<WellKnown.UcpServiceEntry> };
    capabilities: { [key: string]: Array<WellKnown.UcpCapabilityEntry> };
    payment_handlers: { [key: string]: Array<WellKnown.UcpPaymentHandlerEntry> };
  }

  export interface UcpServiceEntry {
    version: string;
    spec: string;
    transport: 'rest' | 'mcp' | 'a2a' | 'embedded';
    endpoint?: string;
    schema?: string;
    [k: string]: unknown;
  }

  export interface UcpCapabilityEntry {
    version: string;
    spec: string;
    schema: string;
    extends?: string | Array<string>;
    [k: string]: unknown;
  }

  export interface UcpPaymentHandlerEntry {
    id: string;
    version: string;
    spec?: string;
    schema?: string;
    config?: { [k: string]: unknown };
    [k: string]: unknown;
  }

  export { type WellKnownRetrieveResponse as WellKnownRetrieveResponse };
}
