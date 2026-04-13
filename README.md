**LangGraph Workflows Project**

A modular implementation of LangGraph-based AI workflows demonstrating sequential processing, parallel execution, and dynamic routing using Large Language Models (LLMs). This project showcases core workflow orchestration patterns commonly used in modern AI systems.

**Project Overview**

**Implemented Workflows**

**Sequential Workflow**
Generates a joke, checks its quality, and conditionally improves and refines the output.

**Parallel Workflow**
Runs multiple tasks simultaneously (joke, story, poem) and combines the results.

**Router Workflow**
Uses structured LLM output to dynamically decide which task to execute.

**Requirements**
Python 3.10+
LangGraph
LangChain
python-dotenv
uv (recommended)

**Setup**
git clone https://github.com/wajeehaghazi/langgraph-workflows.git
cd langgraph-workflows
uv venv
.venv\Scripts\activate
uv sync
**
Create .env file:**
OPENAI_API_KEY=your_api_key
OPENAI_BASE_URL=https://api.chatanywhere.tech

**Run the Project**
uv run python -m src.main

**Select workflow:**
1 - Sequential
2 - Parallel
3 - Router

