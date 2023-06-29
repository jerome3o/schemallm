import os
from transformers import AutoModelForCausalLM, AutoTokenizer
import regex
from rellm import complete_re
from parserllm import complete_cf
from pydantic import BaseModel
from lark import Lark
from jsongpt.server.jsonschema2cfg import create_lark_cfg_for_schema

_model = os.environ["MODEL_PATH"]


def main():
    pass

    print("loading tokenizer")
    tokenizer = AutoTokenizer.from_pretrained(_model, use_fast=False)
    print("loading model")
    model = AutoModelForCausalLM.from_pretrained(
        _model,
        load_in_8bit=True,
        device_map="auto",
    )

    prompt = "Repeat after me: 14.000 is the best number.\nResonse:"
    response = complete_re(
        prompt,
        regex.compile(r"\d+\.0\d+{4, 7}"),
        tokenizer=tokenizer,
        model=model,
        max_new_tokens=3,
        debug=True,
    )
    print(response)

    class PersonalDetails(BaseModel):
        name: str
        age: int
        location: str

    cfg = create_lark_cfg_for_schema(PersonalDetails.schema())
    parser = Lark(cfg, start="start", parser="lalr")

    prompt = "Tell me about yourself, in JSON format!:\n"

    response = complete_cf(
        prompt=prompt,
        parser=parser,
        partial_completion=prompt,
        tokenizer=tokenizer,
        model=model,
        max_new_tokens=30,
        debug=True,
    )

    print(response)
    print(response)


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    main()
