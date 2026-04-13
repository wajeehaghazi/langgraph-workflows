LangGraph Workflows Project

A modular implementation of LangGraph-based AI workflows demonstrating sequential processing, parallel execution, and dynamic routing using Large Language Models (LLMs). This project showcases core workflow orchestration patterns commonly used in modern AI systems.

Project Overview

This project implements three fundamental workflow patterns using LangGraph and LangChain:

Sequential Workflow — Conditional processing pipeline with decision logic
Parallel Workflow — Concurrent execution with aggregation
Router Workflow — Dynamic LLM-based routing using structured output

These workflows demonstrate real-world orchestration techniques used in AI pipelines, multi-agent systems, and intelligent automation.

Project Structure
langgraph_project
│
├── src
│   ├── main.py
│   └── model.py
│
├── workflows
│   ├── sequential_workflow.py
│   ├── parallel_workflow.py
│   └── router_workflow.py
│
├── config
│   └── settings.py
│
├── pyproject.toml
├── uv.lock
├── .gitignore
└── README.md

Technologies Used
Python 3.13
LangGraph
LangChain
OpenAI-compatible API
uv (Python package manager)
Pydantic
dotenv
Installation

Clone the repository:

git clone https://github.com/wajeehaghazi/langgraph-workflows.git
cd langgraph-workflows

Create virtual environment using uv:

uv venv

Activate environment:

.venv\Scripts\activate

Install dependencies:

uv sync
Environment Variables

Create a .env file in the project root:

OPENAI_API_KEY=your_api_key_here
OPENAI_BASE_URL=https://api.chatanywhere.tech

Important:

Do not commit .env
Keep API keys secure
Running the Project

Execute the main controller:

uv run python -m src.main

You will be prompted to select a workflow:

1 - Sequential Workflow
2 - Parallel Workflow
3 - Router Workflow
Example Use Cases

This project demonstrates workflow orchestration patterns applicable to:

AI automation pipelines
Multi-agent systems
Task orchestration engines
Decision-based workflows
Conversational AI systems
LLM routing systems
Data processing pipelines
Key Concepts Demonstrated
Workflow orchestration
Conditional routing
Parallel execution
Aggregation patterns
Structured output validation
State management
Modular architecture
