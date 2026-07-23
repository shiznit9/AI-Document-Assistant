# config/settings.py
from dotenv import load_dotenv
import os

load_dotenv()

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

# Vector Database
CHROMA_DB_DIRECTORY = "data/chroma_db"

# Text Splitting
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# Embedding Model
EMBEDDING_MODEL = "BAAI/bge-large-en-v1.5"

# LLM
LLM_MODEL = "mistral-small-2506"

# Retriever
RETRIEVER_SEARCH_TYPE = "similarity"
RETRIEVER_K = 10
RETRIEVER_FETCH_K = 10
RETRIEVER_LAMBDA = 0.5