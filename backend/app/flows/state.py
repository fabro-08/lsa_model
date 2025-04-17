# app/flows/state.py

from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from langchain.schema import BaseMessage

class GraphState(BaseModel):
    prompt_user: Optional[str] = None
    text: Optional[str] = None
    model: Optional[str] = None
    response: Optional[Dict[str, Any]] = None