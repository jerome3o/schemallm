import requests
from typing import List
from pydantic import BaseModel


from models import SchemaCompletionRequest


class PersonDetails(BaseModel):
    name: str
    email: str
    nicknames: List[str]


def main():
    prompt = (
        "My name is jerome - email is jeromeswannack@gmail.com, and my friends call me j-dog"
        ", but you can call me steve\nJSON object of the above information:\n"
    )
    request = SchemaCompletionRequest(
        prompt="My name is jerome - email is ",
        max_tokens=2000,
        schema_restriction=PersonDetails.schema(),
    )

    resp = requests.post(
        "http://localhost:8000/v1/completion/with-schema", json=request.dict()
    )
    print(resp.json())


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    main()
