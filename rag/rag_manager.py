from embeddings.embedding_manager import EmbeddingManager
from retrieval.retriever_manager import RetrieverManager
from llm.llm_manager import LLMManager
from prompts.prompt_manager import PromptManager
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains import create_retrieval_chain

class RAGManager:
    def __init__(self):
        self.embedding_model = EmbeddingManager.get_embedding_model()

        self.retriever = RetrieverManager.get_retriever(
            embedding_model=self.embedding_model
        )

        self.llm = LLMManager.get_llm()

        self.prompt = PromptManager.get_rag_prompt()

        self.document_chain = create_stuff_documents_chain(
            llm=self.llm,
            prompt=self.prompt,
        )

        self.rag_chain = create_retrieval_chain(
            retriever=self.retriever,
            combine_docs_chain=self.document_chain,
        )

    def ask(self, question: str) -> str:

        response = self.rag_chain.invoke(
            {
                "input": question
            }
        )

        return response["answer"]