from app.utils.llamaindex import build_index_from_docs

def ingest_support_materials(doc_path: str, company_id: str):
    """Ingest support docs into Qdrant under company namespace."""
    collection_name = f"support_{company_id}"
    build_index_from_docs(doc_path, collection_name)
    return {"status": "success", "collection": collection_name}