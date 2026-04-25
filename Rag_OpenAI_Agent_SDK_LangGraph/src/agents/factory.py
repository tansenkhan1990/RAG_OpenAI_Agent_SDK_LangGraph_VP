from agents import Agent, Runner
from src.config import settings
from src.tools.rag_tool import rag_tool
from src.tools.search_tool import search_tool


# 🔹 RAG Agent
rag_agent = Agent(
    name="rag_agent",
    instructions="Use rag_tool to answer from private data only.",
    model=settings.MODEL,
    tools=[rag_tool]
)

# 🔹 Web Agent
search_agent = Agent(
    name="search_agent",
    instructions="Use search_tool for latest or web data.",
    model=settings.MODEL,
    tools=[search_tool]
)

# 🔹 General Agent
general_agent = Agent(
    name="general_agent",
    instructions="Answer general knowledge questions.",
    model=settings.MODEL
)

# 🔹 Router Agent
router_agent = Agent(
    name="router",
    instructions="""
Decide best route:
- rag → private knowledge
- search → internet
- general → common knowledge

Return only one word.
""",
    model=settings.MODEL
)


async def route_query(query: str) -> str:
    result = await Runner.run(router_agent, query)
    return result.final_output.strip().lower()


async def run_agent(route: str, query: str) -> str:
    if "rag" in route:
        result = await Runner.run(rag_agent, query)
        return "rag", result.final_output

    elif "search" in route:
        result = await Runner.run(search_agent, query)
        return "websearch", result.final_output

    else:
        result = await Runner.run(general_agent, query)
        return "llm", result.final_output