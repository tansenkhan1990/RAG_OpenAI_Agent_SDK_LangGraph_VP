import sys
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(PROJECT_ROOT)

from pypdf import PdfReader
from src.tools.embedding import embed
from src.database.supabase_client import supabase


def chunk(text, size=500):
    return [text[i:i+size] for i in range(0, len(text), size)]


def load_pdf(path):
    reader = PdfReader(path)
    return "".join([p.extract_text() or "" for p in reader.pages])


def ingest(file_path):
    print("Loading PDF...")
    text = load_pdf(file_path)

    chunks = chunk(text)
    print(f"Chunks: {len(chunks)}")

    for i, c in enumerate(chunks):
        print(f"Embedding {i+1}/{len(chunks)}")

        vector = embed(c)

        supabase.table("documents").insert({
            "content": c,
            "embedding": vector
        }).execute()

    print("DONE ✔")


if __name__ == "__main__":
    pdf_path = os.path.join(PROJECT_ROOT, "src", "data", "Tansen_Khan_CV.pdf")
    ingest(pdf_path)