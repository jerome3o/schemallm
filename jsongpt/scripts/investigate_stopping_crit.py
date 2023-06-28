import os
from transformers import AutoModelForCausalLM, AutoTokenizer
import regex
from rellm import complete_re

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
    print(response)


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    main()
