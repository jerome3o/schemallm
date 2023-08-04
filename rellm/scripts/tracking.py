import regex
from pathlib import Path

from jsonllm.server.load_model import load_model, load_tokenizer
from rellm.rellm import complete_re
from rellm.logit_tracker import LogitTracker


def main():
    model = load_model("gpt2")
    tokenizer = load_tokenizer("gpt2")

    email_address_regex = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    pattern_list = [regex.compile(email_address_regex)]

    tracker = LogitTracker(
        patterns=[p.pattern for p in pattern_list],
        token_to_index=tokenizer.get_vocab(),
        index_to_token={v: k for k, v in tokenizer.get_vocab().items()},
    )

    result = complete_re(
        "My name is Jerome Swannack, I work at coolcompany.com and my email address is ",
        pattern=pattern_list,
        tokenizer=tokenizer,
        model=model,
        max_new_tokens=30,
        debug=True,
        tracker=tracker,
    )

    (Path("outputs") / "tracker_script_result.json").write_text(tracker.json(indent=4))


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    main()
