import os
from transformers import AutoModelForCausalLM, AutoTokenizer

_model = os.environ["MODEL_PATH"]

# TODO(j.swannack): These seem pointless, should remove or improve later
def load_tokenizer(model: str = None):
    model = model or _model
    print("loading tokenizer")
    return AutoTokenizer.from_pretrained(
        model, 
        use_fast=False,
    )


def load_model(model: str = None):
    model = model or _model
    print("loading model")
    return AutoModelForCausalLM.from_pretrained(
        model,
        load_in_8bit=True,
        device_map="auto",
    )
