// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import LocalProtocol from 'local-protocol';

const client = new LocalProtocol({
  apiKey: 'My API Key',
  baseURL: process.env['TEST_API_BASE_URL'] ?? 'http://127.0.0.1:4010',
});

describe('resource deliveries', () => {
  // Prism tests are disabled
  test.skip('create: only required params', async () => {
    const responsePromise = client.deliveries.create({
      nonce: 'nonce',
      quote_id: 'quote_id',
      request_id: 'request_id',
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
    const response = await client.deliveries.create({
      nonce: 'nonce',
      quote_id: 'quote_id',
      request_id: 'request_id',
      event_vocabulary: 'event_vocabulary',
      webhook_url: 'webhook_url',
    });
  });

  // Prism tests are disabled
  test.skip('retrieve', async () => {
    const responsePromise = client.deliveries.retrieve('delivery_id');
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });

  // Prism tests are disabled
  test.skip('list', async () => {
    const responsePromise = client.deliveries.list();
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });

  // Prism tests are disabled
  test.skip('updateEvent: only required params', async () => {
    const responsePromise = client.deliveries.updateEvent('delivery_id', {
      event: 'event',
      event_description: 'event_description',
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
  test.skip('updateEvent: required and optional params', async () => {
    const response = await client.deliveries.updateEvent('delivery_id', {
      event: 'event',
      event_description: 'event_description',
    });
  });
});
