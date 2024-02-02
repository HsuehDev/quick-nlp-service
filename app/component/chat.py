from pydantic import BaseModel
from typing import List, Optional
import os

class RoleItem(BaseModel):
    role: str
    content: str

class Params(BaseModel):
    engine: str = ''
    temperature: Optional[float] = 0.7
    max_tokens: Optional[int] = 200
    top_p: Optional[float] = 0.95
    top_k: Optional[int] = 5
    roles: List[RoleItem]
    frequency_penalty: Optional[float]
    presence_penalty: Optional[float]
    stop: Optional[str] = ""
    past_messages: Optional[int] = 10
    purpose: str = "dev"
    
class Response(BaseModel):
    purpose: str
    input_messages: List[RoleItem]
    response: dict