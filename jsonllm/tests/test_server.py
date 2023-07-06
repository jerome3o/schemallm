import requests
import pytest
from pydantic import BaseModel
from fastapi.testclient import TestClient
import json


from jsonllm.server.server import app as _app
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


@pytest.fixture
def tokenizer(scope="module"):
    return load_tokenizer("gpt2")


@pytest.fixture(scope="module")
def test_app(model, tokenizer):
    app = TestClient(_app)
    app.dependency_overrides[load_model] = lambda: model
    app.dependency_overrides[load_tokenizer] = lambda: tokenizer
    return app


class Details(BaseModel):
    season: str
    temperature_celsius: float


def test_with_schema(test_app, model: model, tokenizer: tokenizer):
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

def test_standard_completion():
    prompt = "Favourite colour:\n"
    request = CompletionRequest(
        prompt=prompt,
        max_tokens=10,
    )
    resp = requests.post(
        "http://localhost:8000/v1/completion/standard",
        json=request.dict(),
    )
    print(resp.json())


def test_with_cfg():
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
    resp = requests.post(
        "http://localhost:8000/v1/completion/with-cfg",
        json=request.dict(),
    )
    print(resp.json())


def test_with_number():
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
    resp = requests.post(
        "http://localhost:8000/v1/completion/with-cfg",
        json=request.dict(),
    )
    print(resp.json())


def main():
    # test_with_schema()
    test_standard_completion()
    # test_with_cfg()
    # test_with_number()


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    main()
