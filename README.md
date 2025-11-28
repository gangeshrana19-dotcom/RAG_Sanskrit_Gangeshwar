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
|- requirement_min.txt


**Installation Instructions**
Run all the commands in command prompt or powershell of your PC

1. Clone the repository:
   git clone https://github.com/<your-username>/RAG_Sanskrit_<YourName>.git
   cd RAG_Sanskrit_<YourName>
   
2. Create the virual environment for the RAG
    python -m venv venv
    source venv/bin/activate       (Linux/Mac)
    venv\Scripts\activate          (Windows)

3. Install Dependencies
   pip install -r code/requirements.txt

**How to Run the RAG System**
1. Place your Sanskrit document(that should be only in .txt or .pdf or .docx file) in data/sample_sanskrit_docs/ folder.
2. Now open Command prompt or Powershell and go to path of code and run the main app command "python code/app.py".
3. After running the command, It will ask for the query. Enter the query: e.g. “किं करोति राजा भोजः?” or “Vedanta philosophy explanation in Sanskrit” etc.
The system will retrieve relevant text and generates the answer.

**Technical Flow**
1. Document Loading → Read .txt/.pdf files
2. Preprocessing → Cleaning, tokenization, chunking
3. Embedding/Indexing → Vector store creation
4. Query Interface → Sanskrit / Transliteration input
5. Retriever → Fetch top-matching context chunks
6. Generator (LLM) → Produce final answer using context
7. Output → Display retrieved answer

**Example Query and Response**
User Query: "King Bhoj proclamation in Sanskrit?"
System Output:
"राजा भोजः विद्यानां महत्त्वम् अभ्यधात्..."


**Author**
Gangeshwar
AI/ML Intern
2025

