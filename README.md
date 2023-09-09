# SchemaLLM

This is an attempt at making an LLM completion API that allows for the submission of a JSONSchema (and eventually other schema languages) along side your prompt, and reliably returns a result that conforms to the schema.

See the accompanying [blog post](https://www.jeromeswannack.com/projects/2023/06/30/jsonllm.html) for more context :)

## Overview

This repo contains:
* Functions for guiding LLM completion to comply with:
  * JSONSchema
  * Context free grammars
  * Regular expressions
* A server that exposes these functions over HTTP
* A python (requests based) client that can be used to interact with the server
* A LangChain client implementing the LLM object
* Two vendored dependencies with some modifications:
    * [ReLLM](https://github.com/r2d4/rellm) in `schemallm/vendored/rellm`
    * [ParserLLM](https://github.com/r2d4/parserllm) in `schemallm/vendored/parserllm`

## Installation

TODO: bundle this up for pypi

## Usage

These are pretty early days, so the API is likely to change a lot. The following is a rough overview of how it currently stands.

All `model` and `tokenizer` objects are from the huggingface transformers library, and can be loaded here using:

```python
from schemallm.server.load_model import load_model, load_tokenizer

model = load_model("gpt2")
tokenizer = load_tokenizer("gpt2")
```

### Completion functions

#### Regex

`complete_with_regex` is a function that takes a prompt and a regular expression, and returns a completion that conforms to that regex

Leverages [ReLLM](https://github.com/r2d4/rellm), but with some slight modifications, details in my [blog post](https://www.jeromeswannack.com/projects/2023/06/30/jsonllm.html).

```python
from schemallm.models.api import RegexCompletionRequest
from schemallm.server.server import complete_with_regex


result = complete_with_regex(
    model=model,
    tokenizer=tokenizer,
    completion_request=RegexCompletionRequest(
        prompt="An integer between 4 and 8: ",
        regex="[4-8]",
    ),
)
```

#### CFG

`complete_with_cfg` is a function that takes a prompt and a context free grammar, and returns a completion that conforms to the grammar

Leverages [ParserLLM](https://github.com/r2d4/parserllm), but with some slight modifications, details in my [blog post](https://www.jeromeswannack.com/projects/2023/06/30/jsonllm.html).

```python
from schemallm.models.api import CfgCompletionRequest
from schemallm.server.server import complete_with_cfg

JSON_CFG = """
JSON := OBJECT | ARRAY
OBJECT := '{' PAIRLIST? '}'
PAIRLIST := PAIR (',' PAIR)*
PAIR := STRING ':' VALUE
VALUE := STRING | NUMBER | OBJECT | ARRAY | 'true' | 'false' | 'null'
ARRAY := '[' VALUELIST? ']'
VALUELIST := VALUE(',' VALUE)*
STRING := '"' [a-z, A-Z, 0-9]* '"'
NUMBER := [0-9]+
"""

result = complete_with_cfg(
    model=model,
    tokenizer=tokenizer,
    completion_request=CfgCompletionRequest(
        prompt="A JSON object with a key called 'foo' and a string value: ",
        cfg=JSON_CFG,
        max_tokens=300,
    ),
)
```

#### JSONSchema

`complete_with_schema` is a function that takes a prompt and a JSONSchema, and returns a completion that conforms to the schema.

We leverage pydantic to create the schema for us.

```python

from pydantic import BaseModel
from schemallm.models.api import SchemaCompletionRequest
from schemallm.server.server import complete_with_schema


class PersonalDetails(BaseModel):
    name: str
    age: int
    location: str


schema = PersonalDetails.schema()

result = complete_with_schema(
    model=model,
    tokenizer=tokenizer,
    completion_request=SchemaCompletionRequest(
        prompt="A JSON object with a name, age and location: ",
        schema=schema_restriction,
        max_tokens=300,
    ),
)
```

### Server

You can run the inference server with:

```bash
python -m schemallm.server.server
```

You will need some environment variables set:

```bash
export MODEL_PATH=gpt-2
```

This can also point to other huggingface paths.

Now navigate to http://localhost:8000/docs to see the openapi docs for the server.

### HTTP Client

```python

from schemallm.client import SchemaLlmClient
from pydantic import BaseModel

client = SchemaLlmClient()

class PersonalDetails(BaseModel):
    name: str
    age: int
    location: str

print(
    client.completion_with_pydantic(
        "Tell me about yourself, in JSON format!:\n",
        model=PersonalDetails,
    )
)
```

### LangChain Client

Prior art:
* [ReLLM](https://github.com/r2d4/rellm)
* [ParserLLM](https://github.com/r2d4/parserllm)
* [jsonformer](https://github.com/1rgs/jsonformer)
