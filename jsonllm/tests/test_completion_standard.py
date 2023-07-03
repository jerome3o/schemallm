from jsonllm.models.api import CompletionRequest
from jsonllm.server.server import complete_standard
from jsonllm.server.load_model import load_model


def main():
    # doesn't tigger the error, must be an async thing.
    model, tokenizer = load_model()
    complete_standard(
        model=model,
        tokenizer=tokenizer,
        completion_request=CompletionRequest(
            prompt="The name of three types of frogs:\n",
            max_tokens=30,
            temperature=0.7,
        ),
    )


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    main()
