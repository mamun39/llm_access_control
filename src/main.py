# src/main.py

from llm_access_control import AccessManager, AdminPolicy, UserPolicy, LLMIntegration

def main():
    policies = [AdminPolicy(), UserPolicy()]
    llm_integration = LLMIntegration()
    access_manager = AccessManager(policies, llm_integration)

    user = 'admin'
    resource = 'sensitive_data'
    if access_manager.check_access(user, resource):
        print(f"Access granted for user {user} to resource {resource}")
    else:
        print(f"Access denied for user {user} to resource {resource}")

if __name__ == "__main__":
    main()