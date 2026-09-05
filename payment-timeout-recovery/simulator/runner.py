from dataclasses import dataclass

@dataclass
class Scenario:
    name: str
    api_status: str | None
    webhook: bool

def run_scenario(scenario: Scenario) -> Scenario:
    return scenario

if __name__ == "__main__":
    print(run_scenario(Scenario("api_timeout", None, False)))
