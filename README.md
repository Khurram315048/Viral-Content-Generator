# 🚀 TrendPilot: Agentic AI for Instagram Reels

TrendPilot is a production-grade Agentic AI application built for the PITB AI Internship Task 2. It automates the creation of viral Instagram Reels by orchestrating multiple modular AI tools using LangGraph, powered locally by Ollama (`gemma3:4b`), styled with an interactive Streamlit UI, and backed by a local SQLite memory system.

---

## 🛠️ Tech Stack
* **Orchestration:** LangGraph (State Machine & Tool Routing)
* **LLM Engine:** Local Ollama running `gemma3:4b` (3.3 GB model)
* **Frontend UI:** Streamlit
* **Database & Memory:** SQLite (`outputs/agent_memory.db`)
* **Language:** Python 3.10+

---

## 📁 Project Directory Structure
```text
Viral_Content_Generator/
│
├── app/
│   ├── __init__.py
│   ├── agent.py          # LangGraph state machine & agent workflow
│   ├── main.py           # Streamlit user interface & sidebar memory viewer
│   ├── memory.py         # SQLite database initialization & interactions
│   ├── prompts.py        # Structured templates for trends, scripts, & reviews
│   └── tools.py          # Modular tools for AI calls & file saving
│
├── outputs/
│   ├── agent_memory.db   # SQLite database storing full content history
│   └── generated_scripts/# Saved markdown output files (.md)
│
├── screenshots/          # Application and terminal execution proofs
├── report/
│   └── final_report.pdf  # Comprehensive project and error analysis report
├── tests/
│   └── test_cases.md     # Multi-level test cases documentation
├── requirements.txt      # Project dependencies
└── README.md