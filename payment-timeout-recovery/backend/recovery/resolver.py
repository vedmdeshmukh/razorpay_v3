from backend.rules.rule_engine import decide_action
from backend.state_machine.states import PaymentState

def resolve_timeout(*, authoritative_status: str | None = None, webhook_verified: bool = False) -> dict[str, str]:
    return {
        "state": PaymentState.UNKNOWN.value,
        "action": decide_action(
            state=PaymentState.UNKNOWN,
            authoritative_status=authoritative_status,
            webhook_verified=webhook_verified,
        ),
    }
