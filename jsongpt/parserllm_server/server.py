import json
import os

from fastapi import FastAPI
from lark import Lark
from parserllm import complete_cf
from transformers import AutoModelForCausalLM, AutoTokenizer

from jsongpt.parserllm_server.jsonschema2cfg import create_lark_cfg_for_schema
from jsongpt.models.api import (
    CompletionRequest,
    CompletionResponse,
    SchemaCompletionRequest,
    SchemaCompletionResponse,
)

app = FastAPI()


_model = os.environ["MODEL_PATH"]


@app.post("/v1/completion/with-schema", response_model=SchemaCompletionResponse)
def completion(r: SchemaCompletionRequest):
    # TODO(j.swannack): cache parsers?
    cfg = create_lark_cfg_for_schema(r.schema_restriction)
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
                prompt=r.prompt,
                parser=parser,
                partial_completion="",
                tokenizer=tokenizer,
                model=model,
                max_new_tokens=r.max_tokens,
                debug=True,
            )
        )
    )


@app.post("/v1/completion/standard", response_model=CompletionResponse)
def completion(r: CompletionRequest):
    return SchemaCompletionResponse(completion=complete_standard(model, r))


def complete_standard(model, completion_request: CompletionRequest) -> str:
    # TODO(j.swannack): Add normal generation here
    print(model)
    pass


print("loading tokenizer")
tokenizer = AutoTokenizer.from_pretrained(_model, use_fast=False)
print("loading model")
model = AutoModelForCausalLM.from_pretrained(
    _model,
    load_in_8bit=True,
    device_map="auto",
)

if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)

    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
