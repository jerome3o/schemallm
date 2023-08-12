from concurrent.futures import ThreadPoolExecutor
from typing import Dict, List, Set, Union

import regex
from transformers import PreTrainedTokenizer


class ReTokenFilter:
    def __init__(self, tokenizer: PreTrainedTokenizer):
        self.tokenizer = tokenizer
        self.decoded_tokens_cache = self.build_decoded_tokens_cache(tokenizer)

    @staticmethod
    def build_decoded_tokens_cache(tokenizer: PreTrainedTokenizer) -> Dict[int, str]:
        # TODO(j.swannack): apply mapping for special symbols.
        return {
            token_id: tokenizer.decode([token_id])
            for _, token_id in tokenizer.get_vocab().items()
        }

    def is_valid_token(
        self, token_id: int, partial_completion: str, patterns: List[regex.Pattern]
    ) -> bool:
        decoded_token = self.decoded_tokens_cache[token_id]

        # If the model is generating this token, it's likely trying to end the sequence or use some
        # other special token.
        # We only want to allow this token to generate if the regex is already matched.
        partial = decoded_token != ""

        # TODO(j.swannack): full completion, OR when there is a non-full standard match, that is
        #   longer than the original partial_completion
        return any(
            pattern.fullmatch(partial_completion + decoded_token, partial=partial)
            for pattern in patterns
        )

    def filter_tokens(
        self,
        partial_completion: str,
        patterns: Union[regex.Pattern, List[regex.Pattern]],
    ) -> Set[int]:
        if isinstance(patterns, regex.Pattern):
            patterns = [patterns]

        # TODO(j.swannack): investigate this, I don't think it works as intended.
        with ThreadPoolExecutor():
            valid_token_ids = set(
                filter(
                    lambda token_id: self.is_valid_token(
                        token_id, partial_completion, patterns
                    ),
                    self.decoded_tokens_cache.keys(),
                )
            )

        return valid_token_ids
