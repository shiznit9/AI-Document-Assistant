from config.settings import *

def create_retriever(vector_store):

    if RETRIEVER_SEARCH_TYPE == "similarity":
        return vector_store.as_retriever(
            search_type="similarity",
            search_kwargs={
                "k": RETRIEVER_K
            }
        )

    elif RETRIEVER_SEARCH_TYPE == "mmr":
        return vector_store.as_retriever(
            search_type="mmr",
            search_kwargs={
                "k": RETRIEVER_K,
                "fetch_k": RETRIEVER_FETCH_K,
                "lambda_mult": RETRIEVER_LAMBDA
            }
        )
    else:
        raise ValueError(f"Unsupported search type: {RETRIEVER_SEARCH_TYPE}")