from langgraph.graph import StateGraph, START, END
from src.graph.state import State
from src.agents.factory import route_query, run_agent


async def router_node(state: State):
    route = await route_query(state["query"])
    return {"route": route}


async def agent_node(state):
    source, answer = await run_agent(state["route"], state["query"])

    return {
        "answer": answer,
        "source": source
    }

def build_graph():
    graph = StateGraph(State)

    graph.add_node("router", router_node)
    graph.add_node("agent", agent_node)

    graph.add_edge(START, "router")
    graph.add_edge("router", "agent")
    graph.add_edge("agent", END)

    return graph.compile()