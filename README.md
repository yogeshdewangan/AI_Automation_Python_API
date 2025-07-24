# 🤖 AI_Automation_Python_API

A **modular automation framework** built with **Python + Pytest**, enhanced with **AI agents** for intelligent, autonomous API testing.

---

## 🎯 Overview

This framework integrates AI agents using **LangChain** or **CrewAI** to automate the full API testing lifecycle:

### 🧠 AI Agent Roles

- **TestGenAgent**  
  ➤ Uses LLMs (e.g., OpenAI or CrewAI) to dynamically generate `pytest` test cases from API descriptions or documentation.

- **TestExecAgent**  
  ➤ Executes the generated test cases programmatically using `pytest` and saves logs.

- **LogAnalysisAgent**  
  ➤ Analyzes test failure logs using LLMs to provide summarized root cause analysis and intelligent debugging suggestions.

---

## 🧰 Tech Stack

| Component         | Purpose                              |
|------------------|--------------------------------------|
| Python + Pytest  | Core test automation framework       |
| Requests         | REST API testing                     |
| LangChain / CrewAI | AI agent orchestration              |
| OpenAI / Azure OpenAI | LLM backend for code and reasoning |
| FAISS / Chroma   | (Optional) Log embedding & RAG       |
| python-dotenv    | Secrets management                   |

---

## 🗂️ Project Structure

