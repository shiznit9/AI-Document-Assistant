from core.llm import get_llm
from core.prompt import get_prompt

def answer_question(question, retriever):
    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    prompt = get_prompt()

    final_prompt = prompt.invoke(
        {
            "context": context,
            "question": question
        }
    )

    llm = get_llm()

    response = llm.invoke(final_prompt)

    return response.content