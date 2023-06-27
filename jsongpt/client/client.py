from typing import Type, TypeVar
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

T = TypeVar("T", bound=BaseModel)


class JsonGptClient(BaseModel):
    base_url: str = "http://localhost:8000"

    def _request(
        self,
        endpoint: str,
        request: BaseModel,
        response_model: Type[T],
    ) -> T:
        response = get(
            self.base_url + endpoint,
            json=request.json(),
        )
        # TODO(j.swannack): error handling
        return response_model.parse_obj(response.json())

    def completion(
        self,
        request: CompletionRequest,
    ) -> CompletionResponse:
        return self._request(
            "/v1/completion/standard",
            request,
            CompletionResponse,
        )

    def completion_with_cfg(
        self,
        request: CfgCompletionRequest,
    ) -> CfgCompletionResponse:
        return self._request(
            "/v1/completion/with-cfg",
            request,
            CfgCompletionResponse,
        )

    def completion_with_schema(
        self,
        request: SchemaCompletionRequest,
    ) -> SchemaCompletionResponse:
        return self._request(
            "/v1/completion/with-schema",
            request,
            SchemaCompletionResponse,
        )

    def completion_with_regex(
        self,
        request: RegexCompletionRequest,
    ) -> RegexCompletionResponse:
        return self._request(
            "/v1/completion/with-regex",
            request,
            RegexCompletionResponse,
        )

    def completion_with_pydantic(
        self,
        prompt: str,
        model: Type[BaseModel],
    ) -> CompletionResponse:
        # TODO(j.swannack): add in other generation options somehow
        resp = self.completion_with_schema(
            SchemaCompletionRequest(
                prompt=prompt,
                schema=model.schema(),
            )
        )
        return model.parse_obj(resp.completion)
