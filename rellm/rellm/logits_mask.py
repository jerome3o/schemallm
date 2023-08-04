import numpy as np
from transformers import LogitsProcessor

from rellm.logit_tracker import LogitTracker


class LogitsMask(LogitsProcessor):
    """
    LogitsMask is a LogitsProcessor that masks logits for tokens that are
    not in the allowed token ids set.
    """

    def __init__(self, allowed_token_ids, tracker: LogitTracker = None):
        self.allowed_token_ids = set(allowed_token_ids)
        self.logit_tracker = tracker

    def __call__(self, input_ids, scores):
        device = scores.device
        scores = scores.cpu()
        mask = np.ones_like(scores) * -1e10
        for token_id in self.allowed_token_ids:
            mask[:, token_id] = 0

        if self.logit_tracker is not None:
            self.logit_tracker.add_step(
                logits_raw=scores.tolist()[0],
                allowed_ids=list(self.allowed_token_ids),
            )

        scores = scores + mask
        return scores.to(device)
