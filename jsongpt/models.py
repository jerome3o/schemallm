from typing import List, Optional
from pydantic import BaseModel


class CompletionRequest(BaseModel):
    prompt: str
    max_tokens: int = 2000
    stop: Optional[List[str]] = None


class SchemaCompletionRequest(CompletionRequest):
    schema_restriction: dict = None


class CompletionResponse(BaseModel):
    completion: str
