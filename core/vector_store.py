from langchain_chroma import Chroma
from core.embeddings import get_embedding_model

def create_vector_store(chunks, db_path):
    return Chroma.from_documents(
        documents=chunks,
        embedding=get_embedding_model(),
        persist_directory=db_path
    )

def load_vector_store(db_path):
    return Chroma(
        persist_directory=db_path,
        embedding_function=get_embedding_model()
    )