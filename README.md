# Market Trend Analyzer – Multi-Agent AI Powerhouse

An intelligent, fully local market research and trend reporting workflow powered by **CrewAI agents** and **Ollama**.  
No API keys or cloud required — research, analyze, and summarize market trends **directly on your machine**.

---

## 📋 Table of Contents
- 🎯 [Project Overview](#-project-overview)
- 🏗️ [System Architecture](#-system-architecture)
- 🚀 [Key Features](#-key-features)
- 🛠️ [Technology Stack](#-technology-stack)
- 📁 [Project Structure](#-project-structure)
- ⚙️ [Installation & Setup](#-installation--setup)
- 🎮 [Usage Guide](#-usage-guide)
- 💡 [Example Outputs](#-example-outputs)
- 🔧 [Troubleshooting & FAQ](#-troubleshooting--faq)
- ☁️ [Deployment](#-deployment)

---

## 🎯 Project Overview

**Market Trend Analyzer** automates deep-dive market research through a powerful **three-phase AI workflow**:

1. **Researcher Agent** – Finds real, up-to-date data and news from the web.  
2. **Analyst Agent** – Identifies and explains major trends and their impacts.  
3. **Writer Agent** – Produces concise, executive-level markdown reports.

All processing is done locally using **Llama 3 via Ollama**, ensuring **full privacy and offline operation**.

---

## 🏗️ System Architecture

```
[Topic Input]
    │
    └─▶ [Researcher Agent: Web Search & Scraper]
              │
              ▼
[Analyst Agent: Insight Extraction & Trend Mapping]
              │
              ▼
  [Writer Agent: Executive Markdown Report]
              │
              ▼
[Output: research_findings.md, final_report.md]
```

---

## 🚀 Key Features

- 🔎 **Automated market research** with real-time web search and scraping.  
- 🧠 **Expert-level trend analysis** from multiple, current data sources.  
- 📝 **Clean markdown report generation** ready for publishing or sharing.  
- 🔒 **Local-only execution** — zero cloud dependency or data exposure.  
- ⚡️ **No API keys or subscription costs** required.  

---

## 🛠️ Technology Stack

| Layer          | Technology |
|----------------|-------------|
| **Backend**    | Python 3.10+, CrewAI |
| **LLM**        | Ollama (Llama 3 / 8B model) |
| **Web Search** | DuckDuckGoSearchRun |
| **Web Scraping** | ScrapeWebsiteTool |
| **Output**     | Markdown |

---

## 📁 Project Structure

```
market-trend-analyzer/
├── market_analyzer.py    # Main script
├── .env                  # Environment configuration
├── research_findings.md  # Research agent's raw output
├── final_report.md       # Summarized report
└── README.md             # Project documentation
```

---

## ⚙️ Installation & Setup

### Prerequisites
- Python **3.10+**
- Ollama installed and running with **llama3:8b**  
  _(Run: `ollama pull llama3:8b`)_

### 1. Clone & Install Requirements
```bash
git clone <your-repo>
cd market-trend-analyzer

pip install crewai==0.157.0 crewai-tools==0.47.1 langchain-ollama==0.3.0 duckduckgo-search python-dotenv
pip install "langchain-core<1.0.0" "langchain-community<1.0.0"
```

### 2. Configure Environment
Create a `.env` file in the project root:
```
CREWAI_LLM_PROVIDER=ollama
CREWAI_DISABLE_OPENAI_FALLBACK=true
CREWAI_EMBEDDINGS_PROVIDER=ollama
OLLAMA_API_BASE=http://localhost:11434
```

### 3. Start Ollama
```bash
ollama serve
```

### 4. Run the Analyzer
```bash
python market_analyzer.py
```

Output files:
- `research_findings.md`
- `final_report.md`

---

## 🎮 Usage Guide

To analyze a custom topic, modify the input in `market_analyzer.py`:

```python
crew_inputs = {'topic': 'Latest Trends in AI in Finance'}
```

After running, review `final_report.md` for the summarized market insights.  
Use or adapt both markdown outputs for reports, blogs, or presentations.

---

## 💡 Example Outputs

### Market Trend Report: *Latest Trends in AI in Finance*

#### Introduction
The finance industry has witnessed significant advancements driven by AI...

#### Trends
- **Predictive Maintenance:** Detects anomalies and fraud patterns.  
- **Automated Trading:** Leverages AI-driven decision platforms.  
- ...

#### Conclusion
AI is transforming finance — proactive adoption will define future leaders.

---

## 🔧 Troubleshooting & FAQ

- **OpenAI Key Errors** – Ensure `.env` matches the config above and that you set  
  `model="ollama/llama3:8b"` with `api_base` in the CrewAI LLM constructor.

- **DuckDuckGo Fails** – Verify that `DuckDuckGoSearchRun` is imported and registered  
  as a CrewAI `BaseTool`.

- **Dependency Conflicts** – Uninstall `langchain-classic`; keep `langchain-core`  
  and `langchain-community` **below v1.0.0**.

- **Agent/Task Output Missing** – Make sure each task includes the `output_file` parameter  
  for persistent results.

---

## ☁️ Deployment

- **Local:** Fully offline operation with Ollama and Python.  
- **Server:** Containerize with Docker and deploy on any system (Linux/Mac/Windows)  
  that supports Ollama.

---
