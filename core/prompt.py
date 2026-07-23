from langchain_core.prompts import ChatPromptTemplate


SYSTEM_PROMPT = """
You are a helpful AI assistant.

Answer the user's question using ONLY the provided context.

If the answer cannot be found in the context, reply exactly:

"I could not find the answer in the document."
"""


HUMAN_PROMPT = """
Context:
{context}

Question:
{question}
"""


def get_prompt():
    return ChatPromptTemplate(
        [
            ("system", SYSTEM_PROMPT),
            ("human", HUMAN_PROMPT),
        ]
    )