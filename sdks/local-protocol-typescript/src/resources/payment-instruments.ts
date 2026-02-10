// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../core/resource';
import * as PaymentInstrumentsAPI from './payment-instruments';
import * as RequestsAPI from './requests/requests';
import { APIPromise } from '../core/api-promise';
import { RequestOptions } from '../internal/request-options';

export class PaymentInstruments extends APIResource {
  /**
   * Register a payment instrument for use in order creation.
   */
  register(
    body: PaymentInstrumentRegisterParams,
    options?: RequestOptions,
  ): APIPromise<EvmAuthCaptureEscrowInstrument> {
    return this._client.post('/payment-instruments', { body, ...options });
  }
}

/**
 * Amount with explicit currency. Value is always in minor units (e.g., cents for
 * USD).
 */
export interface Amount {
  /**
   * Currency descriptor (fiat or EVM token).
   */
  currency: Amount.FiatCurrency | EvmCurrency;

  /**
   * Value in minor currency units as an integer string.
   */
  value: string;
}

export namespace Amount {
  /**
   * Fiat currency descriptor.
   */
  export interface FiatCurrency {
    /**
     * ISO 4217 currency code (e.g., 'USD', 'EUR', 'JPY').
     */
    symbol: string;
  }
}

/**
 * Payment instrument for auth/capture escrow on EVM chains.
 */
export interface EvmAuthCaptureEscrowInstrument extends PaymentInstrument {
  /**
   * EVM token identifier used for auth/capture settlement.
   */
  token: EvmAuthCaptureEscrowInstrument.Token;

  /**
   * Amount in atomic units. Currency chain_id MUST match the instrument chain_id;
   * currency address and decimals MUST match token address and decimals.
   */
  amount: EvmAuthCaptureEscrowInstrument.Amount;

  /**
   * Authorization expiration (RFC 3339).
   */
  authorization_expires_at: string;

  /**
   * EVM chain id.
   */
  chain_id: number;

  /**
   * Escrow contract address.
   */
  contract: string;

  /**
   * Maximum amount that can be authorized (atomic units). Currency chain_id MUST
   * match the instrument chain_id; currency address and decimals MUST match token
   * address and decimals.
   */
  max_amount: EvmAuthCaptureEscrowInstrument.MaxAmount;

  /**
   * Unique nonce for payment info hash computation.
   */
  nonce: string;

  /**
   * Operator address.
   */
  operator: string;

  /**
   * Payer address.
   */
  payer: string;

  /**
   * Hash identifying the on-chain payment authorization.
   */
  payment_info_hash: string;

  /**
   * Pre-approval expiration (RFC 3339).
   */
  preapproval_expires_at: string;

  /**
   * Receiver address for captures.
   */
  receiver: string;

  /**
   * Refund expiration (RFC 3339).
   */
  refund_expires_at: string;

  type: 'evm_auth_capture_escrow';
}

export namespace EvmAuthCaptureEscrowInstrument {
  /**
   * EVM token identifier used for auth/capture settlement.
   */
  export interface Token {
    /**
     * Token decimals.
     */
    decimals: number;

    /**
     * Token symbol (e.g., USDC).
     */
    symbol: string;

    /**
     * ERC-20 contract address. Omit for native gas tokens.
     */
    address?: string;
  }

  /**
   * Amount in atomic units. Currency chain_id MUST match the instrument chain_id;
   * currency address and decimals MUST match token address and decimals.
   */
  export interface Amount extends Omit<PaymentInstrumentsAPI.Amount, 'currency'> {
    /**
     * EVM token currency descriptor.
     */
    currency?: PaymentInstrumentsAPI.EvmCurrency;
  }

  /**
   * Maximum amount that can be authorized (atomic units). Currency chain_id MUST
   * match the instrument chain_id; currency address and decimals MUST match token
   * address and decimals.
   */
  export interface MaxAmount extends Omit<PaymentInstrumentsAPI.Amount, 'currency'> {
    /**
     * EVM token currency descriptor.
     */
    currency?: PaymentInstrumentsAPI.EvmCurrency;
  }
}

/**
 * EVM token currency descriptor.
 */
export interface EvmCurrency {
  /**
   * Token contract address.
   */
  address: string;

  /**
   * EVM chain id.
   */
  chain_id: number;

  /**
   * Decimal places for the token.
   */
  decimals: number;
}

/**
 * Base definition for any payment instrument.
 */
