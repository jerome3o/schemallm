import numpy as np
from transformers import LogitsProcessor

from schemallm.vendored.rellm.logit_tracker import LogitTracker


def softmax(x: np.ndarray):
    """Compute softmax values for each sets of scores in x."""
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()


class LogitsMask(LogitsProcessor):
    """
    LogitsMask is a LogitsProcessor that masks logits for tokens that are
    not in the allowed token ids set.
    """

    last_prob = 0

    def __init__(self, allowed_token_ids, tracker: LogitTracker = None):
        self.allowed_token_ids = set(allowed_token_ids)
        self.allowed_token_ids_list = list(allowed_token_ids)
        self.logit_tracker = tracker

    def __call__(self, input_ids, scores):
        device = scores.device
        scores = scores.cpu()

        probs = softmax(scores.numpy()[0])
        self.last_prob = sum(probs[self.allowed_token_ids_list])

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
