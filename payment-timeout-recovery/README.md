# Payment Timeout Recovery

An intelligent payment-timeout resolution and reconciliation layer for merchants integrating with payment gateways.

## Core principle

Deterministic rules and authoritative gateway evidence determine financial state. ML may recommend recovery actions, but it cannot directly establish payment truth or override safety controls.

## MVP sequence

1. Payment state machine
2. Gateway simulator and failure scenarios
3. Rule-only recovery
4. Evidence validation and reconciliation
5. Bounded ML advisor
6. Rule-only vs rule+ML evaluation
