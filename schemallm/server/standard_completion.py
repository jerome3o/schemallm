import torch
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    StoppingCriteriaList,
    StoppingCriteria,
)

from schemallm.models.api import (
    CompletionRequest,
    CompletionResponse,
)


class StopOnTokens(StoppingCriteria):
    def __init__(self, stop_ids: list):
        self.stop_ids = stop_ids
        super().__init__()

    def __call__(
        self,
        input_ids: torch.LongTensor,
        scores: torch.FloatTensor,
        **kwargs,
    ) -> bool:
        stop_ids = self.stop_ids
        for stop_id in stop_ids:
            if input_ids[0][-1] == stop_id:
                return True
        return False


@torch.inference_mode()
def complete_standard(
    model: AutoModelForCausalLM,
    tokenizer: AutoTokenizer,
    completion_request: CompletionRequest,
) -> CompletionResponse:
    # TODO(j.swannack): Add proper stop logic
    stop_token_list = [1, 2]
    input_ids = tokenizer.encode(completion_request.prompt, return_tensors="pt").to(
        model.device
    )
    all_tokens = model.generate(
        input_ids,
        # TODO(j.swannack): move validation to pydantic model
        temperature=max(min(completion_request.temperature, 1.0), 0.0),
        max_new_tokens=completion_request.max_tokens,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
        stopping_criteria=StoppingCriteriaList(
            [StopOnTokens(stop_ids=stop_token_list)]
        ),
    )

    tokens = all_tokens[0].tolist()

    # remove input tokens
    tokens = tokens[len(input_ids[0]) :]

    # remove end tokens
    if tokens[-1] in stop_token_list:
        tokens = tokens[:-1]

    # add more outputs if needed
    return CompletionResponse(
        completion=tokenizer.decode(tokens, skip_special_tokens=True)
    )
