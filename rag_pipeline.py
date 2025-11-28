from loader import load_documents
from preprocess import clean_text, chunk_text
from embedder import load_embedding_model, get_embeddings
from retriever import Retriever
from generator import load_llm, generate_answer
from pathlib import Path
import numpy as np

def rag_pipeline(query, data_path=None):
    if data_path is None:
        project_root = Path(__file__).resolve().parent.parent
        data_path = project_root / "data" / "sample_sanskrit_docs"

    docs = load_documents(str(data_path))
    cleaned_docs = [clean_text(doc) for doc in docs]

    chunks = []
    for doc in cleaned_docs:
        chunks.extend(chunk_text(doc))

    embed_model = load_embedding_model()
    chunk_embeddings = np.array(get_embeddings(embed_model, chunks))

    retriever = Retriever(chunks)
    retrieved_context = retriever.search(query, top_k=3)

    tokenizer, llm = load_llm()

    # GPT-2 maximum input length (usually 1024 tokens)
    model_max_input = 1024
    answer_tokens = 120              # space we want for generated answer
    input_budget = model_max_input - answer_tokens

    # Limit the context so it does NOT exceed GPT-2 limits
    final_context = []
    total_chars = 0

    # add only as much text as fits safely (character-level simple limit)
    for chunk in retrieved_context:
        if total_chars + len(chunk) > 1500:    # safe limit: 1500 characters
            break
        final_context.append(chunk)
        total_chars += len(chunk)

    # build prompt using only the trimmed context
    prompt = (
        "Context:\n" +
        "\n".join(final_context) +
        "\n\nQuery: " + query +
        "\nAnswer:"
    )

    answer = generate_answer(tokenizer, llm, prompt)
    return answer