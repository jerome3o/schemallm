# SchemaLLM

This is an attempt at making an LLM completion API that allows for the submission of a JSONSchema (and eventually other schema languages) along side your prompt, and reliably returns a result that conforms to the schema.

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

### Completion functions
### Server
### HTTP Client
### LangChain Client

Prior art:
* [ReLLM](https://github.com/r2d4/rellm)
* [ParserLLM](https://github.com/r2d4/parserllm)
* [jsonformer](https://github.com/1rgs/jsonformer)
