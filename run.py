from services.rag_service import RAGService

def main():

    rag = RAGService()

    pdf_path = input("Enter PDF path: ")

    rag.process_document(pdf_path)

    while True:

        question = input("\nYou: ")

        if question.lower() in ["exit", "quit"]:
            break

        answer = rag.ask_question(question)

        print(f"\nAssistant: {answer}")


if __name__ == "__main__":
    main()