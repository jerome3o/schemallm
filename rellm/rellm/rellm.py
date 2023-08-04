from typing import List

import regex
from transformers import PreTrainedModel, PreTrainedTokenizer

from rellm.logits_mask import LogitsMask
from rellm.re_token_filter import ReTokenFilter
from rellm.logit_tracker import LogitTracker, EndCondition

ESCAPED_CHARS = r"\.*+?{}()[]|^$"


def complete_re(
    prompt: str,
    pattern: regex.Pattern | List[regex.Pattern],
    tokenizer: PreTrainedTokenizer,
    model: PreTrainedModel,
    max_new_tokens: int = 3,
    stop_after_match: bool = True,
    debug: bool = False,
    tracker: LogitTracker = None,
    **model_kwargs,
):
    """
    Complete a prompt with a regex pattern.
    """
    if isinstance(pattern, regex.Pattern):
        pattern = [pattern]

    if len(pattern) == 1 and is_constant_regex(pattern[0].pattern):
        return get_constant_regex_value(pattern[0].pattern)

    gen_tokens = 0
    partial_completion = ""
    prompt_plus_completion = prompt + partial_completion

    # TODO(j.swannack): Allow this to be injected.
    token_filter = ReTokenFilter(tokenizer)

    while gen_tokens < max_new_tokens:
        prompt_token_ids = tokenizer.encode(prompt_plus_completion, return_tensors="pt")
        prompt_length = prompt_token_ids.shape[1]

        allowed_token_ids = token_filter.filter_tokens(partial_completion, pattern)
        if not allowed_token_ids:
            if any([p.match(partial_completion) for p in pattern]):
                return partial_completion

            raise ValueError(
                f"No tokens allowed for completion with pattern {pattern} and partial "
                f"completion {partial_completion}"
            )
        custom_mask_processor = LogitsMask(allowed_token_ids, tracker=tracker)

        output_ids = model.generate(
            prompt_token_ids.to(model.device),
            max_new_tokens=1,
            pad_token_id=tokenizer.eos_token_id,
            logits_processor=[custom_mask_processor],
            **model_kwargs,
        )
        new_token_ids = output_ids[0, prompt_length:].to("cpu")
        output_text = tokenizer.decode(new_token_ids, skip_special_tokens=True)
        previous_partial_completion = partial_completion
        partial_completion += output_text
        prompt_plus_completion = prompt_plus_completion + output_text
        if debug:
            print("step={} completion={}".format(gen_tokens, partial_completion))

        if tracker:
            tracker.result_tokens.append(output_text)

        # TODO(j.swannack): refactor
        if stop_after_match:
            for p in pattern:
                m = p.match(partial_completion)
                if m:
                    if m.start() == 0 and m.end() < (len(partial_completion) - 5):
                        if tracker:
                            tracker.end_condition = EndCondition.TOKEN_LOOKAHEAD
                            tracker.result = m[0]

                        return m[0]
                    if previous_partial_completion == partial_completion:
                        if tracker:
                            tracker.end_condition = EndCondition.REPEAT
                            tracker.result = m[0]

                        return m[0]

        gen_tokens += 1

    if tracker:
        tracker.end_condition = EndCondition.MAX_TOKENS
        tracker.result = partial_completion

    return partial_completion


def get_constant_regex_value(pattern: str) -> str:
    """
    Get the value of a constant regex pattern.
    """
    for char in ESCAPED_CHARS:
        pattern = pattern.replace("\\" + char, char)

    return pattern


def is_constant_regex(pattern: str) -> bool:
    # Escaped characters to be considered when checking for a constant regex pattern

    # remove all escaped characters that have actually been escaped with \ from the pattern
    for char in ESCAPED_CHARS:
        pattern = pattern.replace("\\" + char, "")

    # not sure what escaping the space characters does
    pattern = pattern.replace("\\ ", " ")

    for char in ESCAPED_CHARS:
        if char in pattern:
            return False

    return True
