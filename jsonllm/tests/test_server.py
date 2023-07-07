import requests
import pytest
from pydantic import BaseModel
from fastapi.testclient import TestClient
import json


from jsonllm.server.server import app as _app, get_model, get_tokenizer
from jsonllm.models.api import (
    SchemaCompletionRequest,
    CompletionRequest,
    CfgCompletionRequest,
)

from fastapi.testclient import TestClient
from jsonllm.server.load_model import load_model, load_tokenizer


@pytest.fixture(scope="module")
def model():
    return load_model("gpt2")


@pytest.fixture(scope="module")
def tokenizer():
    return load_tokenizer("gpt2")


@pytest.fixture(scope="module")
def test_app(model, tokenizer):
    _app.dependency_overrides[get_model] = lambda: model
    _app.dependency_overrides[get_tokenizer] = lambda: tokenizer
    app = TestClient(_app)
    return app


class Details(BaseModel):
    season: str
    temperature_celsius: float


def test_with_schema(test_app):
    prompt = "Oh boy, it's cold outside! it must be winter and about 13.51 degrees celsius.\nJSON Object describing environment:\n"
    request = SchemaCompletionRequest(
        prompt=prompt,
        max_tokens=2000,
        schema_restriction=json.loads(Details.schema_json()),
    )
    result = test_app.post(
        "/v1/completion/with-schema",
        json=request.dict(),
    )
    print(result)


def test_standard_completion(test_app):
    prompt = "Favourite colour:\n"
    request = CompletionRequest(
        prompt=prompt,
        max_tokens=10,
    )
    resp = test_app.post(
        "/v1/completion/standard",
        json=request.dict(),
    )
    print(resp.json())


def test_with_cfg(test_app):
    prompt = "Favourite colour:\n"

    cfg = """
    start: value
    value: "red" | "green" | "blue"
    """

    request = CfgCompletionRequest(
        prompt=prompt,
        cfg=cfg,
        max_tokens=10,
    )
    resp = test_app.post(
        "http://localhost:8000/v1/completion/with-cfg",
        json=request.dict(),
    )
    print(resp.json())


def test_with_number(test_app):
    prompt = "Repeat after me: 13.512\nReponse: "

    cfg = """
    %import common.NUMBER
    start: value
    value: NUMBER
    """

    request = CfgCompletionRequest(
        prompt=prompt,
        cfg=cfg,
        max_tokens=10,
    )
    resp = test_app.post(
        "http://localhost:8000/v1/completion/with-cfg",
        json=request.dict(),
    )
    print(resp.json())
