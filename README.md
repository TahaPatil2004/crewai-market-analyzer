🤖 Market Trend Analyzer – Multi-Agent AI Powerhouse
An intelligent, fully local market research and trend reporting workflow driven by CrewAI agents and Ollama. No API keys or cloud required—research, analyze, and summarize market trends directly on your machine.
📋 Table of Contents
* 🎯 Project Overview
* 🏗️ System Architecture
* 🚀 Key Features
* 🛠️ Technology Stack
* 📁 Project Structure
* ⚙️ Installation & Setup
* 🎮 Usage Guide
* 💡 Example Outputs
* 🔧 Troubleshooting & FAQ
* ☁️ Deployment
* 📞 Community & Support
🎯 Project Overview
Market Trend Analyzer automates deep-dive market research. It uses a powerful three-phase AI workflow:
* Researcher Agent: Finds real, up-to-date data/news from the web.
* Analyst Agent: Identifies and explains major trends and impacts.
* Writer Agent: Produces concise, executive-level markdown reports.
Run on your own device, with Llama 3 powered by Ollama—completely private and offline.
🏗️ System Architecture
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

🚀 Key Features
* 🔎 Automates market research using real-time web search and web scraping.
* 🧠 Delivers expert trend analysis from multiple current sources.
* 📝 Generates clean markdown reports ready for sharing or publication.
* 🔒 Runs locally with Ollama—no data is sent off-device.
* ⚡️ No OpenAI API key needed—no cloud cost or privacy risks.
🛠️ Technology Stack
Layer
	Technology
	Backend
	Python 3.10+, CrewAI
	LLM
	Ollama (Llama 3 / 8B model)
	Web Search
	DuckDuckGoSearchRun
	Web Scraping
	ScrapeWebsiteTool
	Output
	Markdown
	📁 Project Structure
market-trend-analyzer/
├── market_analyzer.py    # Main script
├── .env                  # Environment config (see below)
├── research_findings.md  # Research agent's output
├── final_report.md       # Human-readable summary report
└── README.md             # This file

⚙️ Installation & Setup
Prerequisites
* Python 3.10+
* Ollama installed and running with llama3:8b (ollama pull llama3:8b)
1. Clone & Install Requirements
git clone <your-repo>
cd market-trend-analyzer
pip install crewai==0.157.0 crewai-tools==0.47.1 langchain-ollama==0.3.0 duckduckgo-search python-dotenv
pip install "langchain-core<1.0.0" "langchain-community<1.0.0"

2. Configure Environment
Create a .env in your repo root:
CREWAI_LLM_PROVIDER=ollama
CREWAI_DISABLE_OPENAI_FALLBACK=true
CREWAI_EMBEDDINGS_PROVIDER=ollama
OLLAMA_API_BASE=http://localhost:11434

3. Start Ollama
(In a separate terminal, if not already running)
ollama serve

4. Run the Analyzer
python market_analyzer.py

The script will produce research_findings.md and final_report.md in your project folder.
🎮 Usage Guide
* Change the crew_inputs in market_analyzer.py to target any topic:
crew_inputs = {'topic': 'Latest Trends in AI in Finance'}

* Review final_report.md for your human-friendly summary.
* Use or modify the research/analysis report files as needed!
💡 Example Outputs
# Market Trend Report: Latest Trends in AI in Finance

### Introduction
The finance industry has witnessed significant advancements driven by AI...

### Trends
**Predictive Maintenance:** Detects anomalies and fraud...
**Automated Trading:** AI-driven decision platforms...
...

### Conclusions
AI is transforming finance—proactive adoption will define winners.

🔧 Troubleshooting & FAQ
   * OpenAI Key Errors: Ensure you’re using the .env shown above, and you use model="ollama/llama3:8b" with api_base in the CrewAI LLM constructor.
   * DuckDuckGo fails: Confirm you imported and wrapped DuckDuckGoSearchRun as a CrewAI BaseTool.
   * Dependency Conflicts: Uninstall langchain-classic; keep langchain-core and langchain-community below v1.0.0.
   * Agent/Task Errors: Ensure all tasks use the correct output_file parameter if you want persistent outputs.
☁️ Deployment
   * Local: Works fully offline with Ollama and Python.
   * Server: Containerize the app with Docker and host on any machine with Ollama installed (Linux/Mac/Windows).
📞 Community & Support
   * Read the CrewAI docs
   * Ask questions or report issues on the CrewAI Community Forum
   * For Ollama troubleshooting, see Ollama Docs
License
MIT License
Credits
   * CrewAI
   * Ollama
   * DuckDuckGoSearchRun, ScrapeWebsiteTool
