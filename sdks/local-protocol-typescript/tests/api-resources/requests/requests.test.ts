// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import LocalProtocol from 'local-protocol';

const client = new LocalProtocol({ baseURL: process.env['TEST_API_BASE_URL'] ?? 'http://127.0.0.1:4010' });

describe('resource requests', () => {
  // Prism tests are disabled
  test.skip('create: only required params', async () => {
    const responsePromise = client.requests.create({
      id: 'id',
      dropoff_location: {},
      dropoff_time: '2019-12-27T18:11:19.117Z',
      nonce: 'nonce',
      pickup_location: {},
      pickup_time: '2019-12-27T18:11:19.117Z',
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
    const response = await client.requests.create({
      id: 'id',
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
      dropoff_time: '2019-12-27T18:11:19.117Z',
      nonce: 'nonce',
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
      pickup_time: '2019-12-27T18:11:19.117Z',
      dropoff_instructions: 'dropoff_instructions',
      pickup_instructions: 'pickup_instructions',
    });
  });

  // Prism tests are disabled
  test.skip('retrieve', async () => {
    const responsePromise = client.requests.retrieve('request_id');
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
    const responsePromise = client.requests.list();
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });
});
