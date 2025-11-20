from pydantic import BaseModel
from typing import List

class URLRequest(BaseModel):
    url: str

class SummaryResponse(BaseModel):
    summary: List[str]
    key_insights: List[str]
    simplified: str
    citations: List[str]
    quiz: List[str]
