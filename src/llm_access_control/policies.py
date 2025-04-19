# src/llm_access_control/policies.py

class Policy:
    def applies_to(self, user: str, resource: str) -> bool:
        raise NotImplementedError

class AdminPolicy(Policy):
    def applies_to(self, user: str, resource: str) -> bool:
        return user == 'admin'

class UserPolicy(Policy):
    def applies_to(self, user: str, resource: str) -> bool:
        return user != 'admin'