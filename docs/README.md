# LLM Access Control

## Overview
This project implements an LLM-based solution for access control. It uses language models through the LangChain framework to make intelligent access control decisions based on predefined policies.

> **Note:** This is a proof-of-concept implementation. While LLMs have potential in enhancing access control processes, the current state of the technology makes them more suited for supplementary roles rather than as primary decision-makers. Security, compliance, and consistency are paramount in access control, and relying solely on probabilistic models introduces significant risks. A careful, hybrid approach that combines traditional mechanisms with LLM capabilities might be more practical.

## Features
- Policy-based access control system
- LLM integration for intelligent decision making
- Extensible policy framework
- Environment-based configuration management
- Simple web UI using Streamlit

## Prerequisites
- Python 3.10 or higher
- Poetry package manager
- OpenAI API key (or other LLM provider key compatible with LangChain)

## Installation

### 1. Clone the repository
```sh
git clone https://github.com/yourusername/llm-access-control.git
cd llm-access-control
```

### 2. Install dependencies with Poetry
```sh
poetry install
```

### 3. Set up environment variables
Create a `.env` file in the project root directory with your API keys:
```
OPENAI_API_KEY=your-api-key-here
```

## Usage

### Running the command-line application
```sh
poetry run python src/main.py
```

### Launching the web interface
```sh
poetry run streamlit run src/app.py
```

The web interface provides a user-friendly way to interact with the access control system, allowing you to input user identifiers and resources to check access permissions.

### Creating custom policies
You can extend the `Policy` base class to create custom access policies:

```python
from llm_access_control import Policy

class CustomPolicy(Policy):
    def applies_to(self, user: str, resource: str) -> bool:
        # Your custom logic here
        return True  # or False
```

## Development

### Running tests
```sh
poetry run pytest
```

### Project structure
- `src/llm_access_control/`: Core package
  - `access_manager.py`: Main access control logic
  - `policies.py`: Policy definitions and implementations
  - `llm_integration.py`: LLM integration using LangChain
- `src/app.py`: Streamlit web interface
- `src/main.py`: Command-line interface

## Limitations and Considerations

When using this system, consider the following:

- LLMs may produce inconsistent results for similar inputs
- Model responses can be influenced by prompt phrasing
- There's limited explainability for decision-making
- Authorization decisions may change as models are updated
- Consider implementing additional guardrails for production use

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.