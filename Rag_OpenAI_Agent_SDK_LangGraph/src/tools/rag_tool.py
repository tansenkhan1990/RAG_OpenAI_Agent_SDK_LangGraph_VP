from agents import function_tool
from src.database.supabase_client import supabase
from src.tools.embedding import embed

@function_tool
def rag_tool(query: str) -> str:
    q_emb = embed(query)

    res = supabase.rpc(
        "match_documents",
        {
            "query_embedding": q_emb,
            "match_count": 5
        }
    ).execute()

    docs = res.data or []

    if not docs:
        return "No relevant documents found."

    return "\n\n".join([d["content"] for d in docs])