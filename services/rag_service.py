import os

from document_processing.loader import load_pdf
from document_processing.splitter import split_documents

from core.vector_store import (
    create_vector_store,
    load_vector_store,
)

from core.retriever import create_retriever
from core.chain import answer_question

from config.settings import CHROMA_DB_DIRECTORY


class RAGService:

    def __init__(self):
        self.current_db_path = None

    def get_database_path(self, file_path):
        file_name = os.path.splitext(
            os.path.basename(file_path)
        )[0]

        return os.path.join(
            CHROMA_DB_DIRECTORY,
            file_name
        )

    def process_document(self, file_path):

        db_path = self.get_database_path(file_path)
        self.current_db_path = db_path

        if os.path.exists(db_path):
            print("Vector database already exists.")
            return

        documents = load_pdf(file_path)
        chunks = split_documents(documents)

        create_vector_store(chunks, db_path)

        print("Vector database created.")

    def ask_question(self, question):

        if self.current_db_path is None:
            raise Exception("No document has been processed.")

        vector_store = load_vector_store(
            self.current_db_path
        )

        retriever = create_retriever(vector_store)

        return answer_question(
            question,
            retriever
        )