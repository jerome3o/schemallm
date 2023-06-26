from pydantic import BaseModel
from jsongpt.models.api import (
    CompletionRequest,
    CompletionResponse,
    CfgCompletionRequest,
    CfgCompletionResponse,
    RegexCompletionRequest,
    RegexCompletionResponse,
    SchemaCompletionRequest,
    SchemaCompletionResponse,
)


class JsonGptClient(BaseModel):
    base_url: str = "http://localhost:8000"

    def completion(
        self,
        request: CompletionRequest,
    ) -> CompletionResponse:
        raise NotImplementedError

    def completion_with_cfg(
        self,
        request: CfgCompletionRequest,
    ) -> CfgCompletionResponse:
        raise NotImplementedError

    def completion_with_schema(
        self,
        request: SchemaCompletionRequest,
    ) -> SchemaCompletionResponse:
        raise NotImplementedError

    def completion_with_regex(
        self,
        request: RegexCompletionRequest,
    ) -> RegexCompletionResponse:
        raise NotImplementedError
