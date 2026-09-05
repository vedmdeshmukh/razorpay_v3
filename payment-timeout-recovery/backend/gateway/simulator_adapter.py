from dataclasses import dataclass

@dataclass
class GatewayResult:
    status: str
    response_received: bool = True
    webhook_delivered: bool = True

class SimulatorGateway:
    def get_status(self, payment_id: str) -> GatewayResult:
        return GatewayResult(status="PENDING")
