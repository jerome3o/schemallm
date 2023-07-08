import json
import os
from typing import Annotated

import regex
import torch
from fastapi import FastAPI, Depends
from lark import Lark
from parserllm import complete_cf
from rellm import complete_re
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
)

from jsonllm.server.load_model import load_model, load_tokenizer
from jsonllm.server.jsonschema2cfg import create_lark_cfg_for_schema
from jsonllm.server.standard_completion import complete_standard
from jsonllm.models.api import (
    CompletionRequest,
    CompletionResponse,
    SchemaCompletionRequest,
    SchemaCompletionResponse,
    CfgCompletionRequest,
    CfgCompletionResponse,
    RegexCompletionRequest,
    RegexCompletionResponse,
)

app = FastAPI(
    title="JsonLLM",
    description="An API for generating structured output from LLMs",
)

# Add streaming endpoints for all of these
# https://fastapi.tiangolo.com/advanced/custom-response/
# https://github.com/lm-sys/FastChat/blob/1af93d75aa6e43b13fa0170127456e8205ef6f34/fastchat/serve/model_worker.py#L357
# This is a nice to have, but would be really cool to see the completion as it's being generated
# conforming to the schema

_model = os.environ["MODEL_PATH"]


def get_model() -> AutoModelForCausalLM:
    return load_model(_model)


def get_tokenizer() -> AutoTokenizer:
    return load_tokenizer(_model)


# TODO(j.swannack): Use Depends for the model and tokeniser


@app.post("/v1/completion/with-cfg", response_model=CfgCompletionResponse)
def cfg_endpoint(
    r: CfgCompletionRequest,
    model: Annotated[AutoModelForCausalLM, Depends(get_model)],
    tokenizer: Annotated[AutoTokenizer, Depends(get_tokenizer)],
):
    return complete_with_cfg(model, tokenizer, r)


@app.post("/v1/completion/with-schema", response_model=SchemaCompletionResponse)
def schema_endpoint(
    r: SchemaCompletionRequest,
    model: Annotated[AutoModelForCausalLM, Depends(get_model)],
    tokenizer: Annotated[AutoTokenizer, Depends(get_tokenizer)],
):
    return complete_with_schema(model, tokenizer, r)


@app.post("/v1/completion/with-regex", response_model=RegexCompletionResponse)
def regex_endpoint(
    r: RegexCompletionRequest,
    model: Annotated[AutoModelForCausalLM, Depends(get_model)],
    tokenizer: Annotated[AutoTokenizer, Depends(get_tokenizer)],
):
    return complete_with_regex(model, tokenizer, r)


@app.post("/v1/completion/standard", response_model=CompletionResponse)
def standard_endpoint(
    r: CompletionRequest,
    model: Annotated[AutoModelForCausalLM, Depends(get_model)],
    tokenizer: Annotated[AutoTokenizer, Depends(get_tokenizer)],
):
    return complete_standard(model, tokenizer, r)


@torch.inference_mode()
def complete_with_cfg(
    model: AutoModelForCausalLM,
    tokenizer: AutoTokenizer,
    completion_request: CfgCompletionRequest,
) -> CompletionResponse:
    parser = Lark(
        completion_request.cfg,
        parser="lalr",
        lexer="basic",
        propagate_positions=True,
        maybe_placeholders=False,
        regex=True,
    )
    return CompletionResponse(
        completion=complete_cf(
            prompt=completion_request.prompt,
            parser=parser,
            partial_completion="",
            tokenizer=tokenizer,
            model=model,
            max_new_tokens=completion_request.max_tokens,
            debug=True,
        )
    )


@torch.inference_mode()
def complete_with_schema(
    model: AutoModelForCausalLM,
    tokenizer: AutoTokenizer,
    completion_request: SchemaCompletionRequest,
) -> SchemaCompletionResponse:
    cfg = create_lark_cfg_for_schema(completion_request.schema_restriction)
    # TODO(j.swannack): cache parsers?
    parser = Lark(
        cfg,
        parser="lalr",
        lexer="basic",
        propagate_positions=True,
        maybe_placeholders=False,
        regex=True,
    )
    return SchemaCompletionResponse(
        completion=json.loads(
            complete_cf(
                prompt=completion_request.prompt,
                parser=parser,
                partial_completion="",
                tokenizer=tokenizer,
                model=model,
                max_new_tokens=completion_request.max_tokens,
                debug=True,
            )
        )
    )


@torch.inference_mode()
def complete_with_regex(
    model: AutoModelForCausalLM,
    tokenizer: AutoTokenizer,
    completion_request: RegexCompletionRequest,
) -> RegexCompletionResponse:
    return RegexCompletionResponse(
        completion=complete_re(
            prompt=completion_request.prompt,
            pattern=regex.compile(completion_request.regex),
            tokenizer=tokenizer,
            model=model,
            max_new_tokens=completion_request.max_tokens,
            debug=True,
        )
    )


if __name__ == "__main__":
    import logging
    import uvicorn

    logging.basicConfig(level=logging.INFO)

    uvicorn.run(app, host="0.0.0.0", port=8000)
