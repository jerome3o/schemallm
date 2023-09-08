import pytest
from schemallm.server.load_model import load_model, load_tokenizer


@pytest.fixture(scope="module")
def model():
    return load_model("gpt2")


@pytest.fixture(scope="module")
def tokenizer():
    return load_tokenizer("gpt2")
