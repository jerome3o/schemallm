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
    StoppingCriteriaList,
    StoppingCriteria,
)

from jsonllm.server.load_model import load_model, load_tokenizer
from jsonllm.server.jsonschema2cfg import create_lark_cfg_for_schema
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


class StopOnTokens(StoppingCriteria):
    def __init__(self, stop_ids: list):
        self.stop_ids = stop_ids
        super().__init__()

    def __call__(
        self,
        input_ids: torch.LongTensor,
        scores: torch.FloatTensor,
        **kwargs,
    ) -> bool:
        stop_ids = self.stop_ids
        for stop_id in stop_ids:
            if input_ids[0][-1] == stop_id:
                return True
        return False


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


# TODO(j.swannack): move inference code to a separate module
@torch.inference_mode()
def complete_standard(
    model: AutoModelForCausalLM,
    tokenizer: AutoTokenizer,
    completion_request: CompletionRequest,
) -> CompletionResponse:
    # TODO(j.swannack): Add proper stop logic
    stop_token_list = [1, 2]
    input_ids = tokenizer.encode(completion_request.prompt, return_tensors="pt").to(model.device)
    all_tokens = model.generate(
        input_ids,
        # TODO(j.swannack): move validation to pydantic model
        temperature=max(min(completion_request.temperature, 1.0), 0.0),
        max_new_tokens=completion_request.max_tokens,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
        stopping_criteria=StoppingCriteriaList([StopOnTokens(stop_ids=stop_token_list)]),
    )

    tokens = all_tokens[0].tolist()

    # remove input tokens
    tokens = tokens[len(input_ids[0]) :]

    # remove end tokens
    if tokens[-1] in stop_token_list:
        tokens = tokens[:-1]

    # add more outputs if needed
    return CompletionResponse(completion=tokenizer.decode(tokens, skip_special_tokens=True))


if __name__ == "__main__":
    import logging
    import uvicorn

    logging.basicConfig(level=logging.INFO)

    uvicorn.run(app, host="0.0.0.0", port=8000)
