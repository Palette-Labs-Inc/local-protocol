// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../core/resource';
import { APIPromise } from '../core/api-promise';
import { RequestOptions } from '../internal/request-options';
import { path } from '../internal/utils/path';

/**
 * Retrieve event vocabulary definitions by name.
 */
export class EventVocabularies extends APIResource {
  /**
   * Returns a delivery event vocabulary by name.
   */
  retrieve(name: string, options?: RequestOptions): APIPromise<EventVocabularyRetrieveResponse> {
    return this._client.get(path`/event-vocabularies/${name}`, options);
  }
}

/**
 * Schema for delivery event vocabularies.
 */
export interface EventVocabularyRetrieveResponse {
  /**
   * Map of event IDs to event definitions.
   */
  events: { [key: string]: EventVocabularyRetrieveResponse.Events };

  /**
   * Standard identifier in reverse-domain notation.
   */
  name: string;

  /**
   * Human-readable title.
   */
  title: string;

  /**
   * Version in YYYY-MM-DD format.
   */
  version: string;

  /**
   * Human-readable description.
   */
  description?: string;

  /**
   * Parent standard this extends (optional, max one).
   */
  extends?: Array<string>;

  /**
   * URL to specification document.
   */
  spec?: string;
}

export namespace EventVocabularyRetrieveResponse {
  /**
   * A single delivery event definition.
   */
  export interface Events {
    /**
     * Human-readable description of the event.
     */
    description: string;
  }
}

export declare namespace EventVocabularies {
  export { type EventVocabularyRetrieveResponse as EventVocabularyRetrieveResponse };
}
