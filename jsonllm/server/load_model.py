import os
from transformers import AutoModelForCausalLM, AutoTokenizer

_model = os.environ["MODEL_PATH"]

# TODO(j.swannack): These seem pointless, should remove or improve later
def load_tokenizer():
    print("loading tokenizer")
    return AutoTokenizer.from_pretrained(_model, use_fast=False)


def load_model():
    print("loading model")
    return AutoModelForCausalLM.from_pretrained(
        _model,
        load_in_8bit=True,
        device_map="auto",
    )
