from langchain_mistralai import ChatMistralAI
from config.settings import LLM_MODEL

def get_llm():
    return ChatMistralAI(model_name = LLM_MODEL)
