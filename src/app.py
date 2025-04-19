import streamlit as st
from llm_access_control import AccessManager, AdminPolicy, UserPolicy, LLMIntegration

# Initialize components
llm_integration = LLMIntegration()
policies = [AdminPolicy(), UserPolicy()]
access_manager = AccessManager(policies, llm_integration)

# Streamlit UI
st.title("LLM Access Control System")

# User input
user = st.text_input("User ID:", "admin")
resource = st.text_input("Resource:", "sensitive_data")

# Check access when button is clicked
if st.button("Check Access"):
    with st.spinner("Checking access..."):
        has_access = access_manager.check_access(user, resource)
    
    if has_access:
        st.success(f"✅ Access granted for user '{user}' to resource '{resource}'")
    else:
        st.error(f"❌ Access denied for user '{user}' to resource '{resource}'")

# Optional: Add explanation or documentation
with st.expander("How it works"):
    st.write("""
    This system uses LLM-based access control to determine if a user should have 
    access to a specific resource. The decision is made based on predefined policies
    and the judgment of a language model.
    """)