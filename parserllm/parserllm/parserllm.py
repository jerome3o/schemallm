import regex
from lark import UnexpectedInput, Lark
from transformers import PreTrainedModel, PreTrainedTokenizer

from rellm import complete_re
from rellm.logit_tracker import LogitTracker
from parserllm.logit_tracker import LogitTrackerParserLLM


def extract_terminal_regex(parser, stop_token):
    regex_map = {}
    for term in parser.terminals:
        if term.pattern:
            regex_map[term.name] = regex.compile(term.pattern.to_regexp(), regex.DOTALL)

    regex_map["$END"] = regex.compile(stop_token)
    return regex_map


class ParserState:
    def __init__(self, parser: Lark):
        self.parser: Lark = parser
        self.partial_token = ""

    def next_lex(self, input_str):
        try:
            self.parser.parse(input_str)
        except UnexpectedInput as e:
            # Assuming that self.parser is always LALR
            interactive = self.parser.parse_interactive(input_str)
            interactive.exhaust_lexer()
            return interactive.accepts()

        return []


def complete_cf(
    prompt: str,
    parser,
    partial_completion,
    tokenizer: PreTrainedTokenizer,
    model: PreTrainedModel,
    max_new_tokens: int = 3,
    debug: bool = False,
    tracker: LogitTrackerParserLLM = None,
    prob_limit: float = 0.1,
    **model_kwargs,
):
    """
    Complete a prompt with a regex pattern.
    """
    gen_tokens = 0
    prompt_plus_completion = prompt + partial_completion

    terminal_regexes = extract_terminal_regex(
        parser, tokenizer.decode(tokenizer.eos_token_id)
    )
    parser_state = ParserState(parser)

    vocab = tokenizer.get_vocab()
    index_to_token = {v: k for k, v in tokenizer.get_vocab().items()}

    while gen_tokens < max_new_tokens:
        valid_next_lex = parser_state.next_lex(partial_completion)

        if len(valid_next_lex) == 0 or (
            len(valid_next_lex) == 1 and "$END" in valid_next_lex
        ):
            break

        r = [terminal_regexes[t] for t in valid_next_lex]

        if debug:
            print(f"valid next token: {r}")

        re_tracker = None

        if tracker:
            re_tracker = LogitTracker(
                patterns=[p.pattern for p in r],
                token_to_index=vocab,
                index_to_token=index_to_token,
            )

        next_token_completion = complete_re(
            prompt_plus_completion,
            r,
            tokenizer,
            model,
            max_new_tokens=max_new_tokens,
            stop_after_match=True,
            debug=debug,
            tracker=re_tracker,
            prob_limit=prob_limit,
            **model_kwargs,
        )

        if tracker:
            tracker.re_steps.append(re_tracker)

        partial_completion += next_token_completion
        prompt_plus_completion = prompt_plus_completion + next_token_completion
        gen_tokens += 1

    return partial_completion
