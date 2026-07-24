from pathlib import Path

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

from langchain_community.document_loaders.xml import UnstructuredXMLLoader
from langchain_community.document_loaders.email import UnstructuredEmailLoader

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
    def load(file_path: Path) -> list[Document]:
        """
        Loads a supported document.

        Args:
            file_path: Path to the document.

        Returns:
            List of LangChain Document objects.

        Raises:
            ValueError: If the file type is not supported.
        """
        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        extension = file_path.suffix.lower()

        if extension not in SUPPORTED_LOADERS:
            raise ValueError(
                f"Unsupported file type: {extension}. "
                f"Supported types: {', '.join(SUPPORTED_LOADERS.keys())}"
            )

        loader = SUPPORTED_LOADERS[extension](str(file_path))

        return loader.load()