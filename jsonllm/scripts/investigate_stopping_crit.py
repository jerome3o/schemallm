import os
from transformers import AutoModelForCausalLM, AutoTokenizer
import regex
from rellm import complete_re
from parserllm import complete_cf
from pydantic import BaseModel
from lark import Lark
from jsonllm.server.jsonschema2cfg import create_lark_cfg_for_schema

_model = os.environ["MODEL_PATH"]


def test_suite_1(model: AutoModelForCausalLM, tokenizer: AutoTokenizer):
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

    prompt = "You're steve, a 30yo. Tell me about yourself, in JSON format!:\n"

    response = complete_cf(
        prompt=prompt,
        parser=parser,
        partial_completion="",
        tokenizer=tokenizer,
        model=model,
        max_new_tokens=30,
        debug=True,
    )

    print(response)
    print(response)


def main(model: AutoModelForCausalLM, tokenizer: AutoTokenizer):
    class Details(BaseModel):
        season: str
        temperature_celsius: float

    prompt = "Oh boy, it's cold outside! it must be winter and about 13.51 degrees celsius.\nJSON Object describing environment:\n"

    cfg = create_lark_cfg_for_schema(Details.schema())
    parser = Lark(cfg, start="start", parser="lalr")
    response = complete_cf(
        prompt=prompt,
        parser=parser,
        partial_completion="",
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

    print("loading tokenizer")
    tokenizer = AutoTokenizer.from_pretrained(_model, use_fast=False)
    print("loading model")
    model = AutoModelForCausalLM.from_pretrained(
        _model,
        load_in_8bit=True,
        device_map="auto",
    )

    main(model, tokenizer)
