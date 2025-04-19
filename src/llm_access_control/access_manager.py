# src/llm_access_control/access_manager.py

from .policies import Policy
from .llm_integration import LLMIntegration

class AccessManager:
    def __init__(self, policies: list[Policy], llm_integration: LLMIntegration):
        self.policies = policies
        self.llm_integration = llm_integration

    def check_access(self, user: str, resource: str) -> bool:
        for policy in self.policies:
            if policy.applies_to(user, resource):
                decision = self.llm_integration.get_access_decision(user, resource)
                if decision:
                    return True
        return False