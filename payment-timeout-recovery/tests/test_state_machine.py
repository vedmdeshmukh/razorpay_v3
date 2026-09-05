from backend.state_machine.states import PaymentState
from backend.state_machine.validator import InvalidTransition, validate_transition

def test_created_to_processing_is_valid():
    validate_transition(PaymentState.CREATED, PaymentState.PROCESSING)

def test_success_to_failed_is_invalid():
    try:
        validate_transition(PaymentState.SUCCESS, PaymentState.FAILED)
    except InvalidTransition:
        return
    raise AssertionError("Expected InvalidTransition")
