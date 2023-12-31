import os

from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from jsonllm.client.langchain_client import StandardLLM

_openai_api_base = os.environ.get("OPENAI_API_BASE", None)
_openai_api_key = os.environ.get("OPENAI_API_KEY", None)
_model = "vicuna-13b-v1.1-8bit"
# TODO(j.swannack): Add os env var for jsonllm url


def get_llm() -> OpenAI:
    # return OpenAI(
    #     temperature=0,
    #     openai_api_base=_openai_api_base,
    #     openai_api_key="no",
    #     model=_model,
    # )
    return StandardLLM()


def get_llm_chat() -> ChatOpenAI:
    return ChatOpenAI(
        temperature=0,
        openai_api_base=_openai_api_base,
        openai_api_key="no",
        model=_model,
    )


def get_llm_chat_open_ai() -> ChatOpenAI:
    return ChatOpenAI(
        temperature=0,
        openai_api_base="https://api.openai.com/v1",
        openai_api_key=_openai_api_key,
        model="gpt-4",
    )
