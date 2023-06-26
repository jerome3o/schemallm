from pydantic import BaseModel
from requests import get
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


# TODO(j.swannack): error handling
class JsonGptClient(BaseModel):
    base_url: str = "http://localhost:8000"

    def completion(
        self,
        request: CompletionRequest,
    ) -> CompletionResponse:
        response = get(
            self.base_url + "/v1/completion/standard",
            json=request.json(),
        )
        return CompletionResponse.parse_obj(response.json())

    def completion_with_cfg(
        self,
        request: CfgCompletionRequest,
    ) -> CfgCompletionResponse:
        response = get(
            self.base_url + "/v1/completion/with-cfg",
            json=request.json(),
        )
        return CfgCompletionResponse.parse_obj(response.json())

    def completion_with_schema(
        self,
        request: SchemaCompletionRequest,
    ) -> SchemaCompletionResponse:
        response = get(
            self.base_url + "/v1/completion/with-schema",
            json=request.json(),
        )
        return SchemaCompletionResponse.parse_obj(response.json())

    def completion_with_regex(
        self,
        request: RegexCompletionRequest,
    ) -> RegexCompletionResponse:
        response = get(
            self.base_url + "/v1/completion/with-regex",
            json=request.json(),
        )
        return RegexCompletionResponse.parse_obj(response.json())
