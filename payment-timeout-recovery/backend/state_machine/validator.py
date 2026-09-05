from .states import PaymentState
from .transitions import can_transition

class InvalidTransition(ValueError):
    pass

def validate_transition(current: PaymentState, target: PaymentState) -> None:
    if not can_transition(current, target):
        raise InvalidTransition(f"Invalid transition: {current.value} -> {target.value}")
