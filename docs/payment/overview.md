# Payment (Auth/Capture)

Local Protocol uses UCP payment handlers to support payment between
transacting parties. Any payment handler is supported, but on-chain payment is
highly recommended for neutral, verifiable settlement.

Core objects:

- **Authorization instrument**: The payment instrument submitted at checkout
  that proves funds are authorized into escrow.
- **Capture / refund**: Operator-driven state transitions that release or
  return funds based on the authorization window.

See the Auth/Capture handler definition for fields and examples.