export interface PaymentInstrument {
  /**
   * Unique instrument identifier.
   */
  id: string;

  /**
   * Handler instance identifier.
   */
  handler_id: string;

  /**
   * Instrument category (e.g., 'card', 'tokenized_card').
   */
  type: string;

  /**
   * Billing address.
   */
  billing_address?: RequestsAPI.PostalAddress;

  /**
   * Base definition for any payment credential.
   */
  credential?: PaymentInstrument.Credential;

  /**
   * Display information for the instrument.
   */
  display?: unknown;
}

export namespace PaymentInstrument {
  /**
   * Base definition for any payment credential.
   */
  export interface Credential {
    /**
     * Credential type discriminator.
     */
    type: string;

    [k: string]: unknown;
  }
}

export interface PaymentInstrumentRegisterParams {
  /**
   * Unique instrument identifier.
   */
  id: string;

  /**
   * EVM token identifier used for auth/capture settlement.
   */
  token: PaymentInstrumentRegisterParams.Token;

  /**
   * Amount in atomic units. Currency chain_id MUST match the instrument chain_id;
   * currency address and decimals MUST match token address and decimals.
   */
  amount: PaymentInstrumentRegisterParams.Amount;

  /**
   * Authorization expiration (RFC 3339).
   */
  authorization_expires_at: string;

  /**
   * EVM chain id.
   */
  chain_id: number;

  /**
   * Escrow contract address.
   */
  contract: string;

  /**
   * Handler instance identifier.
   */
  handler_id: string;

  /**
   * Maximum amount that can be authorized (atomic units). Currency chain_id MUST
   * match the instrument chain_id; currency address and decimals MUST match token
   * address and decimals.
   */
  max_amount: PaymentInstrumentRegisterParams.MaxAmount;

  /**
   * Unique nonce for payment info hash computation.
   */
  nonce: string;

  /**
   * Operator address.
   */
  operator: string;

  /**
   * Payer address.
   */
  payer: string;

  /**
   * Hash identifying the on-chain payment authorization.
   */
  payment_info_hash: string;

  /**
   * Pre-approval expiration (RFC 3339).
   */
  preapproval_expires_at: string;

  /**
   * Receiver address for captures.
   */
  receiver: string;

  /**
   * Refund expiration (RFC 3339).
   */
  refund_expires_at: string;

  type: 'evm_auth_capture_escrow';

  /**
   * Billing address.
   */
  billing_address?: RequestsAPI.PostalAddress;

  /**
   * Base definition for any payment credential.
   */
  credential?: PaymentInstrumentRegisterParams.Credential;

  /**
   * Display information for the instrument.
   */
  display?: unknown;
}

export namespace PaymentInstrumentRegisterParams {
  /**
   * EVM token identifier used for auth/capture settlement.
   */
  export interface Token {
    /**
     * Token decimals.
     */
    decimals: number;

    /**
     * Token symbol (e.g., USDC).
     */
    symbol: string;

    /**
     * ERC-20 contract address. Omit for native gas tokens.
     */
    address?: string;
  }

  /**
   * Amount in atomic units. Currency chain_id MUST match the instrument chain_id;
   * currency address and decimals MUST match token address and decimals.
   */
  export interface Amount extends Omit<PaymentInstrumentsAPI.Amount, 'currency'> {
    /**
     * EVM token currency descriptor.
     */
    currency?: PaymentInstrumentsAPI.EvmCurrency;
  }

  /**
   * Maximum amount that can be authorized (atomic units). Currency chain_id MUST
   * match the instrument chain_id; currency address and decimals MUST match token
   * address and decimals.
   */
  export interface MaxAmount extends Omit<PaymentInstrumentsAPI.Amount, 'currency'> {
    /**
     * EVM token currency descriptor.
     */
    currency?: PaymentInstrumentsAPI.EvmCurrency;
  }

  /**
   * Base definition for any payment credential.
   */
  export interface Credential {
    /**
     * Credential type discriminator.
     */
    type: string;

    [k: string]: unknown;
  }
}

export declare namespace PaymentInstruments {
  export {
    type Amount as Amount,
    type EvmAuthCaptureEscrowInstrument as EvmAuthCaptureEscrowInstrument,
    type EvmCurrency as EvmCurrency,
    type PaymentInstrument as PaymentInstrument,
    type PaymentInstrumentRegisterParams as PaymentInstrumentRegisterParams,
  };
}
