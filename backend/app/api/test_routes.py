# app/api/test_routes.py

from fastapi import APIRouter
from pydantic import BaseModel
from app.services.llm_service import llm

router = APIRouter()

class QueryRequest(BaseModel):
    text: str

@router.post("/test-llm")
async def test_llm(request: QueryRequest):
    response = await llm.ainvoke(request.text)
    return {
        "input": request.text,
        "output": response.content.strip()
    }