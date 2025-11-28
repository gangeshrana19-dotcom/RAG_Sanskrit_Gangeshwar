from rag_pipeline import rag_pipeline

def main():
    print("Sanskrit RAG System Ready")
    while True:
        query = input("\nEnter Sanskrit Query: ")
        if query.lower() in ["exit", "quit"]:
            break
        print("\nAnswer:\n")
        print(rag_pipeline(query))

if __name__ == "__main__":
    main()