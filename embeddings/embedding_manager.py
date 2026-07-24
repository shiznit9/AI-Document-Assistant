from langchain_huggingface import HuggingFaceEmbeddings
from config import settings

class EmbeddingManager:
    """
    Creates and manages the embedding model used by the application.
    """
    @staticmethod
    def get_embedding_model() -> HuggingFaceEmbeddings:
        embedding_model = HuggingFaceEmbeddings(
            model_name=settings.EMBEDDING_MODEL
        )
        return embedding_model