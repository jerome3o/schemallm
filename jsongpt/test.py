import requests
from pydantic import BaseModel


from jsongpt.models.api import SchemaCompletionRequest, CompletionRequest


class Details(BaseModel):
    season: str
    temperature_celsius: float


def test_with_schema():
    prompt = (
        "Oh boy, it's cold outside! it must be winter and about 13.51 degrees celsius.\nJSON Object describing environment:\n"
    )
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
    prompt = "A short story about frogs:\n"
    request = CompletionRequest(
        prompt=prompt,
        max_tokens=2000,
    )
    resp = requests.post(
        "http://localhost:8000/v1/completion/standard",
        json=request.dict(),
    )
    print(resp.json())


def main():
    # test_with_schema()
    test_standard_completion()



if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    main()
