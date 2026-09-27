# ADK Ollama Time Agent

A lightweight custom AI agent built using the **Google Agent Development Kit (ADK)**, **LiteLLM**, and **Ollama** (`llama3.2`) that acts as a precise time assistant capable of looking up local times across global timezones.

---

## Project Structure

```text
adk_ollama/
│
├── my_agent/
│   └── agent.py       # Main agent logic, tools, and LiteLLM model registration
├── .env               # Environment variables (not tracked in git)
├── .gitignore         # Files to ignore
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
```

---

## Prerequisites

1. Python 3.10+ installed on your system.
2. Ollama installed and running locally.
3. Pull the required model via Ollama:

```bash
ollama pull llama3.2
```

---

## Installation & Setup

1. Clone the repository:

```bash
git clone https://github.com/floraszugyiczki/adk-ollama-time-agent.git
cd adk-ollama-time-agent
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Agent

Run your agent script:

```bash
python my_agent/agent.py
```