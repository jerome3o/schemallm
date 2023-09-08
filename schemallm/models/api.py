from typing import List, Optional
from pydantic import BaseModel

from schemallm.models.jsonschema import JsonSchema

DEFAULT_MAX_TOKENS = 2000
DEFAULT_TEMPERATURE = 0.7


class CompletionRequest(BaseModel):
    prompt: str
    max_tokens: int = DEFAULT_MAX_TOKENS
    temperature: float = DEFAULT_TEMPERATURE
    stop: Optional[List[str]] = None


class CompletionResponse(BaseModel):
    completion: str


class SchemaCompletionRequest(CompletionRequest):
    schema_restriction: JsonSchema = None


class SchemaCompletionResponse(BaseModel):
    completion: dict


class CfgCompletionRequest(CompletionRequest):
    cfg: str


class CfgCompletionResponse(CompletionResponse):
    pass


class RegexCompletionRequest(CompletionRequest):
    regex: str


class RegexCompletionResponse(CompletionResponse):
    pass
