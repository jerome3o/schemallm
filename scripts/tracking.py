from typing import List
from pathlib import Path

import regex
from pydantic import BaseModel

from lark import Lark
import numpy as np

from jsonllm.server.load_model import load_model, load_tokenizer
from rellm.rellm import complete_re
from rellm.logit_tracker import LogitTracker
from parserllm.logit_tracker import LogitTrackerParserLLM
from parserllm import complete_cf


class InfoGraphicStep(BaseModel):
    partial_completion: str
    selected_token: str
    patterns: List[str]

    tokens: List[str]
    probabilities: List[float]
    mask: List[bool]


class InfoGraphicData(BaseModel):
    prompt: str
    pattern: str

    steps: List[InfoGraphicStep]


def re_logit_tracking():
    model = load_model("gpt2")
    tokenizer = load_tokenizer("gpt2")

    email_address_regex = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+[a-zA-Z0-9]"
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


def parser_logit_tracking():
    model = load_model("gpt2")
    tokenizer = load_tokenizer("gpt2")

    cfg = r"""\
BOOLEAN_VALUE: "true" | "false"
NULL: "null"
SIGNED_NUMBER: /-?\d+(\.\d{1,2})?/

?start: root
root_name: root_name_key ":" root_name_value
root_name_key: "\"name\""
root_name_value: ESCAPED_STRING
root_age: root_age_key ":" root_age_value
root_age_key: "\"age\""
root_age_value: SIGNED_INT
root_location: root_location_key ":" root_location_value
root_location_key: "\"location\""
root_location_value: ESCAPED_STRING
root: "{" root_name "," root_age "," root_location "}"


%import common.ESCAPED_STRING
%import common.WS_INLINE
%import common.WS
%import common.SIGNED_INT
%ignore WS_INLINE
%ignore WS
"""

    prompt = """\
bio: Lisa is a 23 year old woman, from london!
data: {"name": "Lisa", "age": 27, "location": "London"}


bio: John's a New Yorker, he just celebrated his half century birthday.
data: {"name": "John", "age": 50, "location": "New York"}

bio: Jerome is from New Zealand, and he's 27
data: """

    tracker = LogitTrackerParserLLM(cfg=cfg, prompt=prompt)
    parser = Lark(
        cfg,
        parser="lalr",
        lexer="basic",
        propagate_positions=True,
        maybe_placeholders=False,
        regex=True,
    )

    result = complete_cf(
        prompt=prompt,
        partial_completion="",
        parser=parser,
        tokenizer=tokenizer,
        model=model,
        max_new_tokens=50,
        debug=True,
        tracker=tracker,
    )

    print(result)
    (Path("outputs") / "tracker_script_result_parser.json").write_text(
        tracker.json(indent=4)
    )


def convert_tracker_to_infographic(tracker: LogitTrackerParserLLM) -> InfoGraphicData:
    infographic_steps = []

    current_completion = ""
    for re_tracker in tracker.re_steps:
        if not re_tracker.steps:
            current_completion += re_tracker.result
            infographic_steps.append(
                InfoGraphicStep(
                    partial_completion=current_completion,
                    selected_token=re_tracker.result,
                    patterns=re_tracker.patterns,
                    tokens=[],
                    probabilities=[],
                    mask=[],
                )
            )
            continue

        for re_i, step in enumerate(re_tracker.steps):
            logits = np.array(step.logits_raw)
            probabilities = np.exp(logits) / np.sum(np.exp(logits))

            mask = np.zeros_like(step.logits_raw)
            mask[step.allowed_ids] = 1

            sorted_indices = np.argsort(probabilities)
            top_100 = sorted_indices[:-100:-1]

            infographic_steps.append(
                InfoGraphicStep(
                    partial_completion=current_completion
                    + "".join(re_tracker.result_tokens[:re_i]),
                    selected_token=re_tracker.result_tokens[re_i],
                    patterns=re_tracker.patterns,
                    tokens=[re_tracker.index_to_token[i] for i in top_100],
                    probabilities=probabilities[top_100].tolist(),
                    mask=mask[top_100].tolist(),
                )
            )

        current_completion += re_tracker.result

    return InfoGraphicData(
        prompt=tracker.prompt,
        pattern=tracker.cfg,
        steps=infographic_steps,
    )


def generate_infographic_data():
    print("Loading tracker data")
    tracker = LogitTrackerParserLLM.parse_file(
        Path("outputs") / "tracker_script_result_parser.json"
    )
    print("Loaded tracker data")

    infographic_data = convert_tracker_to_infographic(tracker)

    (Path("outputs") / "infographic_data.json").write_text(
        infographic_data.json(indent=4)
    )
    print(infographic_data)


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)

    re_logit_tracking()
    parser_logit_tracking()
    generate_infographic_data()
