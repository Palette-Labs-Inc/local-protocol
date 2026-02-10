// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import type { LocalProtocol } from '../client';

export abstract class APIResource {
  protected _client: LocalProtocol;

  constructor(client: LocalProtocol) {
    this._client = client;
  }
}
