// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import LocalProtocol from 'local-protocol';

const client = new LocalProtocol({
  apiKey: 'My API Key',
  baseURL: process.env['TEST_API_BASE_URL'] ?? 'http://127.0.0.1:4010',
});

describe('resource quotes', () => {
  // Prism tests are disabled
  test.skip('create: only required params', async () => {
    const responsePromise = client.requests.quotes.create('request_id', {
      id: 'id',
      currency: 'SEW',
      dropoff_estimate: '2019-12-27T18:11:19.117Z',
      dropoff_location: {},
      nonce: 'nonce',
      payment: {},
      pickup_estimate: '2019-12-27T18:11:19.117Z',
      pickup_location: {},
      price: 0,
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
    const response = await client.requests.quotes.create('request_id', {
      id: 'id',
      currency: 'SEW',
      dropoff_estimate: '2019-12-27T18:11:19.117Z',
      dropoff_location: {
        coordinates: { latitude: -90, longitude: -180 },
        postal_address: {
          address_country: 'address_country',
          address_locality: 'address_locality',
          address_region: 'address_region',
          extended_address: 'extended_address',
          first_name: 'first_name',
          last_name: 'last_name',
          phone_number: 'phone_number',
          postal_code: 'postal_code',
          street_address: 'street_address',
        },
      },
      nonce: 'nonce',
      payment: {
        instruments: [
          {
            id: 'id',
            handler_id: 'handler_id',
            type: 'type',
            billing_address: {
              address_country: 'address_country',
              address_locality: 'address_locality',
              address_region: 'address_region',
              extended_address: 'extended_address',
              first_name: 'first_name',
              last_name: 'last_name',
              phone_number: 'phone_number',
              postal_code: 'postal_code',
              street_address: 'street_address',
            },
            credential: { type: 'type' },
            display: { foo: 'bar' },
            selected: true,
          },
        ],
      },
      pickup_estimate: '2019-12-27T18:11:19.117Z',
      pickup_location: {
        coordinates: { latitude: -90, longitude: -180 },
        postal_address: {
          address_country: 'address_country',
          address_locality: 'address_locality',
          address_region: 'address_region',
          extended_address: 'extended_address',
          first_name: 'first_name',
          last_name: 'last_name',
          phone_number: 'phone_number',
          postal_code: 'postal_code',
          street_address: 'street_address',
        },
      },
      price: 0,
      expires_at: '2019-12-27T18:11:19.117Z',
    });
  });

  // Prism tests are disabled
  test.skip('retrieve: only required params', async () => {
    const responsePromise = client.requests.quotes.retrieve('quote_id', { request_id: 'request_id' });
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });

  // Prism tests are disabled
  test.skip('retrieve: required and optional params', async () => {
    const response = await client.requests.quotes.retrieve('quote_id', { request_id: 'request_id' });
  });

  // Prism tests are disabled
  test.skip('list', async () => {
    const responsePromise = client.requests.quotes.list('request_id');
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });
});
