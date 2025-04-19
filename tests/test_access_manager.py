# tests/test_access_manager.py

import pytest
from src.llm_access_control import AccessManager, AdminPolicy, UserPolicy, LLMIntegration

@pytest.fixture
def access_manager():
    policies = [AdminPolicy(), UserPolicy()]
    llm_integration = LLMIntegration()
    return AccessManager(policies, llm_integration)

def test_admin_access_granted(access_manager):
    assert access_manager.check_access('admin', 'sensitive_data')

def test_user_access_denied(access_manager):
    assert not access_manager.check_access('user', 'sensitive_data')