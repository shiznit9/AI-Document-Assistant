from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from config import settings

class VectorStoreManager:
    """
    Creates and manages the application's Chroma vector store.
    """

    @staticmethod
    def load(
        embedding_model: HuggingFaceEmbeddings,
    ) -> Chroma:
        """
        Loads the application's Chroma vector store.
        If it doesn't exist, Chroma will create it automatically.
        """

        vector_store = Chroma(
            persist_directory=settings.CHROMA_DB_DIRECTORY,
            embedding_function=embedding_model,
        )

        return vector_store

    @staticmethod
    def add_documents(
        vector_store: Chroma,
        documents: list[Document],
    ) -> None:
        """
        Adds new document chunks to the vector store.
        """

        vector_store.add_documents(documents)