# LangGraph AI Agentic Systems

This repository demonstrates the use of [LangGraph](https://github.com/langchain-ai/langgraph) to build modular, graph-based AI agent systems in Python. It includes agent implementations, utilities, tutorials, and exercises for learning and extending agentic workflows.

---

## Table of Contents

- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Agents Overview](#agents-overview)
  - [1. Simple Bot](#1-simple-bot)
  - [2. Chatbot with Memory](#2-chatbot-with-memory)
  - [3. React Agent](#3-react-agent)
  - [4. Drafter Agent](#4-drafter-agent)
  - [5. RAG Agent](#5-rag-agent)
- [Utilities](#utilities)
- [Tutorials](#tutorials)
- [Exercises](#exercises)
- [How to Run](#how-to-run)
- [License](#license)

---

## Project Structure

```
langgraph/
│
├── agents/
│   ├── 1_simple_bot.ipynb         # Basic conversational agent (notebook)
│   ├── 2_chatbot_with_memory.py   # Chatbot with memory (Python script)
│   ├── 3_react_agent.py           # React agent with tool use
│   ├── 4_drafter_agent.py         # Human-in-the-loop document drafter
│   ├── 5_rag_agent.py             # Retrieval-Augmented Generation agent
│   ├── utils/
│   │   ├── __init__.py
│   │   └── settings.py            # Centralized settings/configuration
│   ├── chroma.sqlite3             # Chroma vector DB for RAG agent
│   └── market-infographic-recap-2024.pdf # Example PDF for RAG agent
│
├── tutorials/                     # Step-by-step LangGraph tutorials
│   ├── 1_ hello_world.ipynb
│   ├── 2_multiple_inputs.ipynb
│   ├── 3_sequential_graph.ipynb
│   ├── 4_conditional_graph.ipynb
│   └── 5_looping_graph.ipynb
│
├── exercises/                     # Practice exercises for LangGraph
│   ├── exercise_graph1.ipynb
│   ├── exercise_graph2.ipynb
│   ├── exercise_graph3.ipynb
│   ├── exercise_graph4.ipynb
│   └── exercise_graph5.ipynb
│
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation
```

---

## Installation

1. **Clone the repository:**
   ```powershell
   git clone https://github.com/ankitprasad81/langgraph.git
   cd langgraph
   ```

2. **Create and activate a virtual environment:**
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate
   ```

3. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

---

## Configuration

- Copy `.env.example` to `.env` and fill in your API keys (e.g., for Groq, HuggingFace, etc.).
- The main configuration is in `agents/utils/settings.py` and uses [pydantic-settings](https://pydantic-docs.helpmanual.io/usage/settings/).

Example `.env`:
```
GROQ_API_KEY=your_groq_api_key
```

---

## Agents Overview

### 1. Simple Bot (`agents/1_simple_bot.ipynb`)
- A basic conversational agent using LangGraph and ChatGroq.
- Demonstrates message handling and graph compilation.

### 2. Chatbot with Memory (`agents/2_chatbot_with_memory.py`)
- Maintains full conversation history using both `HumanMessage` and `AIMessage`.
- Saves conversation logs to `logging.txt`.
- Run with:
  ```powershell
  python agents\2_chatbot_with_memory.py
  ```

### 3. React Agent (`agents/3_react_agent.py`)
- Demonstrates tool use (add, subtract, multiply) within a graph.
- Uses conditional edges to decide when to call tools or finish.
- Run with:
  ```powershell
  python agents\3_react_agent.py
  ```

### 4. Drafter Agent (`agents/4_drafter_agent.py`)
- Human-in-the-loop document drafting agent.
- Supports updating and saving documents via tool calls.
- Run with:
  ```powershell
  python agents\4_drafter_agent.py
  ```

### 5. RAG Agent (`agents/5_rag_agent.py`)
- Retrieval-Augmented Generation agent.
- Loads a PDF, chunks it, creates a Chroma vector store, and answers questions using retrieval.
- Requires `market-infographic-recap-2024.pdf` in the `agents/` directory.
- Run with:
  ```powershell
  python agents\5_rag_agent.py
  ```

---

## Utilities

- `agents/utils/settings.py`: Centralized settings using Pydantic. Reads from `.env`.
- `agents/chroma.sqlite3`: Vector database for document retrieval (used by RAG agent).

---

## Tutorials

The `tutorials/` folder contains step-by-step Jupyter notebooks covering:

1. **Hello World**: Basic graph and node setup.
2. **Multiple Inputs**: Handling multiple state fields.
3. **Sequential Graph**: Chaining nodes in sequence.
4. **Conditional Graph**: Routing based on state.
5. **Looping Graph**: Implementing loops in the graph.

Open and run these notebooks in Jupyter or VS Code to learn LangGraph concepts.

---

## Exercises

The `exercises/` folder provides hands-on practice with:

- State management
- Node creation
- Conditional logic
- Looping
- Multi-step workflows

Each exercise is a Jupyter notebook with a task description and starter code.

---

## How to Run

- For Python scripts:  
  ```powershell
  python agents\<script_name>.py
  ```
- For Jupyter notebooks:  
  Open in VS Code or JupyterLab and run cells interactively.

---

## License

This project is for educational and research purposes.

---

**Note:**  
- Make sure you have the required API keys and dependencies.
- For Windows, all commands are provided in PowerShell syntax.
