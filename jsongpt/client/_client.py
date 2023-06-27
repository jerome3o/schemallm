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
    DEFAULT_MAX_TOKENS,
    DEFAULT_TEMPERATURE,
)

T = TypeVar("T", bound=BaseModel)

# TODO(j.swannack): find a way to reduce duplication of arguments so it's easier to change the
# request/response models


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
        prompt: str,
        max_tokens: int = DEFAULT_MAX_TOKENS,
        temperature: float = DEFAULT_TEMPERATURE,
        stop: list[str] = None,
    ) -> CompletionResponse:
        request = CompletionRequest(
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temperature,
            stop=stop,
        )
        return self._request(
            "/v1/completion/standard",
            request,
            CompletionResponse,
        )

    def completion_with_cfg(
        self,
        prompt: str,
        cfg: str,
        max_tokens: int = DEFAULT_MAX_TOKENS,
        temperature: float = DEFAULT_TEMPERATURE,
        stop: list[str] = None,
    ) -> CfgCompletionResponse:
        request = CfgCompletionRequest(
            prompt=prompt,
            cfg=cfg,
            max_tokens=max_tokens,
            temperature=temperature,
            stop=stop,
        )
        return self._request(
            "/v1/completion/with-cfg",
            request,
            CfgCompletionResponse,
        )

    def completion_with_schema(
        self,
        prompt: str,
        schema: dict,
        max_tokens: int = DEFAULT_MAX_TOKENS,
        temperature: float = DEFAULT_TEMPERATURE,
        stop: list[str] = None,
    ) -> SchemaCompletionResponse:
        request = SchemaCompletionRequest(
            prompt=prompt,
            schema=schema,
            max_tokens=max_tokens,
            temperature=temperature,
            stop=stop,
        )
        return self._request(
            "/v1/completion/with-schema",
            request,
            SchemaCompletionResponse,
        )

    def completion_with_regex(
        self,
        prompt: str,
        pattern: str,
        max_tokens: int = DEFAULT_MAX_TOKENS,
        temperature: float = DEFAULT_TEMPERATURE,
        stop: list[str] = None,
    ) -> RegexCompletionResponse:
        request = RegexCompletionRequest(
            prompt=prompt,
            regex=pattern,
            max_tokens=max_tokens,
            temperature=temperature,
            stop=stop,
        )
        return self._request(
            "/v1/completion/with-regex",
            request,
            RegexCompletionResponse,
        )

    def completion_with_pydantic(
        self,
        prompt: str,
        model: Type[BaseModel],
        max_tokens: int = DEFAULT_MAX_TOKENS,
        temperature: float = DEFAULT_TEMPERATURE,
        stop: list[str] = None,
    ) -> CompletionResponse:
        # TODO(j.swannack): add in other generation options somehow
        resp = self.completion_with_schema(
            prompt=prompt,
            schema=model.schema(),
            max_tokens=max_tokens,
            temperature=temperature,
            stop=stop,
        )
        return model.parse_obj(resp.completion)
