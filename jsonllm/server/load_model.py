import os
from transformers import AutoModelForCausalLM, AutoTokenizer

_model = os.environ["MODEL_PATH"]


def load_model():
    print("loading tokenizer")
    tokenizer = AutoTokenizer.from_pretrained(_model, use_fast=False)
    print("loading model")
    model = AutoModelForCausalLM.from_pretrained(
        _model,
        load_in_8bit=True,
        device_map="auto",
    )
    return model, tokenizer
