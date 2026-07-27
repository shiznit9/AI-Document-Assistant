import uuid
from pathlib import Path
from langchain_core.documents import Document
import hashlib

class DocumentMetadata:
    """
    Handles document metadata generation and attachment.
    """
    @staticmethod
    def generate_document_id() -> str:
        return str(uuid.uuid4())

    @staticmethod
    def generate_file_hash(file_path: Path) -> str:
        """
        Generates a SHA-256 hash for the given file.

        Args:
            file_path: Path to the document.

        Returns:
            SHA-256 hash of the file as a hexadecimal string.
        """

        CHUNK_SIZE = 8192

        sha256 = hashlib.sha256()

        with open(file_path, "rb") as file:

            while chunk := file.read(CHUNK_SIZE):
                sha256.update(chunk)

        return sha256.hexdigest()

    @staticmethod
    def extract_file_metadata(file_path: Path) -> dict:
        """
        Extracts metadata from the file path.

        Args:
            file_path: Path to the uploaded document.

        Returns:
            Dictionary containing basic document metadata.
        """

        return {
            "document_name": file_path.name,
            "document_stem": file_path.stem,
            "file_type": file_path.suffix.lower().lstrip("."),
        }

    @staticmethod
    def add_metadata(
        documents: list[Document],
        file_path: Path,
    ) -> list[Document]:
        """
        Adds custom metadata to every loaded document while
        preserving existing metadata.
        """

        document_id = DocumentMetadata.generate_document_id()

        file_hash = DocumentMetadata.generate_file_hash(file_path)

        file_metadata = DocumentMetadata.extract_file_metadata(file_path)

        for document in documents:

            document.metadata.update({
                "document_id": document_id,
                "file_hash": file_hash,
                **file_metadata,
            })

        return documents

