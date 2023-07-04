import requests
from pydantic import BaseModel


from jsonllm.models.api import (
    SchemaCompletionRequest,
    CompletionRequest,
    CfgCompletionRequest,
)

# TODO(j.swannack): Use `from fastapi.testclient import TestClient`
# note it requires httpx

class Details(BaseModel):
    season: str
    temperature_celsius: float


def test_with_schema():
    prompt = "Oh boy, it's cold outside! it must be winter and about 13.51 degrees celsius.\nJSON Object describing environment:\n"
    request = SchemaCompletionRequest(
        prompt=prompt,
        max_tokens=2000,
        schema_restriction=Details.schema(),
    )

    resp = requests.post(
        "http://localhost:8000/v1/completion/with-schema",
        json=request.dict(),
    )
    print(resp.json())


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
