from pathlib import Path

from document_processing.document_loader import DocumentLoader
from document_processing.document_splitter import DocumentSplitter
from embeddings.embedding_manager import EmbeddingManager
from vector_store.vector_store_manager import VectorStoreManager


class DocumentManager:
    """
    Coordinates the document ingestion workflow.
    """

    @staticmethod
    def ingest(file_path: Path) -> None:
        """
        Loads a document, checks for duplicates, splits it into chunks,
        generates embeddings, and stores them in the vector database.

        Args:
            file_path: Path to the document.
        """
        documents = DocumentLoader.load(file_path)

        file_hash = documents[0].metadata["file_hash"]

        embedding_model = EmbeddingManager.get_embedding_model()

        vector_store = VectorStoreManager.load(
            embedding_model=embedding_model,
        )

        if VectorStoreManager.document_exists(
            vector_store=vector_store,
            file_hash=file_hash,
        ):
            print(f"Document '{file_path.name}' already exists. Skipping ingestion.")
            return

        chunks = DocumentSplitter.split(documents)

        VectorStoreManager.add_documents(
            vector_store=vector_store,
            documents=chunks,
        )