-- Enable vector extension (IMPORTANT)
create extension if not exists vector;

-- -----------------------------
-- Documents table (RAG storage)
-- -----------------------------
create table if not exists documents (
    id bigserial primary key,
    content text not null,
    embedding vector(768) not null,
    metadata jsonb default '{}'::jsonb,
    created_at timestamp default now()
);

-- -----------------------------
-- Vector search function
-- -----------------------------
create or replace function match_documents (
    query_embedding vector(768),
    match_count int default 5
)
returns table (
    id bigint,
    content text,
    similarity float
)
language sql stable
as $$
    select
        id,
        content,
        1 - (embedding <=> query_embedding) as similarity
    from documents
    order by embedding <=> query_embedding
    limit match_count;
$$;

-- -----------------------------
-- Index for fast similarity search
-- -----------------------------
create index if not exists documents_embedding_idx
on documents
using ivfflat (embedding vector_cosine_ops)
with (lists = 100);