import os

from jsonformer import Jsonformer
from transformers import AutoModelForCausalLM, AutoTokenizer

from fastapi import FastAPI

from models import (
    CompletionRequest,
    CompletionResponse,
    SchemaCompletionRequest,
    SchemaCompletionResponse,
)


app = FastAPI()


_model = os.environ["MODEL_PATH"]


@app.post("/v1/completion/with-schema", response_model=CompletionResponse)
def completion(r: SchemaCompletionRequest):
    if r.schema_restriction is not None:
        m = Jsonformer(
            model,
            tokenizer,
            r.schema_restriction,
            prompt=r.prompt,
            max_array_length=100,
            max_number_tokens=100,
            max_string_token_length=1000,
        )
        return SchemaCompletionResponse(completion=m())


@app.post("/v1/completion/standard")
def completion(r: CompletionRequest):
    pass


print("loading tokenizer")
tokenizer = AutoTokenizer.from_pretrained(_model)
print("loading model")
model = AutoModelForCausalLM.from_pretrained(
    _model,
    load_in_8bit=True,
    device_map="auto",
)

if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    print("hey")
