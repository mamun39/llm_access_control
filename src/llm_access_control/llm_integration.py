# src/llm_access_control/llm_integration.py

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

class LLMIntegration:
    def __init__(self, model: str = "gpt-3.5-turbo"):
        # Load environment variables from .env file
        load_dotenv()
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("API key not found. Please set an 'OPENAI_API_KEY' in your .env file.")
        
        # Initialize the OpenAI chat model
        self.llm = ChatOpenAI(
            model_name=model,
            api_key=api_key,
            temperature=0  # Use temperature=0 for more deterministic responses
        )

    def get_access_decision(self, user: str, resource: str) -> bool:
        prompt = self.create_prompt(user, resource)
        message = HumanMessage(content=prompt)
        response = self.llm.invoke([message])
        
        # Extract the response content
        response_text = response.content
        print(f"Received response: {response_text}")
        
        return self.parse_response(response_text)

    def create_prompt(self, user: str, resource: str) -> str:
        # Craft a prompt for the LLM based on input parameters
        return f"Determine if user '{user}' should have access to '{resource}'. Respond with only 'yes' or 'no'."

    def parse_response(self, response: str) -> bool:
        # Parse the response for a yes/no decision
        response = response.strip().lower()
        if 'yes' in response:
            return True
        return False