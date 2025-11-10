from fastapi import APIRouter, File, UploadFile, HTTPException
from pydantic import BaseModel
import os
from backend.utils.document_utils import process_document

router = APIRouter()

UPLOAD_DIR = "docs/"

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    if not file.filename.endswith(('.pdf', '.docx')):
        raise HTTPException(status_code=400, detail="Only PDF or DOCX files allowed")
    
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())
    
    result = process_document(file_path)
    return result
