# Payment (Escrow)

Local Protocol uses UCP payment handlers to support business-to-business
settlement. Payments use a neutral smart-contract escrow on EVM chains with
programmatic dual-signature release: the payer attests "approve" or "dispute"
and the payee attests "request" or "release." A guarantor provides 100%
coverage and is only economically exposed on dispute.

This capability does not dictate the token. Each business advertises the tokens
and chain ids it accepts in its handler configuration.

Core objects:

- **Escrow instrument**: The payment instrument submitted at checkout that
  proves funds are locked in escrow.
- **Release attestation**: A signed message from each party that triggers
  escrow release when both are present.

See the Escrow handler definition for fields and examples.
