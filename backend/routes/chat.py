from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from backend.models.chat_model import answer_question
from backend.utils.bad_language_filter import filter_bad_language

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/message")
async def chat_message(request: ChatRequest):
    # Filter bad language
    filtered_message = filter_bad_language(request.message)
    if filtered_message != request.message:
        return {"response": "Please refrain from using inappropriate language."}
    
    # Get answer
    answer = answer_question(filtered_message)
    return {"response": answer}
