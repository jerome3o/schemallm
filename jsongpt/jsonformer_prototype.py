import os
from typing import List

from jsonformer import Jsonformer
from transformers import AutoModelForCausalLM, AutoTokenizer
from pydantic import BaseModel

_model = os.environ["MODEL_PATH"]


class PersonDetails(BaseModel):
    name: str
    email: str
    nicknames: List[str]


def main():
    tokenizer = AutoTokenizer.from_pretrained(_model)
    model = AutoModelForCausalLM.from_pretrained(model=_model, load_in_8bit=True, device_map="auto")

    schema = PersonDetails.schema()

    prompt = (
        "My name is jerome - email is jeromeswannack@gmail.com, and my friends call me j-dog"
        ", but you can call me steve\nJSON object of the above information:\n"
    )

    jsonformer = Jsonformer(model, tokenizer, schema, prompt)
    result = jsonformer()
    print(result)



if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO)
    main()
