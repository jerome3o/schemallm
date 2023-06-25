from typing import List, Optional
from pydantic import BaseModel

from jsongpt.models.jsonschema import JsonSchema


class CompletionRequest(BaseModel):
    prompt: str
    max_tokens: int = 2000
    stop: Optional[List[str]] = None
    temperature: float = 0.7


class CompletionResponse(BaseModel):
    completion: str


class SchemaCompletionRequest(CompletionRequest):
    schema_restriction: JsonSchema = None


class SchemaCompletionResponse(BaseModel):
    completion: dict


class CfgCompletionRequest(CompletionRequest):
    cfg: str


class RegexCompletionRequest(CompletionRequest):
    regex: str
