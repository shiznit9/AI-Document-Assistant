from langchain_mistralai import ChatMistralAI

from config import settings

class LLMManager:
    """
    Creates and manages the application's language model.
    """
    @staticmethod
    def get_llm() -> ChatMistralAI:
        """
        Returns the configured language model.
        """

        llm = ChatMistralAI(
            model_name=settings.LLM_MODEL,
            temperature=settings.LLM_TEMPERATURE,
        )

        return llm