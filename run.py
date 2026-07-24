from rag.rag_manager import RAGManager

rag = RAGManager()

while True:
    question = input("\nAsk a question (or type 'exit'): ")

    if question.lower() == "exit":
        break

    answer = rag.ask(question)
    print("\nAnswer:")
    print(answer)