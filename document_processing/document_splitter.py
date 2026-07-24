from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import settings

class DocumentSplitter:
    """
    Splits LangChain Document objects into smaller chunks.
    """
    @staticmethod
    def split(documents: list[Document]) -> list[Document]:
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.CHUNK_SIZE,
            chunk_overlap=settings.CHUNK_OVERLAP,
        )
        chunks = splitter.split_documents(documents)
        return chunks