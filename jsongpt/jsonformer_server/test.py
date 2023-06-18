import requests
from pydantic import BaseModel


from models import SchemaCompletionRequest


class Details(BaseModel):
    season: str
    temperature_celsius: float


def main():
    prompt = (
        "Oh boy, it's cold outside! it must be winter and about 13 degrees celsius."
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


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    main()
