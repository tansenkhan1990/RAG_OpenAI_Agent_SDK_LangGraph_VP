from agents import function_tool
import requests

@function_tool
def search_tool(query: str) -> str:
    url = "https://api.duckduckgo.com/"
    res = requests.get(url, params={"q": query, "format": "json"}).json()

    results = []

    for item in res.get("RelatedTopics", [])[:5]:
        if isinstance(item, dict) and "Text" in item:
            results.append(item["Text"])

    return "\n".join(results)