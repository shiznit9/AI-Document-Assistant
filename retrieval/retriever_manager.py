from langchain_core.vectorstores import VectorStoreRetriever
from langchain_huggingface import HuggingFaceEmbeddings

from config import settings
from vector_store.vector_store_manager import VectorStoreManager


class RetrieverManager:
    """
    Creates and manages the application's retriever.
    """

    @staticmethod
    def get_retriever(
        embedding_model: HuggingFaceEmbeddings,
    ) -> VectorStoreRetriever:
        """
        Loads the vector store and returns a retriever.
        """

        vector_store = VectorStoreManager.load(
            embedding_model=embedding_model
        )

        retriever = vector_store.as_retriever(
            search_type=settings.RETRIEVER_SEARCH_TYPE,
            search_kwargs={
                "k": settings.RETRIEVER_K,
            },
        )

        return retriever