from openai import OpenAI
from src.config import settings

client = OpenAI(
    base_url=settings.BASE_URL,
    api_key=settings.API_KEY
)

def embed(text: str):
    res = client.embeddings.create(
        model=settings.EMBED_MODEL,
        input=text
    )
    return res.data[0].embedding