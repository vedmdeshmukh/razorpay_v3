from .states import PaymentState

ALLOWED_TRANSITIONS = {
    PaymentState.CREATED: {PaymentState.PROCESSING},
    PaymentState.PROCESSING: {PaymentState.UNKNOWN, PaymentState.SUCCESS, PaymentState.FAILED},
    PaymentState.UNKNOWN: {PaymentState.PENDING, PaymentState.SUCCESS, PaymentState.FAILED},
    PaymentState.PENDING: {PaymentState.PENDING, PaymentState.SUCCESS, PaymentState.FAILED},
    PaymentState.SUCCESS: set(),
    PaymentState.FAILED: set(),
}

def can_transition(current: PaymentState, target: PaymentState) -> bool:
    return target in ALLOWED_TRANSITIONS[current]
