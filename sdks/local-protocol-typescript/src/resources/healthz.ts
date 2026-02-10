// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../core/resource';
import { APIPromise } from '../core/api-promise';
import { RequestOptions } from '../internal/request-options';

export class Healthz extends APIResource {
  /**
   * Returns server health status.
   */
  check(options?: RequestOptions): APIPromise<HealthzCheckResponse> {
    return this._client.get('/healthz', options);
  }
}

/**
 * Health check response.
 */
export interface HealthzCheckResponse {
  status: 'ok';
}

export declare namespace Healthz {
  export { type HealthzCheckResponse as HealthzCheckResponse };
}
