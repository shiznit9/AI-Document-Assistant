from langchain_core.prompts import ChatPromptTemplate


class PromptManager:
    """
    Creates and manages prompts used by the RAG pipeline.
    """

    @staticmethod
    def get_rag_prompt() -> ChatPromptTemplate:
        """
        Returns the prompt template used for question answering.
        """

        return ChatPromptTemplate.from_template(
            """
You are an AI Document Assistant.

Answer the user's question using ONLY the provided context.

Instructions:
- If the answer is present in the context, answer clearly and concisely.
- Do not use outside knowledge.
- Do not make up information.
- If the answer cannot be found in the context, respond exactly with:
  "I couldn't find that information in the uploaded documents."

Context:
{context}

Question:
{input}

Answer:
"""
        )