// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import LocalProtocol from 'local-protocol';

const client = new LocalProtocol({
  apiKey: 'My API Key',
  baseURL: process.env['TEST_API_BASE_URL'] ?? 'http://127.0.0.1:4010',
});

describe('resource paymentInstruments', () => {
  // Prism tests are disabled
  test.skip('register: only required params', async () => {
    const responsePromise = client.paymentInstruments.register({
      id: 'id',
      token: { decimals: 0, symbol: 'symbol' },
      amount: {
        currency: { symbol: 'SQ9_0_L1__5L' },
        value: '269125115713',
      },
      authorization_expires_at: '2019-12-27T18:11:19.117Z',
      chain_id: 1,
      contract: '0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A',
      handler_id: 'handler_id',
      max_amount: {
        currency: { symbol: 'SQ9_0_L1__5L' },
        value: '269125115713',
      },
      nonce: '269125115713',
      operator: '0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A',
      payer: '0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A',
      payment_info_hash: '0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8ACa3CC53eb6CEAA2eaa0Aa6be',
      preapproval_expires_at: '2019-12-27T18:11:19.117Z',
      receiver: '0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A',
      refund_expires_at: '2019-12-27T18:11:19.117Z',
      type: 'evm_auth_capture_escrow',
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
  test.skip('register: required and optional params', async () => {
    const response = await client.paymentInstruments.register({
      id: 'id',
      token: {
        decimals: 0,
        symbol: 'symbol',
        address: '0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A',
      },
      amount: {
        currency: {
          address: '0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A',
          chain_id: 1,
          decimals: 0,
        },
        value: '269125115713',
      },
      authorization_expires_at: '2019-12-27T18:11:19.117Z',
      chain_id: 1,
      contract: '0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A',
      handler_id: 'handler_id',
      max_amount: {
        currency: {
          address: '0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A',
          chain_id: 1,
          decimals: 0,
        },
        value: '269125115713',
      },
      nonce: '269125115713',
      operator: '0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A',
      payer: '0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A',
      payment_info_hash: '0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8ACa3CC53eb6CEAA2eaa0Aa6be',
      preapproval_expires_at: '2019-12-27T18:11:19.117Z',
      receiver: '0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A',
      refund_expires_at: '2019-12-27T18:11:19.117Z',
      type: 'evm_auth_capture_escrow',
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
    });
  });
});
