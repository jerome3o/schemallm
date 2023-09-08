from schemallm.client import JsonLlmClient
from pydantic import BaseModel


def main():
    client = JsonLlmClient()
    print(client.completion_standard("Hello, world!", max_tokens=10))

    class PersonalDetails(BaseModel):
        name: str
        age: int
        location: str

    print(
        client.completion_with_pydantic(
            "Tell me about yourself, in JSON format!:\n",
            model=PersonalDetails,
        )
    )


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    main()
