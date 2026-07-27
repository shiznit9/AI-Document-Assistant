from pathlib import Path

from document_processing.document_metadata import DocumentMetadata
from langchain_core.documents import Document
from langchain_community.document_loaders import (
    BSHTMLLoader,
    CSVLoader,
    Docx2txtLoader,
    JSONLoader,
    PyPDFLoader,
    TextLoader,
    UnstructuredExcelLoader,
    UnstructuredMarkdownLoader,
    UnstructuredPowerPointLoader,
)
from langchain_community.document_loaders.email import UnstructuredEmailLoader
from langchain_community.document_loaders.xml import UnstructuredXMLLoader


SUPPORTED_LOADERS = {
    ".pdf": PyPDFLoader,
    ".docx": Docx2txtLoader,
    ".txt": TextLoader,
    ".md": UnstructuredMarkdownLoader,
    ".html": BSHTMLLoader,
    ".csv": CSVLoader,
    ".xlsx": UnstructuredExcelLoader,
    ".xls": UnstructuredExcelLoader,
    ".pptx": UnstructuredPowerPointLoader,
    ".json": JSONLoader,
    ".xml": UnstructuredXMLLoader,
    ".eml": UnstructuredEmailLoader,
}


class DocumentLoader:
    """
    Loads supported document types and returns LangChain Document objects.
    """

    @staticmethod
    def is_supported(file_path: Path) -> bool:
        """
        Checks whether the given document type is supported.

        Args:
            file_path: Path to the document.

        Returns:
            True if the document type is supported, otherwise False.
        """
        return file_path.suffix.lower() in SUPPORTED_LOADERS

    @staticmethod
    def load(file_path: Path) -> list[Document]:
        """
        Loads a supported document.

        Args:
            file_path: Path to the document.

        Returns:
            List of LangChain Document objects.

        Raises:
            FileNotFoundError: If the file does not exist.
            ValueError: If the file type is not supported.
        """

        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        if not DocumentLoader.is_supported(file_path):
            raise ValueError(
                f"Unsupported file type: {file_path.suffix.lower()}. "
                f"Supported types: {', '.join(SUPPORTED_LOADERS.keys())}"
            )

        loader = SUPPORTED_LOADERS[file_path.suffix.lower()](str(file_path))

        documents = loader.load()

        documents = DocumentMetadata.add_metadata(
            documents,
            file_path,
        )

        return documents