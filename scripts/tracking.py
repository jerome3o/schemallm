import regex
from pathlib import Path
from pydantic import BaseModel

from lark import Lark

from jsonllm.server.load_model import load_model, load_tokenizer
from rellm.rellm import complete_re
from rellm.logit_tracker import LogitTracker
from parserllm.logit_tracker import LogitTrackerParserLLM
from parserllm import complete_cf


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

    tracker = LogitTrackerParserLLM(cfg=cfg)
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
    (Path("outputs") / "tracker_script_result_parser.json").write_text(tracker.json(indent=4))


def convert_to_ui_ready_obj(tracker: LogitTrackerParserLLM):
    pass

if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    parser_logit_tracking()
