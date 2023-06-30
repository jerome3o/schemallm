# Following along here:
# https://python.langchain.com/docs/modules/model_io/models/llms/how_to/custom_llm

from typing import Any, List, Mapping, Optional

from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.llms.base import LLM

from jsonllm.models.jsonschema import JsonSchema, parse_json_schema
from jsonllm.client.http_api import JsonLlmClient, DEFAULT_BASE_URL


class JsonSchemaLLM(LLM):
    schema_restriction: JsonSchema

    base_url: str = DEFAULT_BASE_URL
    api_client: JsonLlmClient = None

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.api_client = JsonLlmClient(base_url=self.base_url)

    @property
    def _llm_type(self) -> str:
        return "jsonllm_json_schema"

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
    ) -> str:
        if stop is not None:
            raise ValueError("stop kwargs are not permitted.")
        return prompt[: self.n]

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {
            "schema_restriction": self.schema_restriction.dict(),
            "base_url": self.base_url,
        }


def main():
    from pydantic import BaseModel

    class PersonalDetails(BaseModel):
        name: str
        age: int
        location: str

    # TODO(j.swannack): make this more succinct, allow input of pydantic model?
    llm = JsonSchemaLLM(schema_restriction=parse_json_schema(PersonalDetails.schema()))
    print(llm)


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    main()
