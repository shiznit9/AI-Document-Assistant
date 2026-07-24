from langchain_core.prompts import ChatPromptTemplate

class PromptManager:

    @staticmethod
    def get_rag_prompt() -> ChatPromptTemplate:

        prompt = ChatPromptTemplate.from_template(
            """
You are a helpful AI assistant.
Use ONLY the provided context to answer the user's question.
If the answer is not contained in the context, reply:
"I couldn't find that information in the uploaded documents."
Context:
{context}
Question:
{input}
Answer:
"""
        )
        return prompt