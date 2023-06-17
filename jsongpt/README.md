# JSONGPT

This is an attempt at making an LLM completion API that allows for submition of a JSON Schema along side your prompt, that forces the result to conform to the schema.

Prior art:
* [ReLLM](https://github.com/r2d4/rellm)
* [ParserLLM](https://github.com/r2d4/parserllm)
* [jsonformer](https://github.com/1rgs/jsonformer)

Potential quick approaches would be to generate a parser for a given JSON schema, and hand that to ParserLLM.
