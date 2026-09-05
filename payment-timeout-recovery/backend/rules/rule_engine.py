from backend.state_machine.states import PaymentState

def decide_action(*, state: PaymentState, authoritative_status: str | None, webhook_verified: bool) -> str:
    if authoritative_status == "SUCCESS":
        return "FINALIZE_SUCCESS"
    if authoritative_status == "FAILED":
        return "FINALIZE_FAILED"
    if webhook_verified and state in {PaymentState.UNKNOWN, PaymentState.PENDING}:
        return "PROCESS_VERIFIED_EVENT"
    if state == PaymentState.UNKNOWN:
        return "WAIT_AND_VERIFY"
    return "NO_ACTION"
