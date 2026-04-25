import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    BASE_URL = os.getenv("OPENAI_BASE_URL")
    API_KEY = os.getenv("OPENAI_API_KEY")

    MODEL = os.getenv("LOCAL_MODEL_NAME")
    EMBED_MODEL = os.getenv("LOCAL_EMBEDDING_MODEL")

    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_KEY = os.getenv("SUPABASE_KEY")

settings = Settings()