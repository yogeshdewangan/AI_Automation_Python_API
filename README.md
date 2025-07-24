# AI_Automation_Python_API
Modular automation framework in Python + Pytest enhanced with AI agents

Here's a modular automation framework in Python + Pytest enhanced with AI agents, where:

🧠 Agent Roles:
TestGenAgent: Uses AI (like OpenAI or CrewAI) to generate test cases for API endpoints dynamically.

TestExecAgent: Executes the generated tests via Pytest programmatically.

LogAnalysisAgent: Analyzes Pytest logs using an LLM (LangChain or CrewAI) and generates summaries or root causes.

✅ Tech Stack
Python + Pytest

Requests (for API testing)

LangChain / CrewAI (for AI agents)

OpenAI or Azure OpenAI (as LLM backend)

Chroma/FAISS (optional for log vector search)

dotenv for managing secrets


Project Structure

ai_api_framework/
├── agents/
│   ├── test_gen_agent.py       # AI agent to generate test cases
│   ├── test_exec_agent.py      # Executes generated tests
│   └── log_analysis_agent.py   # Analyzes pytest logs using LLM
│
├── tests/
│   └── generated_test_users.py # Output test file (AI-generated)
│
├── logs/
│   └── test_failures.log
│
├── utils/
│   └── helpers.py
│
├── main.py                     # Orchestrator
├── .env
└── requirements.txt

Execute: python main.py
