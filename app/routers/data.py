from fastapi import APIRouter, UploadFile
from app.services.ai.ingestion import ingest_support_materials
import tempfile, shutil

router = APIRouter(prefix="/support", tags=["Support"])

@router.post("/ingest/{company_id}")
async def ingest_docs(company_id: str, file: UploadFile):
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        shutil.copyfileobj(file.file, tmp)
        tmp_path = tmp.name

    result = ingest_support_materials(tmp_path, company_id)
    return result