import os
os.environ.pop("OPENAI_API_KEY", None)
os.environ["CREWAI_LLM_PROVIDER"] = "ollama"
os.environ["CREWAI_EMBEDDINGS_PROVIDER"] = "ollama"
os.environ["CREWAI_DISABLE_OPENAI_FALLBACK"] = "true"
from crewai import Agent, Task, Crew, Process, LLM
from crewai.tools import BaseTool
from crewai_tools import ScrapeWebsiteTool
from langchain_community.tools import DuckDuckGoSearchRun

# --- 1. SET UP LLM ---
llm = LLM(
    model="ollama/llama3:8b",
    api_base="http://localhost:11434",
    api_key="ollama",
    temperature=0.5
)
print("CrewAI Ollama LLM initialized successfully.")

# --- 2. DEFINE TOOLS ---

# CrewAI-compatible wrapper for DuckDuckGo
class DuckDuckGoSearchTool(BaseTool):
    name: str = "DuckDuckGo Search"
    description: str = "Searches the web using DuckDuckGo for up-to-date market information."

    def _run(self, query: str) -> str:
        search = DuckDuckGoSearchRun()
        return search.run(query)

# Instantiate tools
search_tool = DuckDuckGoSearchTool()
scrape_tool = ScrapeWebsiteTool()

# --- 3. DEFINE AGENTS ---

researcher_agent = Agent(
    role='Market Research Specialist',
    goal='Find the latest and most relevant information about {topic}',
    backstory=(
        "You are a detailed market researcher specializing in web data extraction and trend discovery."
    ),
    tools=[search_tool, scrape_tool],
    llm=llm,
    verbose=True,
    allow_delegation=False
)

analyst_agent = Agent(
    role='Senior Market Analyst',
    goal='Analyze research outputs to identify 3–5 key trends, implications, and opportunities in {topic}.',
    backstory=(
        "You synthesize data into actionable insights for business strategy and market foresight."
    ),
    tools=[],
    llm=llm,
    verbose=True,
    allow_delegation=False
)

writer_agent = Agent(
    role='Technology Report Writer',
    goal='Prepare a concise, executive-friendly report summarizing the {topic} analysis.',
    backstory=(
        "You translate complex insights into clear, actionable summaries for business stakeholders."
    ),
    tools=[],
    llm=llm,
    verbose=True,
    allow_delegation=False
)

# --- 4. DEFINE TASKS ---

research_task = Task(
    description=(
        "Research the topic {topic}. Find at least 5 credible, recent sources from the last 6 months."
    ),
    expected_output=(
        "A Markdown bullet list: each finding includes a title, summary (1–2 lines), and URL."
    ),
    agent=researcher_agent,
    output_file='research_findings.md'
)

analysis_task = Task(
    description=(
        "Analyze the above findings and identify 3–5 major trends with short analyses for each. "
        "Explain potential impacts and importance."
    ),
    expected_output=(
        "A structured analysis with:\n"
        "1. Key Trends\n2. Analysis per trend\n3. Conclusion section."
    ),
    context=[research_task],
    agent=analyst_agent
)

writing_task = Task(
    description=(
        "Write a well-structured 3–4 paragraph report summarizing the analyst’s findings, "
        "including introduction, trends, and conclusions."
    ),
    expected_output="A markdown-formatted report titled 'Market Trend Report: {topic}'.",
    context=[analysis_task],
    agent=writer_agent
)

# --- 5. RUN CREW ---

crew_inputs = {'topic': 'Latest Trends in AI in Finance'}

market_analysis_crew = Crew(
    agents=[researcher_agent, analyst_agent, writer_agent],
    tasks=[research_task, analysis_task, writing_task],
    process=Process.sequential,
    verbose=True
)

print("\nStarting Market Analysis Crew...")
print(f"Topic: {crew_inputs['topic']}")
result = market_analysis_crew.kickoff(inputs=crew_inputs)

print("\nFinal Report:")
print(result)
print("\n---------------------------------")

