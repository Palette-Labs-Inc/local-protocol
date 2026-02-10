// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import LocalProtocol from 'local-protocol';

const client = new LocalProtocol({ baseURL: process.env['TEST_API_BASE_URL'] ?? 'http://127.0.0.1:4010' });

describe('resource orders', () => {
  // Prism tests are disabled
  test.skip('create: only required params', async () => {
    const responsePromise = client.orders.create({
      nonce: 'nonce',
      order_quote_id: 'order_quote_id',
      order_request_id: 'order_request_id',
      payment_instrument_id: 'payment_instrument_id',
    });
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });

  // Prism tests are disabled
  test.skip('create: required and optional params', async () => {
    const response = await client.orders.create({
      nonce: 'nonce',
      order_quote_id: 'order_quote_id',
      order_request_id: 'order_request_id',
      payment_instrument_id: 'payment_instrument_id',
    });
  });

  // Prism tests are disabled
  test.skip('retrieve', async () => {
    const responsePromise = client.orders.retrieve('order_id');
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });
});
