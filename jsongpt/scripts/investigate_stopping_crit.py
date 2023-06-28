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

    prompt = "Repeat after me: 14 is the best number.\nResonse:"
    response = complete_re(
        prompt, regex.compile("\d+"), tokenizer=tokenizer, model=model, max_tokens=20
    )
    print(response)
    print(response)


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    main()
