import os

from langchain.llms import OpenAI

_openai_api_base = os.environ["OPENAI_API_BASE"]
_model = "vicuna-13b-v1.1-8bit"


def get_llm() -> OpenAI:
    return OpenAI(
        temperature=0,
        openai_api_base=_openai_api_base,
        openai_api_key="no",
        model=_model,
    )
