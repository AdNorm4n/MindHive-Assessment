# 🧠 MindHive AI Chatbot Assessment (FastAPI + LangChain)

**Prepared by:** Adrian Norman Bin Khusairi

This repository is a submission for MindHive’s AI Chatbot Engineer technical assessment. It showcases a robust, multi-turn conversational AI agent built using FastAPI and LangChain. The chatbot supports memory tracking, agentic planning, external tool use (calculator and APIs), and handles edge cases gracefully.

---

## 🔗 Live Demo

- 🌐 App: [https://mindhive-assessment-t3fy.onrender.com]
- 📘 Swagger Docs: [https://mindhive-assessment-t3fy.onrender.com/docs]

---

## ✅ Features Implemented

### 🧩 1. Sequential Conversation (Memory & State Tracking)

- Maintains conversational memory across multiple user turns.
- Follows up to request missing slot information like product names or outlet locations.
- Uses `ConversationBufferMemory` from LangChain.

### 🤖 2. Agentic Planning

- Detects user intent (`calculator`, `outlet_info`, `product_info`).
- Determines appropriate next action:
  - Ask follow-up question.
  - Call a tool or external API.
  - Return an answer.

### 🧮 3. Tool Calling

- Supports basic arithmetic operations.
- Uses a secure regex-based parser.
- Handles invalid or unsafe expressions without crashing.

### 🌐 4. Custom API Integration (FastAPI)

- `/chat`: Main conversation endpoint.
- `/products`: Loads product info from CSV (acts like a simplified RAG).
- `/outlets`: Returns store hours by location from a CSV source.

### 🛡️ 5. Robustness & Unhappy Flows

- Handles:
  - Missing parameters (e.g., “calculate” with no numbers).
  - Invalid/malicious input (e.g., SQL-like injection in `/outlets`).
  - Simulated tool/API failure gracefully.
- Always responds with a fallback or follow-up prompt.

---

## ⚙️ Tech Stack

- **Python 3.11**
- **FastAPI** – Backend web framework
- **LangChain** – LLM integration, memory, and planning
- **OpenAI GPT-3.5** – Natural language understanding and generation
- **Pandas** – CSV parsing for domain knowledge
- **Uvicorn** – ASGI server for FastAPI
- **dotenv** – Secure environment variable management

---

## 📦 How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/AdNorm4n/MindHive-Assessment
cd "MindHive Assessment"
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# OR
source venv/bin/activate  # On macOS/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set OpenAI API key

Create a `.env` file in the root directory:

```ini
OPENAI_API_KEY=your_openai_key_here
```

### 5. Start the server

```bash
uvicorn app.main:app --reload
```

Visit: [http://127.0.0.1:8000/docs]

---

## 🧠 Architecture Overview

```
 MindHive Assessment/
 ┣ app/
 ┃ ┣ main.py            → FastAPI entrypoint with /chat
 ┃ ┣ planner.py         → Intent classification and slot extraction
 ┃ ┣ tools/
 ┃ ┃ ┣ calculator.py    → Safe arithmetic evaluator
 ┃ ┃ ┗ zus_tools.py     → Custom functions for outlet/product info
 ┣ data/
 ┃ ┣ products.csv       → Simulated product KB (drinkware-style)
 ┃ ┗ outlets.csv        → List of ZUS outlet names and opening hours
 ┣ requirements.txt     → Dependencies
 ┗ .env                 → Contains OpenAI API key
```

---
