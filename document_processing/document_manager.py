from pathlib import Path
from langchain_core.documents import Document
from document_processing.document_loader import DocumentLoader
from document_processing.document_splitter import DocumentSplitter
from embeddings.embedding_manager import EmbeddingManager
from vector_store.vector_store_manager import VectorStoreManager

class DocumentManager:
    """
    Coordinates the document ingestion workflow.
    """
    @staticmethod
    def ingest(file_path: Path):
        """
        Loads a document and prepares it for downstream processing by
        splitting it into chunks.

        Args:
            file_path: Path to the document.

        Returns:
            List of chunked LangChain Document objects.
        """

        documents = DocumentLoader.load(file_path)

        chunks = DocumentSplitter.split(documents)

        embedding_model = EmbeddingManager.get_embedding_model()

        vector_store = VectorStoreManager.load(
            embedding_model=embedding_model,
        )

        VectorStoreManager.add_documents(
            vector_store=vector_store,
            documents=chunks,
        )