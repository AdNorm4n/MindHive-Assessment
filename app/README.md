# 🧠 MindHive AI Chatbot Assessment (FastAPI + LangChain)

**Prepared by:** Adrian Norman Bin Khusairi

This repository is a submission for MindHive’s AI Chatbot Engineer technical assessment. It showcases an intelligent, multi-turn chatbot agent built using FastAPI and LangChain, capable of memory tracking, intent recognition, external tool usage, and robust natural language understanding.

---

## 🔗 Live Demo

- 🌐 App: [https://mindhive-assessment-t3fy.onrender.com](https://mindhive-assessment-t3fy.onrender.com)
- 📘 API Docs (Swagger): [https://mindhive-assessment-t3fy.onrender.com/docs](https://mindhive-assessment-t3fy.onrender.com/docs)

---

## ✅ Features Implemented

### 🧩 1. Sequential Conversation (Memory & State Tracking)

- Tracks user input across multiple turns
- Maintains conversation context using `ConversationBufferMemory`
- Follows up to request missing information (e.g., outlet or product)

### 🤖 2. Agentic Planning

- Detects user intent: `calculator`, `outlet_info`, `product_info`
- Determines the next step:
  - Ask a follow-up question
  - Call an external tool
  - Return a final response

### 🧮 3. Tool Calling

- Implements a secure arithmetic calculator tool
- Detects math expressions and evaluates safely
- Handles invalid or malformed expressions gracefully

### 🌐 4. Custom API Integration (FastAPI)

- `/chat`: Central entry point for conversation handling
- `/products`: Reads product data from CSV (acts like a RAG pipeline)
- `/outlets`: Returns outlet hours based on user location query

### 🛡️ 5. Unhappy Flow Handling

- Responds meaningfully to:
  - Missing parameters (e.g. no expression, no outlet)
  - Invalid inputs (e.g. "calculate two apples")
  - Malicious payloads (e.g. SQL injections in `/outlets`)
  - Simulated tool/API errors

---

## ⚙️ Tech Stack

- **Python 3.11**
- **FastAPI** – RESTful web framework
- **LangChain** – For memory and LLM-based logic
- **OpenAI GPT-3.5** – LLM used for reasoning
- **Pandas** – CSV data handling
- **Uvicorn** – ASGI server
- **dotenv** – Environment configuration

---

## 📦 How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/AdNorm4n/MindHive-Assessment
cd "MindHive Assessment"
```
