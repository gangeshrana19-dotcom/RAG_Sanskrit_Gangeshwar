import re
import nltk
nltk.download('punkt')

def clean_text(text):
    # Keep Devanagari + letters + spaces
    text = re.sub(r"[^\u0900-\u097F\w\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def chunk_text(text, max_tokens=100):
    words = text.split()
    chunks = []
    for i in range(0, len(words), max_tokens):
        chunks.append(" ".join(words[i:i+max_tokens]))
    return chunks