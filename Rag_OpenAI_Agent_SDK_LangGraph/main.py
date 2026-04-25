# 🔥 MUST BE FIRST
import os

os.environ["OPENAI_AGENTS_DISABLE_TRACING"] = "1"
os.environ["OPENAI_DISABLE_TELEMETRY"] = "true"

from fastapi import FastAPI
from pydantic import BaseModel
from src.graph.workflow import build_graph

app = FastAPI()
graph = build_graph()


class Request(BaseModel):
    query: str


@app.post("/ask")
async def ask(req: Request):
    result = await graph.ainvoke({
        "query": req.query,
        "route": "",
        "answer": "",
        "source": ""
    })

    return {
        "query": req.query,
        "route": result["route"],
        "source": result["source"],   # 🔥 IMPORTANT
        "answer": result["answer"]
    }