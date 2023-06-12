import os

from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

_openai_api_base = os.environ["OPENAI_API_BASE"]
_model = "vicuna-13b-v1.1-8bit"


def get_llm() -> OpenAI:
    return OpenAI(
        temperature=0,
        openai_api_base=_openai_api_base,
        openai_api_key="no",
        model=_model,
    )


def get_llm_chat() -> ChatOpenAI:
    return ChatOpenAI(
        temperature=0,
        openai_api_base=_openai_api_base,
        openai_api_key="no",
        model=_model,
    )
