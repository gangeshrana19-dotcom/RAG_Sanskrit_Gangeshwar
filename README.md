# RAG_Sanskrit_Gangeshwar
A Sanskrit document Retrieval-Augment Generation system 
It is a kind of RAG system which ingested Sanskrit documents of format .pdf, .txt, or .docx file and based on the documents provides answers of the user's query. The system entirely works on CPU only and supportqueries in both Sanskrit and transliterated English.

**Features of the System:**
° Ingests Sanskrit .txt, .docx or .pdf documents.
° Preprocesses text (tokenization, cleaning, chunking)
° Creates embeddings for retrieval
° Retrieves relevant context using vector/keyword search
° Generates answers using a CPU-based LLM
° Fully modular RAG pipeline

**Project Structure:**
RAG_Sanskrit_Gangeshwar
|
|- code/
    |-loader.py
    |-preprocess.py
    |-embedder.py
    |-retriever.py
    |-rag_pipeline.py
    |-generator.py
    |-app.py
|
|- data/
    |- sample_sanskrit_docs
        |-Rag_docs.docx
        |-Rag_docs.pdf
        |-Rag_docs.txt
|
|- report/
    |- Rag_Sanskrit_Project_Report.pdf
|
|- README.md
|
|


