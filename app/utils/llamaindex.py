from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.vector_stores.qdrant import QdrantVectorStore
from app.core.db import qdrant_client

def build_index_from_docs(doc_path: str, collection_name: str):
    """Read local docs and build an index in Qdrant."""
    docs = SimpleDirectoryReader(doc_path).load_data()
    vector_store = QdrantVectorStore(
        client=qdrant_client,
        collection_name=collection_name
    )
    index = VectorStoreIndex.from_documents(docs, vector_store=vector_store)
    return index

def load_index(collection_name: str):
    """Load an existing index from Qdrant."""
    vector_store = QdrantVectorStore(
        client=qdrant_client,
        collection_name=collection_name
    )
    return VectorStoreIndex.from_vector_store(vector_store)